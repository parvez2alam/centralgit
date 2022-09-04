#1. program to check if the number is prime or not.
n=int(input("enter any number:"))
if n<=1:
    print("not a prime number..")
else:
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
    if is_prime==True:
        print("It is a prime number!!!")
    else:
        print("it is not a prime number:")
###################################################################

#2.take the input list from user and revers the list:
inputs=int(input("enter the number of elements in the list:"))
elements=list()

for i in range(inputs):
    numbers=int(input("enter {} element:".format(i+1)))
    elements.append(numbers)
print(elements)
N=len(elements)
for i in range(N//2):
    temp=elements[i]
    elements[i]=elements[N-i-1]
    elements[N-1-i]=temp
    
print(elements)

###################################################################

#3. reverse a string:
string=input("any string to reverse:")
rvstr=" "
for x in string:
    rvstr=x+rvstr
print(rvstr)

###################################################################

#4. Palindrom
test_input=input("any input to check if it is palindrom or not:")
rv_test_input=""
for x in test_input:
    rv_test_input=x+rv_test_input
if rv_test_input==test_input:
    print("its  a palindrom..")
else:
    print("its not palindrom")

###################################################################
