H = int(input())

def F(x):
    if x==1:
        return 1
    else:
        return 1+2*F(x//2)

print(F(H))
                    
            
        