new_dict = {
    "Eau" : 1,
    "De" : 1,
    "Parfum" : 1,
    "or" : 2,
    "EDP" : 1,
}

print(f"The original dictoniary: {new_dict}")

x = 1
res = 0

for key in new_dict:
    if new_dict[key] == x:
        res = res + 1
        
print(f"Frequency of x is: {res}")