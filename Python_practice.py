counties = ["Arapahoe", "Denver", "Jefferson"]
#Don't have to use print function on terminal, just type "counties[0]"

#Retrieves first item in list
print(counties[0])
#Retrieves last item in list
print(counties[-1])
#Gives us length of list
print(len(counties))
#Slicing lists

#Retrieves only first two items in list: up to 2nd but not including 2nd item
counties[0:2]
#Same as above, but don't need to include first item number. Will return everything up until 2nd item 
counties[:2]
#Retrieves everything starting from first item number listed, unlike above's rules
counties[1:]

#Add items to a list 
counties.append("El Paso")
#Allows you to add to a specific index number (still starting from 0)
counties.insert(2,"El Paso")

#Remove items from a list 
counties.remove("El Paso")
#Removes items from a specific index and returns what the list looks like after
counties.pop(2)

#Change an element in a list: i.e. Remove Arapahoe from first index and replace it with Beirut
counties[0] = Beirut

my_typle = ()
my_dictionary = {}

counties_dictionary["Arapahoe"] = 422829
counties_dictionary["Denver"] = 463353
counties_dictionary["Jefferson"] = 432438

counties_dictionary.items()
counties_dictionary.keys()
counties_dictionary.values()

#Get a specific value 
counties_dict.get("Denver")
#Or you can use this method
counties_dictionary["Arapahoe"]

#LIST OF DICTIONARIES
voting_data = []
voting_data.append({"county":"Arapahoe","registered_voters: 422829"})
voting_data.append({"county":"Denver","registered_voters: 463353"})
voting_data.append({"county":"Jefferson","registered_voters: 432438"})

#Using if statements
#Equal to represented by "=="
#Not equal to represented by "!="
if counties[1] == "Denver":
    print(counties[1])

#If-Else Statements and using input function
#Nested If-Else Statements must be lined up by If and Else 
temperature = int(input("What is the temperature outside"))
if temperature > 80:
    print("Turn on the AC.")
else:
    if temperature >70:
    print("Open the windows.")
    else:
        print("That's whack")
    
#If-Elif-Else Statements
score = int(input("What is your test score?"))

if score >90:
    print("Your grade is an A.")
elif score >80:
    print("Your grade is a B.")
elif score >70:
    print("Your grade is a C.")
elif score >60:
    print("Your score is a D.")
else:
    print("You fucking suck")

#MEMBERSHIP OPERATORS
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso and is not in the list of counties.")

#Using Logical Operators (And, Or, Not)
if "El Paso" in counties and "Arapahoe" in counties:
    print("El Paso and Arapahoe are in the list of counties")
else:
    print("El Paso and Arapahoe are not in the list of counties")

#Using Condition-controlled Loops and Count-controlled Loops
#Using While Loops
x = 0
while x <= 5:
    print(x)
    x = x +1

#Iterate through Lists and Tuples
#When we use county or any other word in its place, it's being declared as the first item in the list "counties"
for county in counties:
    print(county)

#Can also use the range function ot help iterate through a list; simplifies the for loop process
for i in range(len(counties)):
    print(counties[i])
    #This code structure similar to counties[1] (gets item in the list), uses index with i in range function

#Keys and values of dictionary
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
#These are doing the same thing, because the second one is using indexing and declared key values

for key, value in dictionary_name.items():
    print(key, value)
#OR
for county, voters in counties_dict.items():
    print(county, voters)

#ITERATE THROUGH LIST OF DICTIONARIES
voting_data = [{"county":"Arapahoe","registered_voters: 422829},
                {"county":"Denver","registered_voters": 463353},
                {"county":"Jefferson","registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

#Getting values from a list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
#Returns the value from each key: this means we get each county value and each registered voter value
#Arapahoe
#422829

#Retrieves each county in the list of dictionaries 
for county_dict in voting_data:
    print(county_dict["county"])

#USING F-STRINGS
my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("How many total votes were there in the election?"))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#USING F-STRINGS WITH DICTIONARIES 
counties_dict = {"Arapahoe": 369237, "Denver": 413329, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#MULTILINE F-STRINGS
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("How many total votes votes in the election?"))
message_to_candidate = (
        f"You received {candidate_votes:,} votes."
        f"The total number of votes in the election was {total_votes:,}."
        f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_canidate)

#FORMAT FLOATING-POINT DECIMALS
f'{value:{width}.{precision}}'
#Width specifies number of characters used to display the value 
#Precision indicates number of decimal places to format value (use .2f for two decimal places) (f is floating-point)
#Changed above f-string statements to use the formatting 















