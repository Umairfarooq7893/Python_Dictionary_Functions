### dictionaries are used to store data values in key:value pairs, means word:meaning
# They are unordered mutable(changeable) & don't alllow duplicate keys
resume = {
    "Name"     : "Umair",
    "Father"   : "Farooq Ah",
    "Mother"   : "Kulsuma",
    "Age"      : 24,
    "Wife"     : "not yet married",
    "Religion" : "Muslim",
    "Subject"  : "Python, Java, C++",
    "Cgpa"     : 9.9,
    "Marks"    : [99, 99.5, 99.6],
}
print(resume["Name"])
print(resume["Cgpa"])
print(resume["Subject"])

# keys cannot be repeated,or changed
resume["Name"] = "Mir Umair"    # values can be altered
resume["Surname"] =  "Mir"       # we can add some new key:value
print(resume)


### Null Dictionary
null_dict = {}
null_dict["name"] = "Umair"  # now , we can add key:value with time
null_dict["start_up"] = "Code With Mir"
null_dict["age"]  = 20
print(null_dict)


### nested Dictionary
# where one or more of the values are themselves dictionaries

M_sheet = {
    "name"  : "Sahira",
    "Father": "Farooq Ah",
    "marks" : {
        "phy"  :99,
        "che"  : 98,
        "maths": 100
    }
}
print(M_sheet)
print(M_sheet["marks"])
print(M_sheet["marks"]["che"])
print(M_sheet["marks"]["maths"])
print(M_sheet["marks"]["phy"])








