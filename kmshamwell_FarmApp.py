#
# Kyre M Shamwell
# Comp 163-001
# Sat April 9th 2022
# In my code I will be using classes and sub-classes to run my farm app. In my farm app you will select the numbers 1-8 that will give you the option to pick whatever animals in the farm and print out your animals you will end up taking home.
#

# In this class I have functions for every animal I have in my menu which will be used to print the male or female name for each animal and below is the comments for the  male and female for each animal what I will have on my farm
class FarmAnimals:  
    
    # Male Cow
    def setcowMale(self, cmale):
        self.cmale = cmale  
    def printcowMale(self):
        return(self.cmale)
    # Female Cow
    def setcowFemale(self, cfemale):
        self.cfemale = cfemale
    def printcowFemale(self):
        return(self.cfemale)
    # Age Adult cow
    def ageAdultCow(self, aCage):
        self.aCage = aCage
    def printageAdultCow(self):
        return self.aCage
    # Age Child cow
    def ageChildCow(self, cCage):
        self.cCage = cCage
    def printageChildCow(self):
        return self.cCage
    
    # Male Pig
    def setpigMale(self, pmale):
        self.pmale = pmale    
    def printpigMale(self):
        return(self.pmale)
    # Female Pig
    def setpigFemale(self, pfemale):
        self.pfemale = pfemale    
    def printpigFemale(self):
        return(self.pfemale)
    # Age Adult Pig
    def ageAdultPig(self, pAage):
        self.pAage = pAage
    def printageAdultPig(self):
        return self.pAage
    # Age Child Pig
    def ageChildPig(self, pCage):
        self.pCage = pCage
    def printageChildPig(self):
        return self.pCage
    
    # Male Llama
    def setllamaMale(self, lmale):
        self.lmale = lmale
    def printllamaMale(self):
        return(self.lmale)
    # Female Llama
    def setllamaFemale(self, lfemale):
        self.lfemale = lfemale
    def printllamaFemale(self):
        return(self.lfemale)
    # Age Adult Llama
    def ageAdultLlama(self, lAage):
        self.lAage = lAage
    def printageAdultLlama(self):
        return self.lAage
    # Age Child Llama
    def ageChildLlama(self, lCage):
        self.lCage = lCage
    def printageChildLlama(self):
        return self.lCage
    
    # Male Duck
    def setduckMale(self, dmale):
        self.dmale = dmale
    def printduckMale(self):
        return(self.dmale)
    # Female Duck
    def setduckFemale(self, dfemale):
        self.dfemale = dfemale
    def printduckFemale(self):
        return(self.dfemale)
    # Age Adult Ducks
    def ageAdultDucks(self, dAage):
        self.dAage = dAage
    def printageAdultDucks(self):
        return self.dAage
    # Age Child Ducks
    def ageChildDucks(self, dCage):
        self.dCage = dCage
    def printageChildDucks(self):
        return self.dCage
    
    # Male Goat
    def setgoatMale(self, gmale):
        self.gmale = gmale
    def printgoatMale(self):
        return(self.gmale)
    # Female Goat
    def setgoatFemale(self, gfemale):
        self.gfemale = gfemale
    def printgoatFemale(self):
        return(self.gfemale)
    # Age Adult Goat
    def ageAdultGoat(self, gAage):
        self.gAage = gAage
    def printageAdultGoat(self):
        return self.gAage
    # Age Child Goat
    def ageChildGoat(self, gCage):
        self.gCage = gCage
    def printageChildGoat(self):
        return self.gCage
    
    # Male Rabbit  
    def  setrabbitMale(self, rmale):
        self.rmale = rmale
    def printrabbitMale(self):
        return(self.rmale)
    # Female Rabbit
    def setrabbitFemale(self, rfemale):
        self.rfemale = rfemale
    def printrabbitFemale(self):
        return(self.rfemale)
    # Age Adult Rabbit
    def ageAdultRabbit(self, rAage):
        self.rAage = rAage
    def printageAdultRabbit(self):
        return self.rAage
    # Age Child Rabbit
    def ageChildRabbit(self, rCage):
        self.rCage = rCage
    def printageChildRabbit(self):
        return self.rCage
    
    # Male Sheep
    def setsheepMale(self, smale):
        self.smale = smale
    def printsheepMale(self):
        return(self.smale)
    # Female Sheep
    def setsheepFemale(self, sfemale):
        self.sfemale = sfemale
    def printsheepFemale(self):
        return(self.sfemale)
    # Age Adult Sheep
    def ageAdultSheep(self, sAage):
        self.sAage = sAage
    def printageAdultSheep(self):
        return self.sAage
    # Age Child Sheep
    def ageChildSheep(self, sCage):
        self.sCage = sCage
    def printageChildSheep(self):
        return self.sCage
    
    # Male Horse
    def sethorseMale(self, hmale):
        self.hmale = hmale
    def printhorseMale(self):
        return(self.hmale)
    # Female Horse
    def sethorseFemale(self, hfemale):
        self.hfemale = hfemale
    def printhorseFemale(self):
        return(self.hfemale)
    # Age Adult Horse
    def ageAdultHorse(self, hAage):
        self.hAage = hAage
    def printageAdultHorse(self):
        return self.hAage
    # Age Child Horse
    def ageChildHorse(self, hCage):
        self.hCage = hCage
    def printageChildHorse(self):
        return self.hCage

# In this sub-class I have the set names for each male and female name for each gender for all my animals in my farm.  
class YourAnimal(FarmAnimals):
    def __init__(self):
        # Cow
        self.setcowMale("Cows(Bulls)")
        self.setcowFemale("Cows(Heifers)")
        self.ageAdultCow("Adult")
        self.ageChildCow("Child")
        # Pig
        self.setpigMale("Pigs(Boars)")
        self.setpigFemale("Pigs(Sows)")
        self.ageAdultPig("Adult")
        self.ageChildPig("Child")
        
        # Llama
        self.setllamaMale("Llama(Alpacas)")
        self.setllamaFemale("Llama(Hembras)")
        self.ageAdultLlama("Adult")
        self.ageChildLlama("Child")
        
        # Duck
        self.setduckMale("Duck(Drakes)")
        self.setduckFemale("Duck(Hens)")
        self.ageAdultDucks("Adult")
        self.ageChildDucks("Child")
        
        # Goat
        self.setgoatMale("Goat(Billys)")
        self.setgoatFemale("Goat(Nannys)")
        self.ageAdultGoat("Adult")
        self.ageChildGoat("Child")
        
        # Rabbit
        self.setrabbitMale("Rabbit(Buck)")
        self.setrabbitFemale("Rabbit(Doe)")
        self.ageAdultRabbit("Adult")
        self.ageChildRabbit("Child")
        
        # Sheep
        self.setsheepMale("Sheep(Rams)")
        self.setsheepFemale("Sheep(Ewes)")
        self.ageAdultSheep("Adult")
        self.ageChildSheep("Child")
        
        # Horse
        self.sethorseMale("Horse(Stallion)")
        self.sethorseFemale("Horse(Mare)")
        self.ageAdultHorse("Adult")
        self.ageChildHorse("Child")

# This is my variable name for my sub-class which is pulling things from my main class
userAnimals = YourAnimal()

# I have a list for both the users animals they pick and the amount of the specific animal they want to take home with them 
animals = []
amounts = []
ages = []
# While loop for the menu
print("Welcome to my Farm App! ") 
selection = True
while selection:
    print("In my farm we have: ")
    print("1. Cows"+"\n"+"2. Pigs"+"\n"+"3. Llamas"+"\n"+"4. Ducks"+"\n"+"5. Goats"+"\n"+"6. Rabits"+"\n"+"7. Sheep"+"\n"+"8. Horses"+"\n"+"9. Quit"+"\n")
    
    pickAnimals = int(input("Select a number to pick your animal. "))
    
    # For my if elif else statements they are being used to ask specific questions for each animal you want to bring home so you are taking home the specific animal for you which will then be added back into the list seen above
    if pickAnimals == 1:
        # Cows 
        class TheCows:
            cowGenderQ = input("Do you want a (M)ale or (F)emale Cow?: ")
            cowAgeQ = input("Do you want an (A)dult or (C)hild Cow?: ")
            cowAmountQ = int(input("How many Cows do you want? "))
            amounts.append(cowAmountQ)
            if cowGenderQ.upper() == "M":
                animals.append(userAnimals.printcowMale())    
            elif cowGenderQ.upper() == "F":
                animals.append(userAnimals.printcowFemale())
            if cowAgeQ.upper() == "A":
                ages.append(userAnimals.printageAdultCow())
            elif cowAgeQ.upper() == "C":
                ages.append(userAnimals.printageChildCow())
                        
    elif pickAnimals == 2:
        # Pigs
        class ThePigs:
            pigGenderQ = input("Do you want a (M)ale or (F)emale Pig?: ")
            pigAgeQ = input("Do you want an (A)dult or (C)hild Pig?: ")
            pigAmountQ = int(input("How many Pigs do you want? "))   
            amounts.append(pigAmountQ)   
            if pigGenderQ.upper() == "M":
                animals.append(userAnimals.printpigMale())
            elif pigGenderQ.upper() == "F":
                animals.append(userAnimals.printpigFemale())
            if pigAgeQ.upper() == "A":
                ages.append(userAnimals.printageAdultPig())
            elif pigAgeQ.upper() == "C":
                ages.append(userAnimals.printageChildPig())
                

    elif pickAnimals == 3:
        # Llamas
        class TheLlamas:
            llamaGenderQ = input("Do you want a (M)ale or (F)emale Llama?: ")
            llamaAgeQ = input("Do you want an (A)dult or (C)hild Llama?: ")
            llamaAmountQ = int(input("How many Llamas do you want? "))
            amounts.append(llamaAmountQ)
            if llamaGenderQ.upper() == "M":
                animals.append(userAnimals.printllamaMale())
            elif llamaGenderQ.upper() == "F":
                animals.append(userAnimals.printllamaFemale())
            if llamaAgeQ.upper() == "A":
                ages.append(userAnimals.printageAdultLlama())
            elif llamaAgeQ.upper() == "C":
                ages.append(userAnimals.printageChildLlama()) 
    
    elif pickAnimals == 4:
        # Ducks
        class TheDucks:
            duckGenderQ = input("Do you want a (M)ale or (F)emale Duck?: ")
            duckAgeQ = input("Do you want an (A)dult or (C)hild Ducks?: ")
            duckAmountQ = int(input("How many Ducks do you want? "))
            amounts.append(duckAmountQ)
            if duckGenderQ.upper() == "M":
                animals.append(userAnimals.printduckMale())
            elif duckGenderQ.upper() == "F":
                animals.append(userAnimals.printduckFemale())
            if duckAgeQ.upper() == "A":
                ages.append(userAnimals.printageAdultDucks())
            elif duckAgeQ.upper() == "C":
                ages.append(userAnimals.printageChildDucks())     
    
    elif pickAnimals == 5:
        # Goat
        class TheGoats:
            goatGenderQ = input("Do you want a (M)ale or (F)emale Goat?: ")
            goatAgeQ = input("Do you want an (A)dult or (C)hild Goat?: ")
            goatAmountQ = int(input("How many Goat do you want? "))
            amounts.append(goatAmountQ)
            if goatGenderQ.upper() == "M":
                animals.append(userAnimals.printgoatMale())
            elif goatGenderQ.upper() == "F":
                animals.append(userAnimals.printgoatFemale())
            if goatAgeQ.upper() == "A":
                ages.append(userAnimals.printageAdultGoat())
            elif goatAgeQ.upper() == "C":
                ages.append(userAnimals.printageChildGoat())                   
    
    elif pickAnimals == 6:
        # Rabbit
        class TheRabbits:
            rabbitGenderQ = input("Do you want a (M)ale or (F)emale Rabbit?: ")
            rabbitAgeQ = input("Do you want an (A)dult or (C)hild Rabbit?: ")
            rabbitAmountQ = int(input("How many Rabbit do you want? "))
            amounts.append(rabbitAmountQ)
            if rabbitGenderQ.upper() == "M":
                animals.append(userAnimals.printrabbitMale())
            elif rabbitGenderQ.upper() == "F":
                animals.append(userAnimals.printrabbitFemale())
            if rabbitAgeQ.upper() == "A":
                ages.append(userAnimals.printageAdultRabbit())
            elif rabbitAgeQ.upper() == "C":
                ages.append(userAnimals.printageChildRabbit())            
    
    elif pickAnimals == 7:
        # Sheep
        class TheSheeps:
            sheepGenderQ = input("Do you want a (M)ale or (F)emale Sheep?: ")
            sheepAgeQ = input("Do you want an (A)dult or (C)hild Sheep?: ")
            sheepAmountQ = int(input("How many Sheep do you want? "))
            amounts.append(sheepAmountQ)
            if sheepGenderQ.upper() == "M":
                animals.append(userAnimals.printsheepMale())
            elif sheepGenderQ.upper() == "F":
                animals.append(userAnimals.printsheepFemale())
            if sheepAgeQ.upper() == "A":
                ages.append(userAnimals.printageAdultSheep())
            elif sheepAgeQ.upper() == "C":
                ages.append(userAnimals.printageChildSheep())            
    
    elif pickAnimals == 8:
        # Horse
        class TheHorse:
            horseGenderQ = input("Do you want a (M)ale or (F)emale Horse?: ")
            horseAgeQ = input("Do you want an (A)dult or (C)hild Horse?: ")
            horseAmountQ = int(input("How many Horse do you want? "))
            amounts.append(horseAmountQ)
            if horseGenderQ.upper() == "M":
                animals.append(userAnimals.printhorseMale())
            elif horseGenderQ.upper() == "F":
                animals.append(userAnimals.printhorseFemale())
            if horseAgeQ.upper() == "A":
                ages.append(userAnimals.printageAdultHorse())
            elif horseAgeQ.upper() == "C":
                ages.append(userAnimals.printageChildHorse())          
    
    # This is the last elif statement that will stop the loop printing out the animals you decided to take home 
    elif pickAnimals == 9:
        print("\n")
        break
    
    # This is here for when the user puts in the wrong number thats not on the menu, it will say "Number not on menu" and take you back to the menu.
    else:
        print("\n")        
        print("Number not on menu. ")
        print("\n")

# Here I used a for loop to add both my list into to which I later would print about specific the animals you picked from        
wholefarm = []
for animal, amount, age in zip(animals, amounts, ages):
    wholefarm.append(f'{animal}         {amount}             {age}')

# This is how the Menu will look when you exit the loop telling you what you are taking home
print("You are taking home:")
print("   Animal          Amount         Evolution")
# I used this loop to bring out every action together and print it in my list
for farm in wholefarm:
    print(farm)
