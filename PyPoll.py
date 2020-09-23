#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of voters each candidate won
#5. The winner of the election based on popular vote.

# Add our dependencies
import csv
import os

#Assign a variable for the file to load the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file
    #for row in file_reader:
        #print(row)



# Using the open() function with the "w" mode we will write data to the file
#open(file_to_save, "w")- method 1 with open and close

#Using the statement open the file as a text file.
#outfile = open(file_to_save, "w") - method 1

# Using the with statement open the file as text file
#with open(file_to_save, "w") as txt_file: #method 2

# Write some data to the file.
    #outfile.write("Hello World") - method 1
    #txt_file.write("Hello World, ")
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")
    #txt_file.write("Arapahoe, Denver, Jefferson\n")
    #txt_file.write("Counties in the Election\n")
    #txt_file.write("--------------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file
# outfile.close() - not needed with a "with open" statement



