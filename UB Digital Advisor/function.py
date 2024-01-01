from hack import class_dict
from hack import science_dict
from pathwaylib import globalDict
from pathwaylib import thematicDict

import GUI2

#print(class_dict["CSE"])


def classMustTake(year, semester):
    aList = []
    for department in class_dict.keys():
        for aClass in class_dict[department]:
            if ((class_dict[department][aClass]["WhenTakeYear"]) < year) or ((class_dict[department][aClass]["WhenTakeYear"]) == year and (class_dict[department][aClass]["WhenTakeSemester"]) <= semester):
                aList.append(aClass)
    
    return aList




def semesterMustTake(semester):
    aList = []
    for department in class_dict.keys():
        for aClass in class_dict[department]:
            if (class_dict[department][aClass]["WhenTakeSemester"]) <= semester:
                aList.append(aClass)
    return aList

#print(classMustTake(2,2))
#print(semesterMustTake(2))

def yearAndSemester(year, semester):
    aList=[]
    
    yearClass = classMustTake(year)
    semesterClass = semesterMustTake(semester)
    for aClass in yearClass:
        aList.append(aClass)
    for aClass in semesterClass:
        
        aList.append(aClass)
    
    return aList
    

    
#print(yearAndSemester(1,1))

#print(class_dict["MTH"]["MTH 141"]["WhenTakeYear"])

def pathwayAdder(year, semester):
    if len(yearAndSemester(year,semester)) < 4:
        print(str(yearAndSemester(year,semester)) + " you should probably take a pathway")

#print(pathwayAdder(1,1))

def pathwaySelector(input):
    pass

def wordtoword(aWord):
    letters = ""
    numbers = ""
    aWord = aWord.rstrip(" ")
    for letter in aWord:
        if letter.isalpha():
            letters += letter
            
        elif letter.isdigit():
            numbers += letter
    letters =letters.upper()
    result = letters + " " + numbers
    return result

def inputOfClasses():
    run = True
    aList = []
    while run == True:
        print("press E to exit")
        x = input("select class")
        x = wordtoword(x)
        #print(x)
        if x == "E ":
            return aList
        aList.append(x)

def scienceClass(aClass):
    for department in science_dict.keys():
        for class1 in science_dict[department].keys():
            if aClass == class1:
                return True
    return False

def globalClass(aClass):
    for pathwaylist in globalDict.keys():
        for department in globalDict[pathwaylist].keys():
            if aClass in globalDict[pathwaylist][department]:
                return True
    return False
def thematicClass(aClass):
    for pathwaylist in thematicDict.keys():
        for department in thematicDict[pathwaylist].keys():
            if aClass in thematicDict[pathwaylist][department]:
                    return True
    return False
#print(thematicClass("AAS 264"))   


year = GUI2.selected_year
semester = GUI2.selected_semester
list_of_classes = GUI2.user_classes_list
def listtolist(list):
    new_list = []
    for aCLass in list_of_classes:
        new_list.append(wordtoword(aCLass))
    return new_list
    
def whatYouNeed(year, semester):
    aList = []
    thematicCount = 0
    globalCount = 0
    science_count = 0
    

    compare = classMustTake(year, semester)
    result = (listtolist(list_of_classes))
    for aClass in compare:
        if aClass not in result:
            aList.append(aClass)
    for aClass in result:
            if scienceClass(aClass):
                science_count += 1
            elif thematicClass(aClass):
                thematicCount += 1
            elif globalClass(aClass):
                globalCount += 1
    globals_remaining = 3 - globalCount
    thematics_remaining = 3 - thematicCount
    aList.append("globals remaining {0}".format(globals_remaining)) 
    aList.append("thematics remaining {0}".format(thematics_remaining))      
    aList.append("sciences remaining {0}".format(2 - science_count))
    return aList

final = whatYouNeed(year,semester)




    
            

#print(scienceClass("GLY 101"))