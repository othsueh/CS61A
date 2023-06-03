 
# def cond():
#     return False
# def if_function(con,tr,fl):
#     if con:
#         return tr
#     else:
#         return fl
# def true_func():
#     print(42)
# def false_func():
#     print(47)
# if_function(cond(), true_func(), false_func())
def hailstone(x):
    count = 1
    print(x)
    while(x!=1):
        if(x%2==0):
            x/=2
        else:
            x = x*3 + 1
        print(int(x))
        count+=1
    return count
print(hailstone(27))
        