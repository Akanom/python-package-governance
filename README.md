# Python Package Governance

Reusable, fail-closed supply-chain checks and policy templates for Python
libraries. This repository is a governance baseline; it is not evidence that a
specific package or scanner alert has been reviewed.

## Local checks

```powershell
python scripts/verify_dependencies.py --project .
python scripts/inspect_dist.py dist
python -m pytest
```

`verify_dependencies.py` validates declared dependency syntax, rejects direct
URLs and unbounded runtime requirements, and can run `pip check` and
`pip-audit`. `inspect_dist.py` inventories wheels and source distributions and
fails on secrets, path traversal, unexpected binary/archive payloads, or files
outside an explicit allow-list.

Adopting repositories should copy the templates, call the reusable workflows
by immutable commit SHA, compile project-specific `requirements/*.in` files to
hash-pinned `requirements/*.txt` files, and record every scanner finding in
`docs/security/dependency-review.md`. This convention avoids `.lock` files,
which cannot be stored reliably in the configured OneDrive workspace.

See [the security standard](docs/package-security-standard.md) and [the current
handover gap assessment](docs/security/dependency-review.md).
