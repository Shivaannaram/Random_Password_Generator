import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="!@#$%&*?"
all=lower+upper+numbers+symbols
length=int(input("Enter the Length of the Password: "))
password="".join(random.sample(all,length))
print(password)