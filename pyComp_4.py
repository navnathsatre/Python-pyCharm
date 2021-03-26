websites = ['Amazon', 'Flipcart', 'PayTM']
result = []
for i in websites:
    result.append("www."+i+".com")
print(result)

# Using List Comprehensions, generate the below list
# ['www.amazon.com', 'www.flipkart.com', 'www.paytm.com']

result = ["www." + item + ".com" for item in websites]
print(result)