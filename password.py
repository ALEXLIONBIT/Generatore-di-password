import random
lunghezza = int(input("Quanto deve essere lunga la password? "))
caratteri = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
password = ""
for _ in range(lunghezza):
    password += random.choice(caratteri)

print("La tua password generata è:", password)