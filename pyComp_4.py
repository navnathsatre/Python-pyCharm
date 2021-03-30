websites = ["Amazon", "flipkart", "paytm"]

# Using List Comprehensions, generate the below list
# ['www.amazon.com', 'www.flipkart.com', 'www.paytm.com']

result = ["www." + item + ".com" for item in websites]
print(result)