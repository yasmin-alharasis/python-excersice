# =============================================================================
# Q1
# =============================================================================
print("Q1")
num1=int(input("enter num1"))
num2=int(input("enter num2"))
if(num1>num2):
    print("the greatest number is"+" "+str(num1))
else:
    print("the greatest number is"+" "+str(num2))
    
# =============================================================================
# Q2
# =============================================================================
print("Q2")
num=int(input("enter a number"))
for a in range(11):
    print(num,"x",a,"=",(num*a))
 
    
# =============================================================================
# Q3    
# =============================================================================
print("Q3")
for i in range(5):
    for j in range(0,i+1):
        print('*',end=' ')
    print('\r')   
for i in range(5,0,-1):
   for j in range(0,i-1):
        print('*',end=' ')
   print('\r')

# =============================================================================
# Q4
# =============================================================================
print("Q4")
letters = ["x","y","z","a","b","c"]
for i in letters:
    if i =="a":
        continue
    elif i=="c":
        break
    print(i)
"""
output:
x
y
z
b   
"""

# =============================================================================
# Q5   
# =============================================================================
print("Q5")
for x in range(12,25,3):
    print(x)
"""
output:
12
15
18
21
24

"""

# =============================================================================
# Q6    
# =============================================================================
print("Q6")
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
"""
output:
1
2
3
"""
# =============================================================================
# Q7    
# =============================================================================
print("Q7")
num=int(input("enter your number"))
sum=0
for n  in range(num):
    sum+=n
print(sum)

# =============================================================================
# Q8
# =============================================================================
print("Q8")
num=int(input("enter a number"))
if(num%2==0):
    print("the number is even") 
else:
    print("the number is odd")    
# =============================================================================
# Q9    
# =============================================================================
print("Q9")
for i in range(1,10):
    for j in range(10 - i):
        print (" " , end=" ")
    for j in range(1,i):
        print(j, end=" ")
    for i in range(i , 0 , -1):
        print(i , end=" ")
    print()
for i in range(8,0 , -1):
    for j in range(10 - i):
        print (" " , end=" ")
    for j in range(1,i):
        print(j, end=" ")
    for i in range(i , 0 , -1):
        print(i , end=" ")
    print()
   

# =============================================================================
# Q10    
# =============================================================================  
print("Q10")
while True:
    try:
        num=int(input("enter a an integer number")) 
        num=int(num)
        break
    except ValueError:
        print("No valid integer! Please try again ...") 
print("Great, you successfully entered an integer!")
# =============================================================================
# Q11
# =============================================================================
print("Q11")
try:
    a=3
    if a<4:
        b=a/(a-3)
    print("Value of b=",b)
except(ZeroDivisionError,NameError):
    print("\nError Occurred and Handled")
#output:Error Occurred and Handled   

   
   
   
   
   
   
   
   
   
   
   