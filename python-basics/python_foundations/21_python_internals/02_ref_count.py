import sys
obj = []
print(sys.getrefcount(obj))
alias = obj
print(sys.getrefcount(obj))
