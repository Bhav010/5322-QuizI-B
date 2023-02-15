"""
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
"""

import csv
import random

# open the file
with open("employee_data.csv", "r") as file1:
    read1 = csv.reader(file1)

    # create an empty dictionary
    empdict = {}

    # use a loop to iterate through the csv file
    choice_title = ["CSR"]
    choice_Dept = ["Marketing"]
    choice_Clearance = ["TS"]
    # read1[10] = "New Salary"
    # read1[11] = "Difference"
    for row in read1:
        if (
            row[3] in choice_Dept and row[4] in choice_title and row[9] in choice_Dept
        ):  # check if the employee fits the search criteria
            row[10] = row[5] + (row[5] * 0.10)  # New Salary
            row[11] = row[5] - row[10]  # Difference in old and new salary
            print(
                f"Employee Name: {row[1]+row[2]} Current Salary: {row[5]}"
            )  # print employees that fit the criteria

print("=========================================")
print()

empdict = {"Name": "New Salary"}
empdict["Name"] = "read1.First Name" + "read1.Last Name"
empdict["New Salary"] = "empfile.New Salary"
empdict["Salary_Difference"] = "empfile.Difference"

# iternate through the dictionary and print out the key and value as per image
for i, j in empdict.items():
    print(f"Employee name: {i} , New Salary: {j}")


print()
print("=========================================")
print()

# print out the total difference between the old salary and the new salary as per image.
Inc_sal = 0
for x in empdict:
    Inc_sal += x["Salary_Difference"]  # Calculate total increase in salary
    print(f"Total increase in salary: {Inc_sal}")
