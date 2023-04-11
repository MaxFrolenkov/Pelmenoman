from random import *

words = '1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./!@#$%^&*()"№;:?_+<>\|{}QWERTYUIOPASDFGHJKLZXCVBNM'

size = int(input('Какой длины вы хотите пароль?'))
parol = ''
for i in range(size):
    parol += choice(words)


print(parol)
