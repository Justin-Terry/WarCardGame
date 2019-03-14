import os
import binascii
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (Cipher, algorithms, modes)
from cryptography.hazmat.primitives import (padding)


def MyEncrypt(message, key):
    # Create a padder using PKCS7 padding mode
    padder = padding.PKCS7(128).padder()
    # Add the message to the padder
    paddedToEncrypt = padder.update(message)
    # Adds padding to the end of the message in the padder
    paddedToEncrypt += padder.finalize()
    # Generate an IV
    iv = os.urandom(16)
    # Create the cipher using the key in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    # Creates an encryptor that uses the cipher that was just built
    encryptor = cipher.encryptor()
    # Creates a ciphertext from the encryptor
    cipherText = encryptor.update_into(paddedToEncrypt) + encryptor.finalize()
    # Return the cipher text and IV
    return cipherText, iv

def MyDecrypt(cipherText, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    buffer = bytearray((len(cipherText)+32-1))
    len_decrypted = decryptor.update_into(cipherText, buffer)
    string = bytes(buffer[:len_decrypted]) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    unpadded = unpadder.update(string)
    unpadded += unpadder.finalize()
    return unpadded

def MyFileEncrypt(filepath):
    # Get the file extension
    ext = getExtension(filepath)
    # Open the file and reads the bytes
    file = open(filepath, "rb")
    fileBytes = file.read()
    # Generate a key
    key = os.urandom(16)
    # Encrypt the file using the key
    cipherText, iv = MyEncrypt(fileBytes, key)

    return cipherText, iv, key, ext

def getExtension(filepath):
    return os.path.splitext(filepath)[1]

cit, iv, key, ext = MyFileEncrypt("image.jpg")
print(cit)
print(iv)
print(key)
print(ext)

fileName = "encrypted" + ext
f = open(fileName, "wb")
f.write(cit)
f.close()

newFileName = "decrypted" + ext
newFile = open(newFileName, "wb")
newFile.write(MyDecrypt(cit, key, iv))
