import random
import os
import string

def repeatthis():
    password = ""
    passwordc = string.ascii_letters
    password = string.digits

    do = ''.join(random.choice(password+passwordc) for i in range(8))
    print(do)

    my_file = open("algorithm.txt","a+")
    my_file.write(do)
    my_file.write("\n")
    repeatthis()
    

repeatthis()