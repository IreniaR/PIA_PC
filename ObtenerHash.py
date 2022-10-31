import hashlib
import os

file = input(r"Ruta del primer archivo:")
file2 = input(r"Ruta del segundo archivo:")

afile = open(file,file2,"rb")
bfile = afile.read()

Hash = hashlib.sha512(rfile)
print(Hash)
Hashed = Hash.hexdigest()

print(Hashed)


