
Ahmed = {"Hail", "Riyadh", "Dubai"}
Faris = {"Riyadh", "Jizan", "Abu Dhabi", "Hail"}


#1

union_list1 = set()
union_list1.update(Ahmed)
for i in Faris:
    if i not in union_list1:
        union_list1.add(i)
print("\n the cities they visited:\n", union_list1)

#2

intersection_list1 = set()
for i in Faris:
    if i in Ahmed:
        intersection_list1.add(i)
print("\n the cities they visited both:\n", intersection_list1)


#3

difference_list = set()
difference_list.update(Faris)
for i in Ahmed:
    if i in difference_list:
        difference_list.remove(i)
print("\n the cities Faris visited, but Ahmed did not visit:\n", difference_list,"\n")



