lis=[]
num=int(input("enter no. of elements in the list"))
for i in range(0 , num):
    print("enter element ",i)
    ele=int(input())
    lis.append(ele)

print("your initial list looks like this")
print(lis)

def pal(n):
    if (str(n) == str(n)[::-1]):
        return n
    else:
        n=n+1
        return pal(n)

for i in range(0,num):
    lis[i]=pal(lis[i])

print("the palindromic list is now this")
print(lis)
