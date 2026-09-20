nums = [10,20,30]
fruits = ["Mango","Banana","Orange"]

nums.append(40)
nums.insert(0,5)

print("nums",nums)
nums = [34,34,34,65,57,5,476,8,6,4,67,8,7,5,454,545,5,76]
nums.sort()
print(nums)
print(nums[0])

for v in nums:
    print(v)

count=0
while count< len(nums):
    print(nums[count])
    count+=1

print("touple")

point = (10,20)

print(point[0],point[1])

x,y = point 

point = (100,200)

print(x,y,type(point))

print("set")

a = {1,2,3,4,3} # set does not contain duplicate values 
# set is very efficient, set used kind of hashing algo
b ={3,4,5}
print(a | b)

print(a & b)

print(a-b)

print("dictionary")

user = {"id":1,"name":"Faith Infotech"}
pincodes = {"blr-1":560086,"blr-2":560096,"trv-1":695001}
pincodes["gtr-1"]=522001
pincodes["trv-1"]=695004

for k,v in pincodes.items():
    print(k,"-->",v)

try:
    v = pincodes["gtr-2"]
    print(v)
# except Exception as e:
#     print("key does not exist",e.args[0])
except KeyError:
    print("key does not exist")

square_map = {x: x * x for x in range(1,6)}
mods= {x % 3 for x in range(1,20)}
modlist = [x % 3 for x in range (1,20)]
print(square_map,type(square_map))
print(mods,type(mods))
print(modlist,type(modlist))
