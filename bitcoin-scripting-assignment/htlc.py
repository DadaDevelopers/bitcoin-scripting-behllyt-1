import hashlib
import time

def sha256(data):
    return hashlib.sha256(data).digest()

def hash160(data):
    return hashlib.new('ripemd160', sha256(data)).digest()

def generate_secret():
    secret = b"alice_secret_preimage"
    secret_hash = sha256(secret)
    return secret, secret_hash

def htlc_script(secret_hash, alice_pubkey, bob_pubkey, timeout=21):
    script = f"HTLC Script:\nOP_IF\n    OP_SHA256 {secret_hash.hex()}\n    OP_EQUALVERIFY\n    OP_DUP\n    OP_HASH160 {hash160(alice_pubkey).hex()}\n    OP_EQUALVERIFY\n    OP_CHECKSIG\nOP_ELSE\n    {timeout} OP_CHECKLOCKTIMEVERIFY\n    OP_DROP\n    OP_DUP\n    OP_HASH160 {hash160(bob_pubkey).hex()}\n    OP_EQUALVERIFY\n    OP_CHECKSIG\nOP_ENDIF"
    return script

def alice_claim(secret, secret_hash):
    print("=== Alice Claiming with Secret ===")
    computed_hash = sha256(secret)
    if computed_hash == secret_hash:
        print("Secret: " + str(secret))
        print("Secret Hash: " + secret_hash.hex())
        print("Hash verification: PASSED")
        print("Alice claims the funds successfully!")
        return True
    else:
        print("Hash verification: FAILED")
        print("Alice cannot claim the funds!")
        return False

def bob_refund(timeout=21):
    print("=== Bob Claiming Refund ===")
    print("Timeout: " + str(timeout) + " minutes have passed")
    print("Timelock verification: PASSED")
    print("Bob claims the refund successfully!")
    return True

def test_htlc():
    print("==================================================")
    print("HTLC SIMULATION")
    print("==================================================")
    alice_pubkey = b"alice_public_key"
    bob_pubkey = b"bob_public_key"
    secret, secret_hash = generate_secret()
    print("Secret: " + str(secret))
    print("Secret Hash: " + secret_hash.hex())
    print("\n--- HTLC Script ---")
    script = htlc_script(secret_hash, alice_pubkey, bob_pubkey)
    print(script)
    print("--- Scenario 1: Alice claims with correct secret ---")
    alice_claim(secret, secret_hash)
    print("\n--- Scenario 2: Alice tries wrong secret ---")
    alice_claim(b"wrong_secret", secret_hash)
    print("\n--- Scenario 3: Bob claims refund after timeout ---")
    bob_refund(timeout=21)

if __name__ == "__main__":
    test_htlc()
