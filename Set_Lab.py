#SET_LAB

ahmed_set = {"Hail", "Riyadh", "Dubai"}
faris_set = {"Riyadh", "Jizan", "Abu Dhabi", "Hail"}

union_set = ahmed_set.union(faris_set)
intersection_set = ahmed_set.intersection(faris_set)
faris_set_difference = faris_set.difference(ahmed_set)

print("Cities that either Ahmed or Faris visited:")
for city in union_set:
    print(city, end=",")
print("\n------------")
print("Cities that both Ahmed and Faris visited:")
for city in intersection_set:
    print(city, end=",")
print("\n------------")
print("Cities that Faris visited but Ahmed did not")
for city in faris_set_difference:
    print(city, end=",")



