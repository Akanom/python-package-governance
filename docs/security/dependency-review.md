# Dependency Review

Review date: 2026-07-21

## Scope and status

The active repositories are `systemgmmkit`, `limiteddepkit`, and
`universal-output-hub`. Their build, runtime, optional, test, documentation,
and release dependency groups are bounded and covered by hash-pinned
requirement sets. An isolated `pip-audit` 2.10.1 OSV scan resolved 13, 6, and
23 dependencies respectively and found no known vulnerabilities.

This result is point-in-time evidence, not a permanent safety claim. CI repeats
the audit, validates dependency consistency, reviews dependency diffs, and
blocks high-severity findings.

## NumPy 2.5.1 archive review

- Source: official PyPI source distribution.
- SHA-256:
  `a48a113e6afea91f5608793bafa7ef2ad481fefbda87ec5069f483de61cb9fa3`.
- Hash result: matched the PyPI-published digest.
- Nested archives: five Meson test fixtures; two contain only `dummy\n`, and
  three contain only small Meson/Rust test sources.
- Executable payloads in those fixtures: none found.
- Disposition: `MONITOR` because the exact Socket artifact/report identifier
  was not available for a byte-for-byte correlation. The evidence does not
  justify removing NumPy, declaring a false positive, or recording an accepted
  risk.

## Optional-dependency decisions

- `systemgmmkit`: Matplotlib moved to `plots`; core imports are tested without
  it.
- `limiteddepkit`: Matplotlib remains in `plots`; missing plotting support has
  an actionable error and a regression test.
- `universal-output-hub`: Excel, Parquet, DOCX, and PDF backends moved to
  format-specific extras with guarded imports.

## Reassessment triggers

Re-run the review when a resolved version or artifact hash changes, a new
scanner/advisory finding appears, a binary or nested archive enters a built
distribution, or a dependency moves between core and optional scope.
