#Dictionaries

# Dictionaries are used to information in the form of key value pairs

band={
    "vocals":"Plant",
    "guitar":"Page"
}

band2=dict(vocals="plants", guitar="page")

print(band)
print(band2)

#Acessing items in the dictionaries
print(band.get("guitar"))

#List all keys

print(band.keys())

#list all values

print(band.values())


#Return the key , value pairs as tuples

print(band.items())

#Verify if a key exists in a dictionary

print("guitar" in band)

#Changing values in a dictionary

band["Vocals"]="Coverdale"

band.update({"bass" :"JPJ"})

print(band)

#Removing items from a dictionary

print(band.pop()) # This returns what has been removed from the dictionary

print(band)

band["drums"]="Bonham"

print(band.popitem()) # This removes the last key value pair from the dictionary

#Del or clear an item

del band["drums"]
print(band)

#Empty out a dictionary completely

band2.clear()
print(band2)

del band2

# Copying a dictionary
band2=band.copy()
band2["drums"]="Dave"
print(band2)

 


