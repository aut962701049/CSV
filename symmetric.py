from cryptography.fernet import Fernet
key=Fernet.generate_key()
f_obj=Fernet(key)
msg=b"Hello World"
encrypt_msg=f_obj.encrypt(msg)
print("encrypted Message",encrypt_msg)
decrypt_msg=f_obj.decrypt(encrypt_msg)
print("decrypted Message",decrypt_msg.decode())
