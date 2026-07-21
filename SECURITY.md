# Security Policy

## Supported versions

Security fixes are provided for the latest released minor version. Adopting
packages must replace this statement with their actual support window and
supported Python versions.

## Reporting a vulnerability

Use the repository's private GitHub security-advisory form. Do not open a
public issue containing exploit details, credentials, or private data. The
maintainers will acknowledge a report within five business days and provide a
status update within ten business days. These are response targets, not a
guarantee of remediation time.

## Disclosure and dependencies

Coordinated disclosure is preferred. Confirmed critical and high dependency
vulnerabilities block release unless a documented, time-bounded exception is
approved. Capability and heuristic alerts require evidence-based review and
are not treated as vulnerabilities by label alone.

Releases should use PyPI Trusted Publishing, protected environments, immutable
workflow dependencies, provenance attestations, and wheel-first verification.
Adopting repositories must document whether these controls are enabled.
