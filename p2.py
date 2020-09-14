"""
CALCULATE THE AVERAGE OF NUMBERS IN A GIVEN LIST
"""
n=int(input("enter the number of the elements"))
a=[]
for i in range(0,n):
    e=int(input(" enter the element in list "))
    a.append(e)
avg=sum(a)/n
print(" average of th list ",avg)


OUTPUT-
enter the number of the elements5
enter the element in list 56
enter the element in list 76
enter the element in list 87
enter the element in list 54
enter the element in list 78
average of th list  70.2
