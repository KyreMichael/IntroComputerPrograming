#
# Kyre M Shamwell
# Comp 163-001
# March 2 2022
# In this assignment I will be calculating the weight of each grading allocation and the amount of assignments with its grade and printing back the students final grade he/she recived in the class.
# 

# This is where I called for the users name
name = input("Enter your name:")
# This is where I called for the users class name
class_name = input("Enter class name:")

# In this while statment I called for the user to input the wieght for each catagory
while True:    
    hwweight = int(input("Enter weight of the Homework catagory: "))
    qweight = int(input("Enter weight of the Quiz catagory: "))
    tweight = int(input("Enter weight of the Test catagory: "))
    paweight = int(input("Enter weight of the Projects/Assignments catagory: "))
    lweight = int(input("Enter weight of the Labs catagory: "))
    sumofweights = (hwweight+qweight+tweight+paweight+lweight)
# To make sure the users weights all are equal to 100 I added all the weights together and use the if-else statement to check if the wiehgts all equal to 100        
    if sumofweights == 100:
        break
# Once they are equal to 100 the code will break and go on into the functions down below    
# If they do not qual 100 the loop will start over again until all weights are equal to 100    
    else:
        print("Error does not equal 100")

# In this function I will be calling for the users homework grade and saving its precent in the getHomework function
def getHomework():
    hw = int(input("How many homework assignmets did you have this semester? "))
    list1 = []
    # This for loop looks for all the grades in this catagory and adds it to the list
    for a in range(hw):
        list1.append(float(input("Enter grades for homework: ")))
    # Once its in the list all the numbers will be calculated and returned back into the function which will be used later    
        addhw = (sum(list1))
        divweight = hwweight/100
        divmulhw = (addhw/hw)*divweight
    return divmulhw

# In this function I will be calling for the users quiz grade and saving its precent in the getQuizes function
def getQuizes():
    quiz = int(input("How many quizes did you have this semester? "))
    list2 = []
    # This for loop looks for all the grades in this catagory and adds it to the list
    for b in range(quiz):
        list2.append(float(input("Enter grades for Quizes: ")))
    # Once its in the list all the numbers will be calculated and returned back into the function which will be used later   
        addquiz = (sum(list2))
        divquizweight = qweight/100
        divmulqu = (addquiz/quiz)*divquizweight
    return divmulqu

# In this function I will be calling for the users test grade and saving its precent in the getTest function
def getTest():
    test = int(input("How many tests did you have this semester? "))
    list3 = []
    # This for loop looks for all the grades in this catagory and adds it to the list
    for c in range(test):
        list3.append(float(input("Enter grades for Tests: ")))
    # Once its in the list all the numbers will be calculated and returned back into the function which will be used later    
        addtest = (sum(list3))
        divtestweight = tweight/100
        divmulte = (addtest/test)*divtestweight
    return divmulte

# In this function I will be calling for the users projects grade and saving its precent in the getProjects function
def getProjects():
    assignment = int(input("How many projects/assignments did you have this semester? "))
    list4 = []
    # This for loop looks for all the grades in this catagory and adds it to the list
    for d in range(assignment):
        list4.append(float(input("Enter grades for projects: ")))
    # Once its in the list all the numbers will be calculated and returned back into the function which will be used later    
        addproass = (sum(list4))
        divproassweight = paweight/100
        divmulproass = (addproass/assignment)*divproassweight
    return divmulproass

# In this function I will be calling for the users labs grade and saving its precent in the getLabs function
def getLabs():
    labs = int(input("How many lab did you have this semester? "))
    list5 = []
    # This for loop looks for all the grades in this catagory and adds it to the list
    for e in range(labs):
        list5.append(float(input("Enter grades for labs: ")))
    # Once its in the list all the numbers will be calculated and returned back into the function which will be used later    
        addlab = (sum(list5))
        divlabweight = lweight/100
        divmullab = (addlab/labs)*divlabweight
    return divmullab

# This is the final function I used to finsh and find the grade the user recived in the class
def findFinalGrade():
    sumfinalgrade = (getHomework()+getLabs()+getQuizes()+getProjects()+getTest())
    # Once I get the sum of all 5 catagories I used a if else statement to see if the grade was between an A and F
    if sumfinalgrade >= 94:
        print("In", class_name, name, "recived an A.", end=" ")
    elif sumfinalgrade >=90:
        print("In", class_name, name, "recived an A-.", end=" ")
    elif sumfinalgrade >=87:
        print("In", class_name, name, "recived an B+.", end=" ")
    elif sumfinalgrade >=84:
        print("In", class_name, name, "recived an B.", end=" ")
    elif sumfinalgrade >=80:
        print("In", class_name, name, "recived an B-.", end=" ")    
    elif sumfinalgrade >=77:
        print("In", class_name, name, "recived an C+.", end=" ")
    elif sumfinalgrade >=74:
        print("In", class_name, name, "recived an C.", end=" ")
    elif sumfinalgrade >=70:
        print("In", class_name, name, "recived an C-.", end=" ")
    elif sumfinalgrade >=67:
        print("In", class_name, name, "recived an D+.", end=" ")
    elif sumfinalgrade >=64:
        print("In", class_name, name, "recived an D.", end=" ")
    else:
        print("In", class_name, name, "recived an F.", end=" ")
    return sumfinalgrade

# Finally I print the final grade with the name and class with the letter grade 
print(f'{findFinalGrade():.2f}')
