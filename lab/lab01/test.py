def double_Eight(n):
    count = 0
    while(count < 2 and n>0):
        if(n%10 == 8):
            count += 1
        n //= 10
        print(n)
    if(count < 2):
        return False
    else: 
        return True
print(double_Eight(88))