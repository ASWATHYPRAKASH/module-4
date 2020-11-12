D={1:"aswathy",2:"orange",3:"apple",4:"aswathy"}
temp = [] 
res = dict() 
for key, val in D.items(): 
    if val not in temp: 
        temp.append(val) 
        res[key] = val 
print(res)
