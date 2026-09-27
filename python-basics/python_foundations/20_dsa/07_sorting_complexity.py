items = [5,1,4,2,8]
for i in range(len(items)):
    for j in range(0, len(items)-i-1):
        if items[j] > items[j+1]:
            items[j], items[j+1] = items[j+1], items[j]
print(items)
