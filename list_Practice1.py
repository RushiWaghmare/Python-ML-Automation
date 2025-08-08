batches = ["PPA","LB","Angular","Python"]

print(batches)
print(batches[-1])
print(batches[1:])
print(batches[1:])
print(batches[:3])

print("-------------------------------------")
# we can store heterogenious data 
data1=[11,"rushikesh",3.14]
data2=[12,"Waghmare",4.00]
print(data1)
print(data2)
#
print("--------------------------------------")
#we can combined both above list
combined=[data1,data2]
print(combined)
#[[11, 'rushikesh', 3.14], [12, 'Waghmare', 4.0]]
print("------------------")

#multiple methods for manipulation of list

print(batches)
print("here are some operations")
print("-----------------------------")
batches.append("mean")
print(batches)
print("-----------------------------")
batches.remove("mean")
print(batches)
print("-----------------------------")
batches.pop()
print(batches)
print("-----------------------------")
batches.pop(2)
print(batches)
print("-----------------------------")
del batches[1:]
print(batches)
print("-----------------------------")
batches.extend(["lb","Python","Angular","Mean"])
print(batches)
print("-----------------------------")
batches.sort()
print(batches)