import string
import secrets
import random

l=int(input("Enter the length of password. \n"))
al=list(string.ascii_letters)
num=list(string.digits)
cha=['!','@','#','$','%','^','&','*','(',')','_','+']

ele=al+num+cha
pas=""

while len(pas)<l:
    pas+=secrets.choice(ele)


print("\nPassword:",pas)
