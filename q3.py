
def fact(x,di):
    for i in range(x):
        di[i] = i*i
        
    return di

di={}
x = int(raw_input())
print fact(x, di)
