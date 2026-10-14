"""Run checksum-pinned actionlint on active and materialized starter workflows."""
import hashlib
import io
import platform
import subprocess
import tarfile
import tempfile
import urllib.request
import zipfile
from pathlib import Path

VERSION = "1.7.12"
DIGESTS = {
    ("Windows", "amd64"): "6e7241b51e6817ea6a047693d8e6fed13b31819c9a0dd6c5a726e1592d22f6e9",
    ("Linux", "amd64"): "8aca8db96f1b94770f1b0d72b6dddcb1ebb8123cb3712530b08cc387b349a3d8",
}
ROOT = Path(__file__).resolve().parents[1]

def main():
    machine = platform.machine().lower()
    architecture = "amd64" if machine in ("amd64", "x86_64") else machine
    system = platform.system()
    digest = DIGESTS.get((system, architecture))
    if not digest:
        raise SystemExit("Use actionlint 1.7.12 manually on this unsupported platform.")
    suffix = "zip" if system == "Windows" else "tar.gz"
    asset = f"actionlint_{VERSION}_{system.lower()}_{architecture}.{suffix}"
    url = f"https://github.com/rhysd/actionlint/releases/download/v{VERSION}/{asset}"
    request = urllib.request.Request(url, headers={"User-Agent": "Pragmatic-Ts-foundation-validation"})
    with urllib.request.urlopen(request, timeout=60) as response:
        archive = response.read(20 * 1024 * 1024 + 1)
    if len(archive) > 20 * 1024 * 1024:
        raise SystemExit("Tool archive exceeds size limit.")
    if hashlib.sha256(archive).hexdigest() != digest:
        raise SystemExit("Tool archive checksum mismatch.")
    with tempfile.TemporaryDirectory(prefix="foundation-actionlint-") as tmp:
        temp = Path(tmp)
        name = "actionlint.exe" if system == "Windows" else "actionlint"
        executable = temp / name
        if suffix == "zip":
            with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
                binary = bundle.read(name)
        else:
            with tarfile.open(fileobj=io.BytesIO(archive), mode="r:gz") as bundle:
                member = bundle.getmember(name)
                if not member.isfile():
                    raise SystemExit("Tool member is not a regular file.")
                binary = bundle.extractfile(member).read()
        executable.write_bytes(binary)
        executable.chmod(0o755)
        workflows = sorted((ROOT / ".github/workflows").glob("*.yml"))
        for template in sorted((ROOT / "workflow-templates").glob("*.yml")):
            destination = temp / template.name
            destination.write_text(template.read_text(encoding="utf-8").replace("$default-branch", "main"), encoding="utf-8")
            workflows.append(destination)
        if not workflows:
            raise SystemExit("No workflows found.")
        # ShellCheck/Pyflakes are not mandatory tool dependencies; actionlint validates
        # workflow keys, expressions and command wiring, not application behavior.
        subprocess.run([str(executable), "-shellcheck=", "-pyflakes=", *map(str, workflows)], check=True, cwd=ROOT)
        print(f"actionlint {VERSION}: {len(workflows)} workflows valid.")

if __name__ == "__main__":
    main()
