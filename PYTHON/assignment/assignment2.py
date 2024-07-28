#average finder function
lis=[23,45,56,67,78,9,89,90]
def total(ls):
    totalsum=0
    for item in lis:
        totalsum+=item
    return totalsum
print(total(lis))
def totalno(ls):
    count=0
    for item in lis:
        count+=1
    return count
print(totalno(lis))
print(total(lis)/totalno(lis))

#even finder function

lis=[0,23,45,56,67,78,9,89,90]
def even(ls):
    count=0
    for n in ls:
        if n%2==0 and n!=0:
            count+=1
    return count
print('even no')
print(even(lis))

# odd finder 

lis=[0,23,45,56,67,78,9,89,90]
def odd(ls):
    count=0
    for n in ls:
        if n%2!=0 and n!=0:
            count+=1
    return count
print('odd no')
print(odd(lis))
