# Lab 1 — Encryption & Oracle Attacks (SEED Labs)

This lab explores fundamental cryptographic concepts using SEED Labs,
focusing on encryption mechanisms and oracle-based analysis.

All experiments were conducted in isolated Docker-based virtual
environments for educational purposes.

---

## Objectives

- Understand block cipher encryption behavior
- Explore the role of initialization vectors (IVs)
- Analyze encryption oracle responses
- Perform basic ciphertext analysis and frequency inspection

---

## Environment

- Platform: SEED Labs
- Execution: Docker containers
- Network: Isolated private environment
- Languages: C++, Python

---

## Contents

### `encryption_files_setup/`
Contains the lab setup files provided by SEED Labs, including:

- `docker-compose.yml` — Container orchestration
- `encryption_oracle/` — Oracle service source code
- `Files/` — Sample plaintexts, ciphertexts, and analysis scripts

### Notable Files
- `evp-encrypt.hpp` — Encryption utilities
- `server.cpp` — Oracle server logic
- `freq.py` — Frequency analysis helper script

---

## Notes

Screenshots for this portion of the lab were included in the original
course submission document and are not reproduced here.

This lab is intended to strengthen understanding of cryptographic
design and potential weaknesses when encryption is misused.

