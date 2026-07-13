### Dictionary

myDict =  { 
    "Name" : "Umair",
    "Father"   : "Farooq Ah",
    "Mother"   : "Kulsuma",
    "Age"      : 20,
    "Wife"     : "not yet married",
    "Religion" : "Muslim",
    "Subject"  : "Python, Java, C++",
    "Cgpa"     : 9.9,
    "Marks"    : [99, 99.5, 99.6],
    }
     
# myDict.keys()         #returns all key
print(myDict.keys()) 
print(list(myDict.keys()))
print(len(myDict))


# myDict.values()       #returns all values
print(myDict.values())
print(list(myDict.values()))
print(len(myDict))


# myDict.items()          #returns all (key,value) pairs as tuples
print(myDict.items())
#let's = asign this to some variable
items = list(myDict.items())
print(items)
print(items[0])
print(items[1])
print(items[2])


# myDict.get("key")         #returns the key according to value
print(myDict.get("Age"))
print(myDict["Age"])        # or we can also write it as 
#print(myDict["Age2"])      # error,iss ma, bez Dict ma aysa key:value nhi h
#print(myDict.get("Age2"))  # No error -> prints None,hence we use it


# myDict.update({"newItem"})  #insert the specified items to the dictionary
myDict.update({"city":"srinager","state":"J & K","Name":"Mir Umair"})
print(myDict)                 #If old key with some new value is typed, It doesnot
#create new ,key:value ,bez python not allows duplicate key's,but will be altered
#that key , Like Name = Mir Umair



