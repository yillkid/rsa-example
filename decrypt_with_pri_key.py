from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode
import binascii

def bin2hex(bin_str):
    return binascii.hexlify(bin_str)

def hex2bin(hex_str):
    return binascii.unhexlify(hex_str)

def decrypt_with_pri_key(data):
    # Decrypt
    private_key = ""
    decrypted = ""
    with open("./private.pem", 'r') as outfile:
        private_key = outfile.read()

    privatekey = RSA.importKey(private_key)
    decryptor = PKCS1_OAEP.new(privatekey)

    # Convert string to byte
    encrypted = data.encode('ascii')

    # Hex to bin
    encrypted = hex2bin(encrypted)
    decrypted = decryptor.decrypt(encrypted)

    return decrypted.decode()


cyphertext = "0b1cdd4c9abf95a8784ce009c058746743bc59f7f4486d7423008bb6510b276ccd214fa6cf5839c2c1ac0ac5ec5456709d492f94afe931aa8a39ee7eb544dacd9b746edb27e43907c65c8de03c6aff25db34b01352e0e0e0630bf910c2fdd5225757bc3980b929b6ef31d3f4731b5b94f0208c955d0510aa888d4ec69c014b79"

cyphertext = decrypt_with_pri_key(cyphertext)

print(cyphertext)
