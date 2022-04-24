'''
### Ahmed visited those cities {"Hail", "Riyadh", "Dubai"}  and Faris visited {"Riyadh", "Jizan", "Abu Dhabi", "Hail"} .
### Using Sets, do the following:
- Creat a set of visited cities for Ahmed. 
- Creat a set of visited cities for Faris.
- Using a loop , print all the cities they visited (union).
- Using another loop, print the cities they visited both (intersection). 
- Using a third loop, print the cities Faris visited, but Ahmed did not visit (difference).
'''
Ahmed_cities = {"Hail", "Riyadh", "Dubai"}
Faris_cities = {"Riyadh", "Jizan", "Abu Dhabi", "Hail"}

for visited_union in Ahmed_cities.union(Faris_cities):
    print(visited_union)

print("\n------------")
    
for visited_inter in Ahmed_cities.intersection(Faris_cities):
    print(visited_inter)

print("\n------------")
for visited_deff in Faris_cities.difference(Ahmed_cities):
    print(visited_deff)    