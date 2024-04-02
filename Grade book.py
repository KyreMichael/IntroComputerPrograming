#
# Kyre M Shamwell
# Comp 163-005
# Dec 1 2021
# I will be helping the professor sort the grade average of every student, the grade average of every male and female, the grade average of the entire class, and the highest grade average in the class.
#

import csv
# This is the class calling for all the males in the grade book trying to find the male grade average
def male_gender(file):
    male_avg = []
    
    with open(file, 'r') as csvfile:
        grades_reader = csv.reader(csvfile, delimiter=',')
    # The for loop looking for every male in the grade book file and once its found them it does the math and adds them all into the list    
        for row in grades_reader:
            if row[1] == 'M':
                malesum = float(row[2])+float(row[3])+float(row[4])+float(row[5])+float(row[6])
                male_avg.append(round(malesum/5,2))
                
    male_avg = round(sum(male_avg)/len(male_avg),2)
    
    return(male_avg)
# This is the class calling for all the females in the grade book trying to fine the female grade average
def female_gender(file):
    female_avg = []
    
    with open(file, 'r') as csvfile:
        grades_reader = csv.reader(csvfile, delimiter=',')
    # The for loop looking for every female in the grade book file and once its found them it does the math and adds them all into the list     
        for row in grades_reader:
            if row[1] == 'F':
                femalesum = float(row[2])+float(row[3])+float(row[4])+float(row[5])+float(row[6])
                female_avg.append(round(femalesum/5,2))
                
    female_avg = round(sum(female_avg)/len(female_avg),2)
    
    return(female_avg)
# This is the class calling for all of the student average in the grade book file placeing every students average into a dictionary 
def student_avg(file):
    dict = {}
    with open(file, 'r') as csvfile:
        grades_reader = csv.reader(csvfile, delimiter=',')
        for row in grades_reader: 
            if row[6] != 'Grade 5':
                dict[row[0]] = round((float(row[2])+float(row[3])+float(row[4])+float(row[5])+float(row[6]))/5,2)
                
    for key, value in dict.items():
        print(f'{key}    {value}')
# This is the class calling for the class average once its done all the math it returns everything back into the dictionary        
def class_avg(file):
    dict = {}
    with open(file, 'r') as csvfile:
        grades_reader = csv.reader(csvfile, delimiter=',')
        
        for row in grades_reader: 
            if row[6] != 'Grade 5':
                dict[row[0]] = round((float(row[2])+float(row[3])+float(row[4])+float(row[5])+float(row[6]))/5,2)
    
    values = dict.values()
    return round(sum(values)/10,2)
# This is the class that gets all the keys from the dictionary to print for the final line of code
def getting_key(val):
    dict = {} 
    with open(file, 'r') as csvfile:
        grades_reader = csv.reader(csvfile, delimiter=',')
        for row in grades_reader: 
            if row[6] != 'Grade 5':
                dict[row[0]] = round((float(row[2])+float(row[3])+float(row[4])+float(row[5])+float(row[6]))/5,2)
    
    for key, value in dict.items():
        if val == value:
            return key
# This class is searching for the student with the highest average in the class by sorting through all of the values pullings the highest value out      
def highest_avg(file):
    dict = {}
    with open(file, 'r') as csvfile:
        grades_reader = csv.reader(csvfile, delimiter=',')
        for row in grades_reader: 
            if row[6] != 'Grade 5':
                dict[row[0]] = round((float(row[2])+float(row[3])+float(row[4])+float(row[5])+float(row[6]))/5,2)
    
    values = dict.values()
    return max(values)
# Final part of the code where you would enter the loctation of the csv file you have Grade Book saved in pulling out all the information from the classes and printing them out 
if __name__ == '__main__':
    file = input("Enter location of file: ")
    # /Users/kyreshamwell/Downloads/Grades.csv    # << This is what I used to copy and test code to make sure everything ran correctly 
    print(f'Name         Averages')
    student_avg(file)
    print('\n')
    print(f'Male         {male_gender(file)}')
    print(f'Female       {female_gender(file)}')
    print('\n')
    print(f'Class        {class_avg(file)}')
    print('\n')
    print(f'{getting_key(highest_avg(file))} was the highest with an average of {highest_avg(file)}')