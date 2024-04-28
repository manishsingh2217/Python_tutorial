# Arthematic operator
a=6
b=3
c=0
print(a+b)
print(a-b)
print(a*b)
print(a/b)   #division 2.0 will answer
print(a//b)  #floor division 2 will answer
print(a%b)
print(a**b)  #power operator


#random function random.randrange(initialRange,finalRange)
import random
print(random.randrange(1,6))


# logical operator
print(a<9 and b>2)  #(and operator)
print(a>10 or b>10) #or operator
print(not(c))  #not operator

# bitwise operator
print(a|b)
print(a^b)
print(a<<b)
print(a>>b)
print(-b)

# identity operator  it check if the class id is same
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

#Membership operator
name= 'Manish singh'

print("M" in name)
print('k' in name)
print("m" not in name)
