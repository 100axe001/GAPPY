import { copyFileSync, mkdirSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { build } from "esbuild";

// Opt-in UI bundle: the vanilla web components (<lemma-agent-task>,
// <lemma-agent-thread>) as a classic-script IIFE that sets `window.LemmaUI` and
// auto-registers the elements on load. Separate from lemma-client.js so a desk
// only pays for UI when it loads this script. No React — built on the agent core.
const sdkDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const entry = path.join(sdkDir, "src", "browser-ui.ts");
const outFile = path.join(sdkDir, "dist", "browser", "lemma-ui.js");
const publicOutFile = path.join(sdkDir, "public", "lemma-ui.js");

mkdirSync(path.dirname(outFile), { recursive: true });
mkdirSync(path.dirname(publicOutFile), { recursive: true });

await build({
  entryPoints: [entry],
  bundle: true,
  format: "iife",
  globalName: "LemmaUI",
  platform: "browser",
  target: "es2019",
  define: {
    "import.meta.env": "undefined",
    "process.env.NODE_ENV": '"production"',
  },
  legalComments: "none",
  outfile: outFile,
});

copyFileSync(outFile, publicOutFile);
console.log(`Built UI bundle (esbuild) at ${outFile}`);
console.log(`Updated committed UI bundle at ${publicOutFile}`);
