import re
empDetails = "Hi I have a credit card with number 3775 123456 78910 and " \
             "other card is" \
             " 3545 456789 12345"

#http://www.getcreditcardnumbers.com
# AMEX Card
# Always start with 3
# Second digit is either 4 or 7
# <4 Digit> <6 Digit> <5 Digit>


lstCards = re.findall(r"3[4|7]\d{2}\s\d{6}\s\d{5}", empDetails)
print(lstCards)