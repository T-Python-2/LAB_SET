from math import factorial

#Q1
AhmedSet = {"Hail", "Riyadh", "Dubai"}
#Q2
farisSet = {"Riyadh", "Jizan", "Abu Dhabi", "Hail"}

#Q3
travel = AhmedSet.union(farisSet)
for city in travel:
    print(city)
print("================================")
#Q4
visitedBoth = AhmedSet.intersection(farisSet)
for both in visitedBoth:
    print(both)

print("================================")
#Q5
farisVisited = farisSet.difference(AhmedSet)
for faris in farisVisited:
    print(faris)