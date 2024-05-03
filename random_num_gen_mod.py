import time 

def random_num_gen():
    seed = int(time.time() * 1000)
    r_num = (seed * 12432 + 98745) % (3**9)
    return r_num