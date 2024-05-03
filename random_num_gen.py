from append_binf import append_binf
from view_binf import view_binf
from random_num_gen_mod import random_num_gen
import time
i=True

while i==True:
    print("Generating a random number in bin file...")
    time.sleep(1)
    
    file=open("rand.bin", "ab")

    append_binf(random_num_gen(), file)
    print("Generated.")

    view=input(print("Do you want to view the file?"))

    if view=="yes":
        file=open("rand.bin", "rb")
        print(view_binf(file))
    else:
        exit()

    rep=input(print("Do you want to exit?"))

    if rep=="yes":
        exit()
