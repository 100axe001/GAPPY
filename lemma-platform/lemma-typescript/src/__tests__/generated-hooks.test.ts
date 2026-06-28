import { describe, expect, it } from "vitest";
import { readFileSync, readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

import * as generated from "../react/generated/index.js";

// Wave 3 / CG-3 acceptance, across every generated resource: the barrel exports the
// hooks, queries are keyed under [resource, pod], and — the whole point — every
// mutation invalidates a query-key prefix the queries actually use. That alignment is
// what kills the stale-list footgun and is what would break if the generator's
// key/invalidation derivation ever drifts.

const HERE = dirname(fileURLToPath(import.meta.url));
const GEN_DIR = join(HERE, "../react/generated");
const files = readdirSync(GEN_DIR).filter((f) => f.endsWith(".ts") && f !== "index.ts");

describe("generated hooks", () => {
  it("barrel exports hooks for every resource", () => {
    for (const name of [
      "useRecordList",
      "useAgentList",
      "useTableCreate",
      "useScheduleGet",
      "useAppUpdate",
      "useFunctionDelete",
      "useWorkflowList",
    ]) {
      expect(typeof (generated as Record<string, unknown>)[name]).toBe("function");
    }
  });

  it("covers all 7 cleanly pod-scoped CRUD resources", () => {
    expect(files.length).toBe(7);
  });

  for (const file of files) {
    const src = readFileSync(join(GEN_DIR, file), "utf8");
    const resource = src.match(/\/\/ Resource: (\w+)/)?.[1] as string;

    describe(file, () => {
      it("every query key is scoped to [resource, pid, ...]", () => {
        const keys = [...src.matchAll(/queryKey: \[([^\]]*)\]/g)].map((m) => m[1]);
        expect(keys.length).toBeGreaterThan(0);
        for (const key of keys) {
          expect(key.startsWith(`"${resource}", pid`)).toBe(true);
        }
      });

      it("every mutation invalidates the resource prefix on success", () => {
        const mutations = src.split("export function").filter((b) => b.includes("useMutation({"));
        expect(mutations.length).toBeGreaterThan(0);
        for (const block of mutations) {
          expect(block).toContain("onSuccess");
          // invalidates a bare [resource, pid] prefix → a prefix of every query key above,
          // so the mutation refreshes the lists/entities with no manual refetch.
          expect(block).toMatch(/invalidateQueries\(\{ queryKey: \["[^"]+", pid\] \}\)/);
        }
      });
    });
  }
});
