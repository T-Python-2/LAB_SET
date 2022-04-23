#SET_LAB

ahmed_cities = {"Hail", "Riyadh", "Dubai"}
faris_cities = {"Riyadh", "Jizan", "Abu Dhabi", "Hail"}

    
for city in ahmed_cities.union(faris_cities):
    print(city)


for city in ahmed_cities.intersection(faris_cities):
    print("\n the cities they visited both: " + city)


for city in faris_cities.difference(ahmed_cities):
    print("\n the cities Faris visited, but Ahmed did not visit: " + city) 

 ####################### extra for more information #######################
 
for city in ahmed_cities.difference(faris_cities):
    print("\n the cities ahmed visited, but faris did not visit: " + city) 
