from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import binascii
key=RSA.generate(2048)
privatekey=key.export_key()
publicc=key.publickey()
publickey=publicc.export_key()

def rsa_enc_public(inputblock,keypair):
    rsakey = RSA.import_key(keypair)
    cipher = PKCS1_v1_5.new(rsakey)
    return cipher.encrypt(inputblock)
def rsa_dec_private(cipherblock,keypair):
    rsakey = RSA.import_key(keypair)
    cipher = PKCS1_v1_5.new(rsakey)
    return cipher.decrypt(cipherblock,sentinel=None)#sential only for decrypt in PKCS1_v1_5

a=str(input("Please enter the strings to encrypt and decrypt :-"))
print("the plane text is",a)
a=a.encode()
encrypted=rsa_enc_public(a,publickey)
decrypteddd=rsa_dec_private(encrypted,privatekey)
print("the encrypted block is ",binascii.hexlify(encrypted))
print("the decrypted block is ",decrypteddd.decode("utf-8"))