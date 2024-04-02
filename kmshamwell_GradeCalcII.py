#
# Kyre M Shamwell
# Comp 163-001
# March 34th 2022
# In this Grade Calc II program I will be usings classes to find the avereage weight of the set catagories and print out the letter grade with the weight you recived in the specifc class.
#

# This variable calls for the users class name they will be in  
class_name = input("Enter class name: ")

# This while loop has a class inside that finds all the weights for the specific class catagory and make sure its equal too 100 and onces it equal to 100 it leaves the loop and goes to the next class
while True:
    class Weights:
        hwweight = int(input("Enter weight of the Homework catagory: "))
        qweight = int(input("Enter weight of the Quiz catagory: "))
        tweight = int(input("Enter weight of the Test catagory: "))
        paweight = int(input("Enter weight of the Projects/Assignments catagory: "))
        lweight = int(input("Enter weight of the Labs catagory: "))
        sumofweights = (hwweight+qweight+tweight+paweight+lweight)

    allWeights = Weights()
        
    if allWeights.sumofweights == 100:
        break
    else:
        print("Make sure weight is equal to 100")
# In this class I have the user input the averages for the specific catagories and then add them all up to find the average            
class Allocation:
    hw = float(input("Enter Homework average: "))
    quiz = float(input("Enter Quiz average: "))
    test = float(input("Enter Test average: "))
    proass = float(input("Enter Projects/Assignments average: "))
    labs = float(input("Enter Labs average: "))
    avg = (hw+quiz+test+proass+labs)
    
allAvg = Allocation()

# In this class is here to do all the math for the different catagories to find your weights total grade for you class
class TheMath:
    homeworkmath = (allAvg.hw*allWeights.hwweight)/100
    quizmath = (allAvg.quiz*allWeights.qweight)/100
    testmath = (allAvg.test*allWeights.tweight)/100
    proassmath = (allAvg.proass*allWeights.paweight)/100
    labsmath = (allAvg.labs*allWeights.lweight)/100

    sumMath = (homeworkmath+quizmath+testmath+proassmath+labsmath)

sumAllMath = TheMath()

# This class is to find the letter grade with an if else statment and will also tell you the weighted total of your class
class FinalAvg:
    if sumAllMath.sumMath >= 94:
        print("You have an A in", class_name, end=", Weighted total: ")
    elif sumAllMath.sumMath >=90:
        print("You have an A- in", class_name, end=", Weighted total: ")
    elif sumAllMath.sumMath >=87:
        print("You have an B+ in", class_name, end=", Weighted total: ")
    elif sumAllMath.sumMath >=84:
        print("You have an B in", class_name, end=", Weighted total: ")
    elif sumAllMath.sumMath >=80:
        print("You have an B- in", class_name, end=", Weighted total: ")
    elif sumAllMath.sumMath >=77:
        print("You have an C+ in", class_name, end=", Weighted total: ")
    elif sumAllMath.sumMath >=74:
        print("You have an C in", class_name, end=", Weighted total: ")
    elif sumAllMath.sumMath >=70:
        print("You have an C- in", class_name, end=", Weighted total: ")
    elif sumAllMath.sumMath >=67:
        print("You have an D+ in", class_name, end=", Weighted total: ")
    elif sumAllMath.sumMath >=64:
        print("You have an D in", class_name, end=", Weighted total: ")
    else:
        print("You have an F in", class_name, end=", Weighted total: ")
        
print('{:.2f}'.format(sumAllMath.sumMath)) # or # print('f{sumAllMath.sumMath:.2f}')

