a="Manish singh"

# MUltiline string
b='''Bhagwati instute of technology 
and science'''

#printing string
print(a,b)
print(a[1])

#traverse string using for loop
for x in a:
    print(x)
    
#length of string using len() function
print(len(a))
print(len(b))

# checking if Bhagwati in b
if("Bhagwati" in b):
    print("Yes")
else:
    print("No") 
    
#slicing string

print(b[2:7]) 

# slice form starting
print(a[:3])   

#slicing string from starting
print(a[3:])

#tells weather string end with or not 
c=a.endswith("chutiya")
print(c)


#tells occurence of c in string a 
print(a.count("s"))

#use to captal the string
print(a.capitalize())

#use to replace string
print(b.replace("Bhagwati","Bhutiya"))