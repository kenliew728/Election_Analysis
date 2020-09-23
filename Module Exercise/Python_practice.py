counties = ["Arapahoe", "Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso in not in the list of counties")
#Method 1 to print all counties
for county in counties:
    print(county)    
#Method 2 to print all counties
for i in range(len(counties)):
    print(counties[i])
    