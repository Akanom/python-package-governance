# Release Integrity Checklist

- Build from a clean, reviewed tag in CI.
- Install test and release tools from hash-pinned `requirements/*.txt` files
  generated from reviewed `.in` inputs; do not create `.lock` files in the
  OneDrive workspace.
- Run the full test and security matrix before publication.
- Build both wheel and sdist and validate them with Twine.
- Save the JSON artifact inventory and review unexpected payloads.
- Install and smoke-test the wheel with `--only-binary=:all:`.
- Install and smoke-test the sdist in a separate clean environment.
- Generate and attach an SBOM and provenance attestation.
- Publish with PyPI Trusted Publishing from a protected environment.
- Grant `id-token: write` only to the publication job.
- Verify hashes and smoke-test the artifact downloaded from PyPI.
- Record the workflow run, source revision, build environment, and results.
