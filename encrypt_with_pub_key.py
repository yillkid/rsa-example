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

def encrypt_with_pub_key(pub_key, data):
    publickey = RSA.importKey(pub_key)
    encryptor = PKCS1_OAEP.new(publickey)
    # Convert data to byte and encrypt it
    encrypted = encryptor.encrypt(str.encode((data)))
    # Convert byte to hex
    encrypted = bin2hex(encrypted)
    # Convert hex to string
    encrypted = encrypted.decode('ascii')

    return encrypted

pub_key = "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDcFvnPAoK/RC/HCGAhJochITd9\n5XJASaSyM/Q6hZm8FHLoYDpqBzpuakwfhswBLOQpwQACdJF8I6ce+cwfjQ33aDHs\n5NncIKqP68axy7HIh4RMB2K//1Pgxkp4BmAMXuHIqtivRSZdjkob7A6RbXE9GrNw\nsHP56r5yDyEZqXm+ywIDAQAB\n-----END PUBLIC KEY-----"

cyphertext = encrypt_with_pub_key(pub_key, "123")

print(cyphertext)
