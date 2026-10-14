import test from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { mkdtempSync, cpSync, rmSync, readFileSync, writeFileSync, unlinkSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
const root = resolve(import.meta.dirname, "..");
const python = process.env.PYTHON || (process.platform === "win32" ? "python" : "python3");
function planning(fixture) {
  return spawnSync(python, [join(root, "templates/product/scripts/validate_project.py"), "--root", fixture], {encoding:"utf8"});
}
function fixture(run) {
  const directory = mkdtempSync(join(tmpdir(), "foundation-planning-"));
  try { cpSync(join(root, "templates/product"), directory, {recursive:true}); run(directory); }
  finally { rmSync(directory, {recursive:true, force:true}); }
}
test("complete planning skeleton passes structure without claiming acceptance", () => fixture(directory => {
  const result = planning(directory);
  assert.equal(result.status, 0, result.stderr + result.stdout);
  assert.match(result.stdout, /Content and acceptance require human review/);
}));
test("missing local agent instructions fail", () => fixture(directory => {
  unlinkSync(join(directory, "AGENTS.md"));
  const result = planning(directory);
  assert.equal(result.status, 1);
  assert.match(result.stdout, /Missing AGENTS.md/);
}));
test("missing success criteria fail", () => fixture(directory => {
  const path = join(directory, "PROJECT.md");
  writeFileSync(path, readFileSync(path, "utf8").replace("## Success criteria", "## Unrelated"));
  const result = planning(directory);
  assert.equal(result.status, 1);
  assert.match(result.stdout, /Missing PROJECT.md section: Success criteria/);
}));
test("empty problem evidence section fails", () => fixture(directory => {
  const path = join(directory, "PROJECT.md");
  writeFileSync(path, readFileSync(path,"utf8").replace(/## Validated problem[\s\S]*?(?=## Scope)/, "## Validated problem\n\n"));
  const result = planning(directory);
  assert.equal(result.status, 1);
  assert.match(result.stdout, /Empty PROJECT.md section: Validated problem/);
}));
test("duplicate roadmap section fails", () => fixture(directory => {
  const path = join(directory, "PROJECT.md");
  writeFileSync(path, readFileSync(path,"utf8") + "\n## Roadmap and priorities\nDuplicate\n");
  const result = planning(directory);
  assert.equal(result.status, 1);
  assert.match(result.stdout, /Duplicate PROJECT.md section: Roadmap and priorities/);
}));

function foundationFixture(run) {
  const directory = mkdtempSync(join(tmpdir(), "foundation-policy-"));
  try { cpSync(root, directory, {recursive:true}); run(directory); }
  finally { rmSync(directory, {recursive:true, force:true}); }
}
function validateFoundation(directory) {
  return spawnSync(python, ["-c",
    "import importlib.util, sys; from pathlib import Path; spec=importlib.util.spec_from_file_location('validation', sys.argv[1]); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); errors=mod.validate(Path(sys.argv[2])); print('\\n'.join(errors)); sys.exit(bool(errors))",
    join(directory, "scripts/validate_foundation.py"), directory], {encoding:"utf8"});
}
test("broken documentation links fail", () => foundationFixture(directory => {
  writeFileSync(join(directory,"README.md"), "[broken](missing.md)\n");
  const result = validateFoundation(directory);
  assert.equal(result.status,1,result.stderr);
  assert.match(result.stdout,/Broken local link/);
}));
test("unpinned third-party actions fail", () => foundationFixture(directory => {
  const path = join(directory,".github/workflows/foundation.yml");
  writeFileSync(path,readFileSync(path,"utf8").replace(/actions\/checkout@[a-f0-9]{40}/,"actions/checkout@main"));
  const result = validateFoundation(directory);
  assert.equal(result.status,1,result.stderr);
  assert.match(result.stdout,/Unpinned external action/);
}));
test("duplicate issue form IDs fail", () => foundationFixture(directory => {
  const path = join(directory,".github/ISSUE_TEMPLATE/bug_report.yml");
  writeFileSync(path,readFileSync(path,"utf8").replace("id: reproduction","id: behavior"));
  const result = validateFoundation(directory);
  assert.equal(result.status,1,result.stderr);
  assert.match(result.stdout,/duplicate issue field IDs/);
}));
test("missing active CI fails instead of silently checking nothing", () => foundationFixture(directory => {
  unlinkSync(join(directory,".github/workflows/foundation.yml"));
  const result = validateFoundation(directory);
  assert.equal(result.status,1,result.stderr);
  assert.match(result.stdout,/Missing .github\/workflows\/foundation.yml/);
}));
