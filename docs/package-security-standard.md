# Python Package Supply-Chain Standard

## Required controls

Each adopting package must inventory direct, optional, development, test,
documentation, and transitive dependencies. Runtime dependencies require
tested lower and upper compatibility bounds. Exact versions and hashes belong
in environment-specific `requirements/*.txt` files generated from reviewed
`.in` inputs, not in library metadata. `.lock` filenames are not used because
they cannot be saved reliably in the configured OneDrive workspace.

Release candidates must pass tests, `pip check`, `pip-audit`, build and Twine
validation, artifact inspection, wheel-only installation, and sdist
installation. Optional extras require isolated CI coverage and lazy imports.
Confirmed critical or high vulnerabilities, malware, typosquatting,
dependency-confusion exposure, or unexplained executable payloads block a
release.

Behavioural capabilities and heuristic findings require package-, version-,
artifact-, and file-level evidence. Expected native code in established
scientific packages is monitored rather than suppressed globally. Every
exception is narrowly scoped, owned, dated, and reassessed on version change.

## Adoption sequence

1. Copy the security documentation templates and identify an owner.
2. Record dependency groups and every scanner alert.
3. Generate hash-pinned `.txt` requirement sets separately for every materially
   different supported Python environment with `pip-compile --generate-hashes`.
4. Call reusable workflows by a reviewed immutable commit SHA.
5. Add minimum-version, latest-compatible, and optional-extra test jobs.
6. Configure protected branches, CODEOWNERS, secret scanning, push protection,
   and dependency review in repository settings.
7. Publish through a protected environment and PyPI Trusted Publishing; grant
   `id-token: write` only to the publish job.
8. Attach an SPDX or CycloneDX SBOM and provenance to the release, then install
   and smoke-test the published wheel.

## Alert decision record

Use the following fields for each alert: name, package, version, artifact, file
path, direct/transitive status, advisory, runtime relevance, expected
capability, action, disposition, evidence, owner, review date, and reassessment
trigger. Allowed dispositions are `FIX`, `UPGRADE`, `REPLACE`, `REMOVE`,
`CONSTRAIN`, `MOVE TO OPTIONAL EXTRA`, `MONITOR`, `FALSE POSITIVE`,
`ACCEPTED RISK`, and `BLOCK RELEASE`.

## Workflow trust

The example workflows pin each third-party `uses:` reference to the commit
currently resolved from its documented major-version tag. Dependabot should
propose controlled updates. Adopting repositories must reference reusable
workflows by a reviewed immutable SHA as well.
