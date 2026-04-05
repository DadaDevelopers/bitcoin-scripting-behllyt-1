# Assignment A — Bitcoin Script Analysis

## The Script
OP_DUP OP_HASH160 <PubKeyHash> OP_EQUALVERIFY OP_CHECKSIG

This script is called P2PKH (Pay to Public Key Hash).
It is the most classic Bitcoin locking script.

---

## 1. What Each Opcode Does

### OP_DUP
- Duplicates the top item on the stack
- At this point the stack has your Public Key
- After OP_DUP the stack has two copies of your Public Key
- Like a photocopier makes an exact copy

### OP_HASH160
- Takes the top item which is the copy of your Public Key
- Runs it through two hashing functions SHA256 then RIPEMD160
- Produces a short fixed-length fingerprint of your Public Key
- Same key always gives the same result but you cannot reverse it

### <PubKeyHash>
- This is not an opcode it is the expected hash stored in the script
- It was put there by the sender when they created the output
- It is the hash of the recipients public key

### OP_EQUALVERIFY
- Compares the two hashes on the stack
- If they match continue
- If they do not match STOP transaction fails

### OP_CHECKSIG
- Takes the signature and public key from the stack
- Verifies the signature was made with the correct private key
- If valid transaction succeeds output is unlocked
- If invalid transaction fails

---

## 2. Data Flow Diagram

Start:
Stack: [Signature, PublicKey]

OP_DUP → Duplicate PublicKey
Stack: [Signature, PublicKey, PublicKey]

OP_HASH160 → Hash the top PublicKey
Stack: [Signature, PublicKey, Hash(PublicKey)]

<PubKeyHash> → Push stored hash onto stack
Stack: [Signature, PublicKey, Hash(PublicKey), PubKeyHash]

OP_EQUALVERIFY → Compare the two hashes
Match?  YES continue   NO FAIL
Stack: [Signature, PublicKey]

OP_CHECKSIG → Verify signature against PublicKey
Valid?  YES SUCCESS   NO FAIL
Stack: [TRUE]

---

## 3. What Happens if Signature Verification Fails

- The stack returns FALSE
- The transaction is immediately rejected
- The Bitcoin output stays locked
- Nobody loses any money the coins stay where they are
- The failed transaction is not added to the blockchain

---

## 4. Security Benefits of Hash Verification

1. PRIVACY
   - Your full public key is never revealed until you spend
   - The world only sees a short hash of it

2. SHORTER ADDRESSES
   - A public key is 33 bytes
   - A hash is only 20 bytes
   - Smaller means cheaper to store on the blockchain

3. QUANTUM RESISTANCE
   - Hashing adds an extra layer of protection
   - An attacker would still need to reverse the hash first

4. INTEGRITY
   - You cannot fake a hash
   - Same input always gives same output
   - Guarantees the right person is being paid
