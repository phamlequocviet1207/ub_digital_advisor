with open ("pathwayslist2.txt") as file:
    line_list = []
    dict = {}
    for line in file:
        line = line.rstrip("\r\n")
        words = line.split(" ")
        for x in range(len(words)):
            dict[words[x]] 




