import hashlib
password=input("Введите пароль:")
hash_pass=hashlib.sha256(password.encode()).hexdigest()
print("Хэш пароля: ",hash_pass)