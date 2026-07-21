# Reproducible requirement sets

The reviewed `.in` files are compiled to exact, hash-pinned `.txt` files. The
project intentionally does not use `.lock` files because they cannot be stored
reliably in the configured OneDrive workspace.

Generate the CI and release sets on Linux with Python 3.12 so
platform-conditional dependencies match the reusable workflow runner:

```powershell
docker run --rm -v "${PWD}:/workspace" -w /workspace python:3.12-slim sh -c 'python -m pip install "pip-tools>=7.5,<8" && pip-compile --generate-hashes --resolver=backtracking --strip-extras --no-emit-index-url --no-emit-trusted-host requirements/test.in -o requirements/test.txt && pip-compile --generate-hashes --resolver=backtracking --strip-extras --no-emit-index-url --no-emit-trusted-host requirements/release.in -o requirements/release.txt'
```

Install without changing the reviewed resolution:

```powershell
python -m pip install --require-hashes -r requirements/test.txt
```
