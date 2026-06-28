import { copyFileSync, mkdirSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { build } from "esbuild";

// Bundle the browser entry into a single classic-script IIFE that sets
// `window.LemmaClient`. esbuild (not the old hand-rolled bundler) is required
// because the entry pulls in bare npm deps (supertokens-web-js) and uses
// `import.meta.env` — both of which a classic <script> cannot handle unless
// they are inlined / defined away at build time.
const sdkDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const entry = path.join(sdkDir, "src", "browser.ts");
const outFile = path.join(sdkDir, "dist", "browser", "lemma-client.js");
const publicOutFile = path.join(sdkDir, "public", "lemma-client.js");

mkdirSync(path.dirname(outFile), { recursive: true });
mkdirSync(path.dirname(publicOutFile), { recursive: true });

await build({
  entryPoints: [entry],
  bundle: true,
  format: "iife",
  // window.LemmaClient = { LemmaClient, AuthManager, ... } → the class is
  // window.LemmaClient.LemmaClient (matches the documented HTML usage).
  globalName: "LemmaClient",
  platform: "browser",
  target: "es2019",
  // config.ts reads import.meta.env behind a try/catch + truthiness guard, so
  // undefined is safe; this also removes the parse-time `import.meta` token
  // that breaks classic scripts. NODE_ENV keeps bundled deps on prod paths.
  define: {
    "import.meta.env": "undefined",
    "process.env.NODE_ENV": '"production"',
  },
  legalComments: "none",
  outfile: outFile,
});

copyFileSync(outFile, publicOutFile);
console.log(`Built browser bundle (esbuild) at ${outFile}`);
console.log(`Updated committed browser bundle at ${publicOutFile}`);
