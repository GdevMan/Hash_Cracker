import bcrypt

hash_to_crack = input("Enter hash: ").encode().strip()

with open("passwords.txt", "r") as f:
    passwords = [line.strip() for line in f if line.strip()]

for password in passwords:
    print("Trying:", password)
    if bcrypt.checkpw(password.encode(), hash_to_crack):
        print(f"Password found: {password}")
        break
else:
    print("Password not found in list.")
