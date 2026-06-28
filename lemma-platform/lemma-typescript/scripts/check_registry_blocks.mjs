import { existsSync, readFileSync } from "node:fs";
import { basename, join } from "node:path";

const root = process.cwd();
const registryPath = join(root, "registry.json");
const generatedRoot = join(root, "public", "r");

function fail(message) {
  console.error(`registry check failed: ${message}`);
  process.exitCode = 1;
}

function readJson(path) {
  return JSON.parse(readFileSync(path, "utf8"));
}

const registry = readJson(registryPath);
const generatedIndexPath = join(generatedRoot, "registry.json");

if (!existsSync(generatedIndexPath)) {
  fail("public/r/registry.json is missing. Run npm run registry:build first.");
}

const generatedIndex = existsSync(generatedIndexPath) ? readJson(generatedIndexPath) : { items: [] };
const generatedNames = new Set((generatedIndex.items ?? []).map((item) => item.name));

for (const item of registry.items ?? []) {
  if (!generatedNames.has(item.name)) {
    fail(`generated registry index is missing item "${item.name}"`);
  }

  const itemPath = join(generatedRoot, `${item.name}.json`);
  if (!existsSync(itemPath)) {
    fail(`generated item file is missing for "${item.name}"`);
    continue;
  }

  const generatedItem = readJson(itemPath);
  if (generatedItem.name !== item.name) {
    fail(`generated item file ${basename(itemPath)} has name "${generatedItem.name}"`);
  }

  for (const file of item.files ?? []) {
    const sourcePath = join(root, file.path);
    if (!existsSync(sourcePath)) {
      fail(`${item.name} references missing source file ${file.path}`);
    }
  }

  for (const file of generatedItem.files ?? []) {
    const target = file.target ?? "";
    const content = file.content ?? "";
    if (!target || !content) continue;

    if (content.includes("../../lemma-assistant-experience/")) {
      fail(`${item.name}:${target} contains a source-tree relative assistant import`);
    }

    const isClientLikeTsx =
      target.endsWith(".tsx") &&
      /(useState|useEffect|useMemo|useRef|useCallback|onClick=|onChange=|onKeyDown=|window\.|document\.|FileList)/.test(content);
    if (isClientLikeTsx && !content.trimStart().startsWith('"use client"')) {
      fail(`${item.name}:${target} appears client-side but is missing "use client"`);
    }
  }
}

if (!process.exitCode) {
  console.log(`registry check passed (${registry.items?.length ?? 0} items)`);
}
