age = 43
price = 90.05
name="Faith Infotech"
active=True
nothing=None

for value in [age,price,name,active,nothing]:
    print(value,type(value))

# dynamic typing 

age = "Fourty Three"

print(age,type(age))

a,b = 17,5

print(a+b,a-b,a*b,a/b)
print(a//b,a%b,a**b)

x = 12 

print(x>10 and x<20) # and or not // true and true --> true
print(x < 5 or x == 12) # false or true --> true
print( not x == 12) # not true --> false

a = [1,2]
b = a 
c = [1,2]

print(a == c)
print(a is c)
print(a is b)
print(2 in a)
b.append(10)
print("a",a,"b:",b)

b = [10,11,12] # reassign
print("a",a,"b:",b)
a = b.copy()

# conditional statements

score = 82 
if score >=90:
    if score >=85 and score <=88:
        grade ='A'
      
elif score >=75:
    grade='B'
else:
    grade = 'C'
print(grade,type(grade))


for i in range(1,6):
    print(i, i*i)

n = 5
while n>=0: # while n:
    print(n)
    n-=1

for n in range(1,11):
    if n%3==0:
        continue
    else:
        print(n)

t = (1,True,"hello World")
a,b,c = t
print(a,b,c)

for v in t:
    print(v,type(v))

# match case 

status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not found")
    case _:
        print("Some other case")

n = 1 

while True:
    if n ==100:
        break
    print(n)
    n+=1