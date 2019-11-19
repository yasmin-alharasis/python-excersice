###################(1)#########################
print("Hello")
print("%9s" % 'Hello')
print("%13s" % 'Hello')



###################(2)#########################

print(("Orange Academy \n")*20)

###################(3)#########################
x=float(1)
y=float(2.8)
z=float("3")
w=float("4.2")
print(x,y,z,w,sep='10')
#output:1.0102.8103.0104.2
###################(4)#########################

num1=int(input("inter your first number"))
num2=int(input("inter your second number"))
print(num1*num2)

###################(5)#########################

a=int(input("enter num1" ))
b=int(input("enter num2" ))
c=int(input("enter num3" ))
d=int(input("enter num4" ))
e=int(input("enter num5" ))
sum=(a+b+c+d+e)
avg=int(sum/5)
print(avg)


###################(6)#########################

x=1
y=2.8
z=1j
o="Orange"
A=True
print(type(x))
print(type(y))
print(type(z))
print(type(o))
print(type(A))
"""
output:
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'str'>
<class 'bool'>
"""
###################(7)#########################

x,y="Orange",1
x1,y1=100,-10
print(x)
print(y)
print(x1)
print(y1)
"""
output:
Orange
1
100
-10
"""
###################(8)#########################

#correct
x5=10
print(x5)
X_q="'Orange"
print(X_q)
AB=14
print(AB)
print("10"*10)

###################(11)#########################

print("Hello,World!")
print("Cheers,Mate!")#This is the program
"""
output:
Hello,World!
Cheers,Mate!
"""

###################(12)#########################

name=input("enter your name")
age=int(input("enter your age"))
value=((100-age)+2019)

print("Hello" ,name, value,"Years to turn 100")

###################(13)#########################

base=int(input("enter base"))
height=int(input("enter height"))
area=(0.5*base*height)
print(area)

###################(14)#########################

x=11
y=3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(abs(x*-1))
print(int(x))
print(float(x))
print(divmod(x,y))
print(pow(x,y))
print(x**y)
print(x>y)
print(x==y)
print( x !=y )
"""
output:
14
8
33
3.6666666666666665
3
2
11
11
11.0
(3, 2)
1331
1331
True
False
True
"""














