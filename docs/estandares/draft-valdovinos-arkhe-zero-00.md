# draft-valdovinos-arkhe-zero-00
# ARKHE-ZERO: Requirements for Human-AI Co-Authorship Verification
# Status: Internet-Draft, version 00, November 2026
# Author: Valdovinos, Marco Antonio Rojas Valdovinos, Toluca-Global, Mexico

## Abstract
This document defines requirements for verifying human-AI co-authored works.
It follows the same archiving principles as RFC 6778: stable URI per record,
search by author, date, identifier, export in standard format, redundancy,
and integrity preservation.

## Model
51% Human decides. 49% AI orders and builds.
Human is Sovereign. AI is Architect.

## Requirements

1. Each verified file MUST have a stable URI: /verify/<FOLIO>
2. Each record MUST contain: folio, SHA-256, filename, size, date, author, model 51/49
3. System MUST allow searching by folio, SHA-256, author, date, filename
4. System MUST allow exporting record as JSON + HTML with same structure
5. System MUST preserve integrity: if one byte changes, folio becomes invalid
6. System MUST NOT require login for public records
7. System MUST support redundancy: GitHub Pages + Zenodo DOI + local copy

## Example
Folio: KRONOS-20261121-604A4EF0
SHA-256: 604a4ef04b88c46d351c0ae37f0efa6a00837f41d1f7f76988d85151884833da

## Status
This is version 00. Intended for public review, like draft-sparks-genarea-mailarch-00 was for RFC 6778.

— Valdovinos • KRONOS2099 • ARKHE-ZERO
