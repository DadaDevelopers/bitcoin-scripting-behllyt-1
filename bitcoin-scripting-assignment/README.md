# Bitcoin Scripting Assignment

## Files
- assignment-a.md — Analysis of P2PKH Bitcoin script
- htlc.py — Hashed Time-Lock Contract implementation
- output.txt — Output from running htlc.py
- README.md — This file

## How to Run
python3 htlc.py

## Assignment A Summary
The script OP_DUP OP_HASH160 <PubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
is a P2PKH locking script. It verifies that the spender owns the
correct private key by checking their public key hash and signature.

## Assignment B Summary
The HTLC allows two parties to swap Bitcoin safely:
- Alice can claim funds using a secret preimage within 21 minutes
- Bob gets a refund automatically after 21 minutes
- Uses SHA256 hashing and CHECKLOCKTIMEVERIFY for enforcement

## Test Results
- Alice claiming with correct secret: PASSED
- Alice claiming with wrong secret: FAILED as expected
- Bob claiming refund after timeout: PASSED
