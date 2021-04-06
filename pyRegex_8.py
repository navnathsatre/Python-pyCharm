import re

print("Find all matches in the format Month day")
s = "These are the match dates June 24, August 9, Dec 12"

result = re.finditer(r"([A-Z][a-z]+)\s(\d{1,2})", s)
print(result)

for item in result:
    print("Match found at index start: {}, End: {}".format(item.start(), item.end()))
    print("Element: ", s[item.start(): item.end()])
    print("Match found at group 0: {}".format(item.group(0)))
    print("Match found at group 1: {}".format(item.group(1)))
    print("Match found at group 2: {}".format(item.group(2)))
    print("--------------------------------------------")


