from base64 import (
    b64encode,
    b64decode,
)

from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA


message = "I want this stream signed".encode("utf-8")
digest = SHA256.new()
digest.update(message)

# Read shared key from file
private_key = False
with open ("private.pem", "r") as myfile:
    private_key = RSA.importKey(myfile.read())

# Load private key and sign message
signer = PKCS1_v1_5.new(private_key)
sig = signer.sign(digest)

print("Signature: " + sig.hex())

# Load public key and verify message
verifier = PKCS1_v1_5.new(private_key.publickey())
verified = verifier.verify(digest, sig)
assert verified, 'Signature verification failed'
print ("Successfully verified message")
