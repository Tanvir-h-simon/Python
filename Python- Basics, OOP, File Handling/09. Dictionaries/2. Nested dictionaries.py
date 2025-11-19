# A dictionary can contain dictionaries, this is called nested dictionaries.
family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# family = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# Access items in nested dictionaries
print(family["child1"]["name"])
print(family["child1"]["year"])

print(family["child2"]["name"])
print(family["child2"]["year"])

print(family["child3"]["name"])
print(family["child3"]["year"])

print()

# Loop Through Nested Dictionaries
for x, obj in family.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])