ahmed_set = {"Hail", "Riyadh", "Dubai"}
faris_set = {"Riyadh", "Jizan", "Abu Dhabi", "Hail"}


#Union
for x in faris_set | ahmed_set :
    print(x,end= " ")
print()
    
#Intersection    
for x in faris_set & ahmed_set :
    print(x,end= " ")
print()
   
#Difference    
for x in faris_set - ahmed_set :
    print(x,end= " ")
    
    
    
    