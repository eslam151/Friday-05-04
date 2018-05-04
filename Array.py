import random

def buildList(len_list):
    list = []
    for i in range(0,len_list):
        list.append(random.randint(0,100))
    return list

def findLargest(list):
    largestNumber = 0
    for i in range(0, len(list)):
        if list[i]> largestNumber:
            largestNumber = list[i]
    return largestNumber

def findLowest(list):
    lowestNumber = 10000000000000000000000
    for i in range(0, len(list)):
        if list[i]< lowestNumber:
            lowestNumber = list[i]
    return lowestNumber