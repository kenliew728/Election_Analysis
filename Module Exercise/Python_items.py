counties_dict = {"Arapahoe": 422289, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    #print(county,"county has", voters, "registered voters")
    #print(county + " county has " + str(voters) + " registered voters")
    print(f"{county} county has {voters:,} registered voters.") #adding :,after string will add comma separator



    

