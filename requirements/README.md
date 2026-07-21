# Reproducible requirement sets

The reviewed `.in` files are compiled to exact, hash-pinned `.txt` files. The
project intentionally does not use `.lock` files because they cannot be stored
reliably in the configured OneDrive workspace.

Regenerate with the oldest maintained Python minor version:

```powershell
python -m piptools compile --generate-hashes --resolver=backtracking `
  --output-file requirements/test.txt requirements/test.in
python -m piptools compile --generate-hashes --resolver=backtracking `
  --output-file requirements/release.txt requirements/release.in
```

Install without changing the reviewed resolution:

```powershell
python -m pip install --require-hashes -r requirements/test.txt
```
