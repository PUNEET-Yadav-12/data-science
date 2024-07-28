# # find min and maximum
ls=[56,34,23,21,12,45,67,78,89,90,9,98,]
print(ls)
maximum=ls[0]
minimum=ls[0]
print(minimum)
for item in ls:
    if item< minimum:
        minimum = item
    if item>maximum:
        maximum=item
print('maximum value',maximum)
print("minimum value",minimum)
# # we have to print this
# 1
# 12
# 123
# 1234
# 12345

n=int(input("input the amount "))
for i in range(1,n+1):
    for j in range(1,i+1):
     print(j,end="")

    print()
    # we have to print 
    # *
    # **
    # ***
    # ****
n =int(input('enter the amount'))
for i in range(0,n):
   for j in range(0,i+1):
        print("$",end="")
   print()