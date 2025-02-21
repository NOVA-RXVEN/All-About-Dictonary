country_code = {
    "India" : "+91",
    "USA" : "+1",
    "Bangladesh" : "+880"
}

print("Country code for India - ")
print(country_code.get("India", "Not Found"))

print("Country code for Japan - ")
print(country_code.get("Japan", "Not Found"))

print("Country code for Bangladesh - ")
print(country_code.get("Bangladesh", "Not Found"))