import re

sampleString = '''
Rohit made 122 runs, Virat made 96 runs, and
Dhawan made 46 runs and we won the match.
'''

# {"Rohit": 122, "Virat": 96, "Dhawan": 46}

lstNames = re.findall(r"[A-Z][]a-z]+", sampleString)
lstRuns = re.findall(r"\d{3}|\d{2}", sampleString)  #r"\d{2,3}"

print(lstNames)
print(lstRuns)

result = {}
for item in range(len(lstNames)):
    result[lstNames[item]] = lstRuns[item]

print(result)

result = {lstNames[item]: lstRuns[item] for item in range(len(lstRuns))}
print(result)

result = dict(zip(lstNames, lstRuns))
print(result)
print(type(result))
