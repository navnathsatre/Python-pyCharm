import re
s = "Welcome to   Regex   Programming    using    Python"

print("Value of s: ", s)

lstValues = re.split(r"\s", s)
print("Regex split using '\s'       : ", lstValues)

lstValues = re.split(r"\s+", s)
print("Regex split using '\s+'      : ", lstValues)

lstValues = re.split(r"(\s+)", s)
print("Regex split using '(\s+)'    : ", lstValues)

lstValues = re.split(r"m+", s)
print("Regex split using 's+'       : ", lstValues)

lstValues = re.split(r"(m+)", s)
print("Regex split using '(s+)'     : ", lstValues)

lstValues = re.split(r"m+|s+", s)
print("Regex split using 'm+|s+'       : ", lstValues)

lstValues = re.split(r"(m+|s+)", s)
print("Regex split using '(m+|s+)'     : ", lstValues)

s = "Welcome to Regex Programming using Python"
lstValues = re.split(r"[a-f]", s)
print("Regex split using '[a-f]'       : ", lstValues)

lstValues = re.split(r"([a-f])", s)
print("Regex split using '([a-f])'     : ", lstValues)

lstValues = re.split(r"[a-f][l-n]", s)
print("Regex split using '[a-f][l-n]'  : ", lstValues)

lstValues = re.split(r"([a-f][l-n])", s)
print("Regex split using '([a-f][l-n])': ", lstValues)