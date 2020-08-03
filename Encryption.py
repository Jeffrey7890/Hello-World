import cryptography					## Importing dependencies for cryptography
from cryptography.fernet import Fernet


### Encrpt the files or strings and such :)
#======================================!!

class Encrypted():
	def __init__(self,file):
		f = open("key.txt","rb")
		self.this = f.read()
		self.file = file.encode()
		self.key = Fernet(self.this)


	def Encrypt_file(self):
		
		encrypteds = self.key.encrypt(self.file)
		return encrypteds





##Decrypting the string or files 
#=================================

class Decrypted():
	def __init__(self,encrypted_file):
		f = open("key.txt","rb")
		self.this = f.read()
		self.encrypted_file = encrypted_file
		self.key = Fernet(self.this)

	def Decrypt_file(self):

		decrypteds = self.key.decrypt(self.encrypted_file)
		decryptedss = decrypteds.decode()
		return decryptedss

