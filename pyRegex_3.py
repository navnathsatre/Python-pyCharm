import re
address = "Hi 11    89 Main, 4th Cross, 123 Road, Marathalli, 5678 Bangalore, 560023 67893"

lstValues = re.findall(r"\d+", address)
print("findall using '\d+'         : ", lstValues)

lstValues = re.findall(r"\d{6}", address)
print("findall using '\d{6}'       : ", lstValues)

lstValues = re.findall(r"\d{2}", address)
print("findall using '\d{2}'       : ", lstValues)

lstValues = re.findall(r"\d{1,6}", address)
print("findall using '\d{1,6}'     : ", lstValues)

lstValues = re.findall(r"\s(\d{2})\s", address)
print("findall using '\d{2}'       : ", lstValues)