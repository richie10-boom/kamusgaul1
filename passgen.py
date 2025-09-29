import random

def gen_pass(n):
    character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(n):
        password += random.choice(character)
    
    return password

n = int(input('Masukkan panjang password: '))
print('HASIL GENERATE PASSWORD: ', gen_pass(n))