voting_data =[{"county":"Arapahoe","registered_voters": 42289},
                {"county":"Denver","registered_voters": 463353},
                {"county":"Jefferson","registered_voters": 432438}]
for dictionary in voting_data:
    #print(f"{county} county has {registered_voters:,} registered voters.") #adding :,after string will add comma separator
    #print(f"There are {registered_voters} voters in {county}.")
    #print(f"{county} and {registered_voters}")
    print(f"{dictionary['county']} county has {dictionary['registered_voters']} voters.")
    

  