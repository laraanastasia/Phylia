import random

def password(length):
    all = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!%&/><+-()@"
    password = ""
    for i in range(length):
        password += random.choice(all)
    return password
