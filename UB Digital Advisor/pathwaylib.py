def pathwayDictMaker(input):
    with open(input) as file:
        dic = {}
        for line in file:
            line = line.rstrip("\n\r")
            key = line[:3]
            if key[2] == " ":
                key = key.rstrip(" ")
                value = line[:6]
            else:
                value = line[:7]
            if key not in dic:
                dic[key] = [value]
            else:
                dic[key].append(value)
        return dic
    
globalDict = {"globalpathwayslist1" :(pathwayDictMaker("globalpathwayslist1.txt")),
              "globalpathwayslist2": (pathwayDictMaker("globalpathwayslist2.txt")),
              "globalpathwayslist3": (pathwayDictMaker("globalpathwayslist3.txt"))}


'''
print(globalDict["globalpathwayslist1"])
print(globalDict["globalpathwayslist2"])
print(globalDict["globalpathwayslist3"])
'''
thematicDict = {"thematicpathwayslist1" :(pathwayDictMaker("thematicpathwayslist1.txt")),
              "thematicpathwayslist2": (pathwayDictMaker("thematicpathwayslist2.txt")),
              "thematicpathwayslist3": (pathwayDictMaker("thematicpathwayslist3.txt"))}

#print(thematicDict["thematicpathwayslist1"])