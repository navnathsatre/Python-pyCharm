websites = ["amazon", "flipkart", "snapdeal", "paytm"]
extensions = ["com", "org", "in"]

result = ["www." + web + "." + ext for web in websites for ext in extensions]
print(result)


