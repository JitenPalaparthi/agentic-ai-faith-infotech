p=.8
for y in [1,0]:
    prob=(p**y)*((1-p)**(1-y))
    print("actual y",y,"probability assigned to observed outcome",prob)
