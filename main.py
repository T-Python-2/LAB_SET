# LAB_SET

#Creat a set of visited cities for Ahmed. 
#Creat a set of visited cities for Faris.

ahmed_set = {"Hail", "Riyadh", "Dubai"} 
faris_set = {"Riyadh", "Jizan", "Abu Dhabi", "Hail"} 

#Using a loop , print all the cities they visited (union).
for cities in ahmed_set and faris_set:
 print(ahmed_set|faris_set)

#Using another loop, print the cities they visited both (intersection). 
print(ahmed_set&faris_set)

#Using a third loop, print the cities Faris visited, but Ahmed did not visit (difference).

print(faris_set.difference(ahmed_set))

