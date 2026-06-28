#!/usr/bin/env node
// Wave 3 / CG-3 — generate mechanical TanStack-Query hooks from x-lemma metadata.
//
// STRUCTURE comes from the backend's x-lemma metadata in the committed OpenAPI spec:
// which hooks exist, query vs mutation, the query key, and (the prize) which queries
// each mutation invalidates on success. That invalidation graph is what kills the
// stale-list footgun — it comes from the backend, not hand-maintained per consumer.
//
// TYPES come from the real facade via TypeScript's `Parameters<LemmaClient[...]>`, so
// the generator needs zero per-resource type knowledge and the compiler verifies every
// generated call. The only per-resource config is RESOURCES below: a resource -> public
// namespace mapping for the cleanly pod-scoped CRUD facades. Irregular verbs (run,
// stream, toggle, visualize, …) and differently-scoped resources (pod/org/user) are
// intentionally NOT generated — they stay in the hand-owned bespoke layer.
//
// Run: node scripts/generate_l2.mjs   (or: npm run generate:l2)

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const REPO = join(HERE, "..", "..");
const SPEC_PATH = join(REPO, "lemma-python", "lemma_sdk", "openapi_spec.json");
const OUT_DIR = join(HERE, "..", "src", "react", "generated");

// Cleanly pod-scoped CRUD resources: x-lemma resource -> public LemmaClient namespace.
const RESOURCES = [
  { resource: "record", ns: "records" },
  { resource: "agent", ns: "agents" },
  { resource: "table", ns: "tables" },
  { resource: "schedule", ns: "schedules" },
  { resource: "app", ns: "apps" },
  { resource: "function", ns: "functions" },
  { resource: "workflow", ns: "workflows" },
];

// Mechanical verbs we generate. Everything else is bespoke by design.
const VERB_METHOD = {
  list: ["list"],
  get: ["get"],
  create: ["create"],
  update: ["update"],
  delete: ["delete"],
  bulk_create: ["bulk", "create"],
  bulk_update: ["bulk", "update"],
  bulk_delete: ["bulk", "delete"],
};

const snakeToCamel = (s) => s.replace(/_([a-z])/g, (_, c) => c.toUpperCase());
const pascal = (s) => s.replace(/(^|[._])([a-z])/g, (_, __, c) => c.toUpperCase());

const pathParams = (template) =>
  [...template.matchAll(/\{([^}]+)\}/g)].map((m) => m[1]).filter((p) => p !== "pod_id");

function collectOps(spec, resource) {
  const ops = [];
  for (const [template, item] of Object.entries(spec.paths ?? {})) {
    for (const op of Object.values(item)) {
      const meta = op && op["x-lemma"];
      if (!meta || meta.resource !== resource || !VERB_METHOD[meta.verb]) continue;
      ops.push({
        meta,
        path: pathParams(template).map(snakeToCamel),
        hasBody: Boolean(op.requestBody),
      });
    }
  }
  return ops.sort((a, b) => a.meta.verb.localeCompare(b.meta.verb));
}

const typeRefOf = (ns, methodPath) =>
  `LemmaClient[${JSON.stringify(ns)}]${methodPath.map((m) => `[${JSON.stringify(m)}]`).join("")}`;

const hookNameOf = (resource, verb) => `use${pascal(resource)}${pascal(verb)}`;

function emitQuery(op, ns) {
  const { meta, path } = op;
  const methodPath = VERB_METHOD[meta.verb];
  const typeRef = typeRefOf(ns, methodPath);
  const call = `scoped.${ns}.${methodPath.join(".")}`;
  const isCollection = meta.result === "collection";

  const params = path.map((p, i) => `  ${p}: Parameters<${typeRef}>[${i}],`);
  if (isCollection) params.push(`  options?: Parameters<${typeRef}>[${path.length}],`);
  params.push("  queryOptions?: GeneratedQueryOptions,");

  const keyParts = [JSON.stringify(meta.resource), "pid", JSON.stringify(meta.verb), ...path];
  if (isCollection) keyParts.push("options ?? null");

  const callArgs = [...path];
  if (isCollection) callArgs.push("options");

  return `export function ${hookNameOf(meta.resource, meta.verb)}(
  client: LemmaClient,
  podId: string | undefined,
${params.join("\n")}
) {
  const scoped = resolvePodClient(client, podId);
  const pid = resolvePodId(client, podId);
  return useQuery({
    queryKey: [${keyParts.join(", ")}],
    queryFn: () => ${call}(${callArgs.join(", ")}),
    ...queryOptions,
  });
}`;
}

function emitMutation(op, ns) {
  const { meta, path, hasBody } = op;
  const methodPath = VERB_METHOD[meta.verb];
  const typeRef = typeRefOf(ns, methodPath);
  const call = `scoped.${ns}.${methodPath.join(".")}`;

  const fields = path.map((p, i) => `${p}: Parameters<${typeRef}>[${i}]`);
  if (hasBody) fields.push(`payload: Parameters<${typeRef}>[${path.length}]`);
  const callArgs = path.map((p) => `vars.${p}`);
  if (hasBody) callArgs.push("vars.payload");

  const invalidations = (meta.invalidates ?? [])
    .map((target) => `      void queryClient.invalidateQueries({ queryKey: [${JSON.stringify(target)}, pid] });`)
    .join("\n");

  return `export function ${hookNameOf(meta.resource, meta.verb)}(client: LemmaClient, podId?: string) {
  const queryClient = useQueryClient();
  const scoped = resolvePodClient(client, podId);
  const pid = resolvePodId(client, podId);
  return useMutation({
    mutationFn: (vars: { ${fields.join("; ")} }) => ${call}(${callArgs.join(", ")}),
    onSuccess: () => {
${invalidations}
    },
  });
}`;
}

function emitResource(spec, { resource, ns }) {
  const ops = collectOps(spec, resource);
  const blocks = ops.map((op) => (op.meta.kind === "query" ? emitQuery(op, ns) : emitMutation(op, ns)));
  const header = `// GENERATED by scripts/generate_l2.mjs from x-lemma metadata — do not edit by hand.
// Resource: ${resource}. Regenerate with: npm run generate:l2
//
// Mechanical TanStack-Query hooks over the ${ns} facade. Query keys and the mutation
// invalidation graph are derived from the backend's x-lemma metadata, so a mutation
// refreshes exactly the lists/entities it should — no manual refetch. Types are pulled
// from the real facade via Parameters<>, so the compiler verifies every call.
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import type { LemmaClient } from "../../client.js";
import { resolvePodClient, resolvePodId, type GeneratedQueryOptions } from "../utils.js";
`;
  return { code: header + "\n" + blocks.join("\n\n") + "\n", count: ops.length };
}

function main() {
  const spec = JSON.parse(readFileSync(SPEC_PATH, "utf8"));
  mkdirSync(OUT_DIR, { recursive: true });

  const exportLines = [];
  let total = 0;
  for (const config of RESOURCES) {
    const { code, count } = emitResource(spec, config);
    writeFileSync(join(OUT_DIR, `${config.ns}.ts`), code, "utf8");
    exportLines.push(`export * from "./${config.ns}.js";`);
    total += count;
    console.log(`  ${count} hooks  ${config.resource} -> src/react/generated/${config.ns}.ts`);
  }

  const barrel = `// GENERATED by scripts/generate_l2.mjs — do not edit by hand.\n${exportLines.join("\n")}\n`;
  writeFileSync(join(OUT_DIR, "index.ts"), barrel, "utf8");
  console.log(`total: ${total} generated hooks across ${RESOURCES.length} resources`);
}

main();
