websites = ["amazon", "flipkart", "paytm"]
extensions = ("org", "com", "in")

# www.amazon.org
# www.amazon.com
# www.amazon.in
# ...

for web in websites:
    for ext in extensions:
        print("www." + web + "." + ext)