#creating a functione group_by_owners
def group_by_owners(dict):
    finalDict={}
    for key,values in dict.items():       #iterating on the dictionary items
        finalDict[values]=finalDict.get(values,[])+[key]    #creating a list of values of dictionary and appending it with keys
    print(finalDict)
    return finalDict
    
dict={'input.txt':'randy',
       'code.py':'stan',
        'output.txt':'randy'}
group_by_owners(dict)
