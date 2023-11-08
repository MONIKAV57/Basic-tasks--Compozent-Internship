def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
print("---BASIC CALCULATOR---")
print(" Operations Available:\n 1.Addition\n 2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")
sel=int(input ("Please Select a Operation"))
a=int(input("Enter the 1st Operand:\n"))
b=int(input("Enter the 2nd Operand:\n"))

if sel==1:
    print(a,"+",b,"=",add(a,b))
elif sel==2:
    print(a,"-",b,"=",sub(a,b))
elif sel==3:
    print(a,"*",b,"=",mul(a,b))
elif sel==4:
    print(a,"/",b,"=",div(a,b))
elif sel==5:
    print(a,"%",b,"=",mod(a,b))
else:
    print("Invalid input!")
    
