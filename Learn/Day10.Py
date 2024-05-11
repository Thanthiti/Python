def Pass(Num):
    Num = Num + 10
    return(Num)
    pass

def Cas(num):
    num  = num + 11
    return num
    pass

Dictionary ={"+":Pass , "-":Cas}

FNSs = Dictionary["+"]
print(FNSs(20))
print(Pass(int(input("Enter num : "))))