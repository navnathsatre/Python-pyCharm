# Rule 72 (finance)
# 1000 INR -> Stocks / Mutual Funds / FDs /
# 10% / 8% / 5%
class Inventment:
    def __init__(self, amount, roi, type):
        self.amount = amount
        self.roi = roi
        self.type = type

    def YearsToDouble(self):
        try:
            return 72 / self.roi
        except ZeroDivisionError:
            return "invalid interest rate"
        except ValueError:
            return "invalid interest rate"


i1 = Inventment(1000, 8, "Stock")
print("Years to double", i1.YearsToDouble())

i2 = Inventment(5000, 0, "Savings")
print("Years to double", i2.YearsToDouble())