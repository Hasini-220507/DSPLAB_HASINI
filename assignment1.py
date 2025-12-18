#1st question
import datetime;
present=datetime.datetime.now();
print("current date and time:",present)


#2nd question
fname=input("enter ur first name:");
lname=input("enter ur last name");
for char in reversed(fname+" "+lname):
    print(char,end="");
print("\n")

##3rd question
number=int(input("enter a number:"))
print("n+nn+nnn:",(number+int(str(number)*2)+int(str(number)*3)));

##4th question
n1=int(input("enter 1st number:"));
n2=int(input("enter 2nd number:"));
n3=int(input("enter 3rd number:"));
if(n1==n2==n3):
    print(3*(n1+n2+n3));
else:
    print(n1+n2+n3);


##5th question
x=int(input("enter x:"));
y=int(input("enter y:"));
result=(x+y)**2;
print(result);

##6th question
p=int(input("enter amount:"));
r=float(input("enter interest:"));
n=int(input("enter time:"));
print("compound interest:",p*(1+r/100)**n);

##7th question
string=input("Enter a string:");
if('.' in string):
    result=float(string)
    print("the integer is",result);
    print(type(result));
else:
    result=int(string);
    print("the integer is",result);
    print(type(result));
    

##8th question
n=int(input("enter the value of n:"));
print(n*((n+1)/2));

##9th question
n=int(input("enter a number:"));
total=0;
while n!=0:
    rem=n%10;
    total+=rem;
    n=n//10;
print("sum of digits ofa number is:",total);


##10th question
character=input("enter a character:");
print("ASCII value of a character:",ord(character));

##11th question
number=input("enter a number or anything:");
if(number.isnumeric()):
    print("it is a number");
else:
    print("not a number");


##12th question
rows=int(input("enter number of rows:"));
colns=int(input("enter number of colns"));
for i in range(rows):
    for j in range(colns):
        print("*",end=" ");
    print();


##13th question
start=int(input("enter start number:"));
end=int(input("enter end number:"));
for i in range(start,end+1):
      if(i%7==0 and i%5!=0):
          print(i,end=" ")



##14th question
import math
c=50
h=30
d_values=input("enter the numbers separated by comma");
d_list=d_values.split(",")
result=[];
for d in d_list:
      r=math.sqrt(2*c*int(d)/h);
      result.append(str(round(r)));
      print(",".join(result));            



##15th question
s=64;
for i in range(5,0,-1):
    for j in range(i):
        s=s+1;
        print(chr(s),end=" ");
    print();






