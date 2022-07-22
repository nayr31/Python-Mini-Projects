# This file takes in a single user account and creates an importable file
# Not at all encrypted, use with caution

with open("passwords.csv", "w") as f:
    f.write("url,username,password\n")
    url = input("url: ")
    username = input("username: ")
    password = input("password: ")
    f.write(f"\"{url}\",\"{username}\",\"{password}\"")