def print1(n):
    if(n<0):
        return
    print("hello")
    print1(n/2)
    print1(n/2)
print1(6)