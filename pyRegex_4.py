import re

s = '''
<html>
<head>
<title>Current IP Address Allocations
</title>
</head>
<body>
IP Address are 172.45.78.109
LoopBack Address: 127.0.0.1
Computer 1: 10.67.89.101
Computer 2: 11.67.98.102
Computer 2: 12.68.98.102
</body>
</html>
'''
# IPAddress : 4 parts => number.
lstvalue = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", s)
print("IPadresses : ", lstvalue)

lstvalue = re.findall(r"10\.\d{1,3}\.\d{1,3}\.\d{1,3}", s)
print("IPadresses : ", lstvalue)

lstvalue = re.findall(r"1[0-2]\.\d{1,3}\.\d{1,3}\.\d{1,3}", s)
print("IPadresses : ", lstvalue)

