#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes 
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote 

#Using dependencies and modules
#import datetime
#now = datetime.datetime.now()
#print("The time right now is ", now)

#Can type this instead to avoid confusion
    #dt.datetime.now()

#CSV MODULE
#import csv
#dir(csv)
#this allows us to import the csv module 
#"dir" allows us to see all the functions within the imported csv module 

#Possible modes for reading or writing files:
    #r, w, x (open a file for exclusive creation, won't create one if not already created)
    #a (opens a file to append the data: if not created already, it will create the file and add the data)
    #+ opens a file for reading and writing 

#Assign a variable for the file to load and the path 
#file_to_load = "Resources/election_results_csv"
#election_data = open(file_to_load, 'r')

#Close the file
#election_data.close()

#EASIER TO USE WITH STATEMENT, BECAUSE OPENS AND CLOSES THE FILE AUTOMATICALLY 

#Open the election results and read the file 
#with open(file_to_load) as election_data:
    #print(election_data)

#OS Module important for connecting to operating system and connecting with files that may not have a direct path 
#os.path allows us to access files on different operating systems, like macOS and Windows 
#import csv
#import os
#Assign a variable for the file to load and the path 
#file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read the file 
#with open(file_to_laod) as election_data:
    #Print the file object
    #print(election_data)


#Create a filename variable to a direct or indirect path to the file 
#No such folder as "analysis", so we must create it now, then this code will run 
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#Using the open() function with the "w" mode we will write data to the file
#open(file_to_save, "w")
#Write data to the file 
#outfile = open(file_to_save, "w")
#outfile.write("Hello World")
#outfile.close()

#Easier to use "with" statement 
#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Counties in the election\n")
    #txt_file.write("---------------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")

import csv
import os 

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #for row in file_reader:
        #print(row[2]) - allows you to print all the data from a column 
    headers = next(file_reader)
    print(headers)













