# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) # search()- Returns a Match object if there is a match anywhere in the string
if x:
    print("Match found!")
else:
    print("No match")
    
txt = "The rain in Spain" 
x = re.findall("Portugal", txt) # findall()- Returns a list containing all matches
print(x)    
    
txt = "The rain in Spain"
x = re.split("\s", txt) # split()- Returns a list where the string has been split at each match
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt) # sub()- Replaces one or many matches with a string
print(x)