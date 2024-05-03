import pickle

def append_binf(append,filen):
    try:
        pickle.dump(append, filen)
    except EOFError:
        filen.close
    