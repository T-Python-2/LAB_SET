

ahmad_visited_city = {"Hail", "Riyadh", "Dubai"}
faris_visited_city = {"Riyadh", "Jizan", "Abu Dhabi", "Hail"}


for member in ahmad_visited_city.union(faris_visited_city):
    print(member)

print("#################################")

for member in ahmad_visited_city.intersection(faris_visited_city):
    print(member)

print("#################################")


for member in ahmad_visited_city.difference(faris_visited_city):
    print(member)