import re

print("Find all matches in the format Month day")

result = re.findall(r"[A-Z][a-z]+\s\d{1,2}", "These are the match dates June 24, August 9, Dec 12")
print(result)

result = re.findall(r"([A-Z][a-z]+)\s\d{1,2}", "These are the match dates June 24, August 32, Dec 12 and Nov")
print(result)

result = re.findall(r"[A-Z][a-z]+\s(\d{1,2})", "These are the match dates June 24, August 32, Dec 12 and Nov")
print(result)

result = re.findall(r"([A-Z][a-z]+)\s(\d{1,2})", "These are the match dates June 24, August 32, Dec 12 and Nov")
print(result)