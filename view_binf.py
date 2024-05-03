import pickle 
i=True
def view_binf(file):
    try:
        while i==True:
            outp=pickle.load(file)
    except EOFError:
        file.close
    return outp