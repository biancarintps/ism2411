# 1) The first bug was the missing colon on the for loop. I found it from the error message, because Python flags it before anything runs. This tells me I’m good at reading error messages but need more practice tracing logic bugs with print().
# 2)It returns the price after taking off 15%, 10%, or 5%, or the same price if the tier isn’t one of those. Yes, a colleague could use it without reading the body.
#3) I used ai to ask a quetion on why my code wasn't working. It helped my a lot because it helped me understand what I did wrong by explaining it to me. This helped me build my understanding. 




#----Exercise 1----
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")



#----Exercise 2----
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

price = 200
print(f"gold:   ${apply_discount(price, 'gold'):.2f}")
print(f"silver: ${apply_discount(price, 'silver'):.2f}")
print(f"bronze: ${apply_discount(price, 'bronze'):.2f}")
print(f"none:   ${apply_discount(price, 'none'):.2f}")

#----Exercise 3----

def calculate_tax(price, rate):
    return price * rate

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    return discounted + calculate_tax(discounted, tax_rate)

discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${discounted + calculate_tax(discounted, 0.07):.2f}")
print(f"final_price(200, \"gold\", 0.07) = ${final_price(200, 'gold', 0.07):.2f}")


#----Exercise 4----

def calculate_tax(price, rate):
    return price * rate

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    return discounted + calculate_tax(discounted, tax_rate)

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


#----Exercise 5----
# broken_sales.py - fixed
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    # Bug: total = sale overwrites the total each time, so it only keeps the last sale.
    # Fix: use += so each sale is added to the running total.
    total += sale
print(f"Total: ${total}")

count = 0
# Bug: the for statement is missing a colon, which causes a SyntaxError.
# Fix: add : at the end of the line.
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
# Bug: i <= len(sales) lets i reach 5, but the last valid index is 4, which causes an IndexError.
# Fix: use < so the loop stops at the last valid index.
while i < len(sales):
    print(sales[i])
    i += 1


#----Exercise 6----

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

# Scope is where a variable can be used. A variable made inside a function is local so it's separate from a global variable with the same name. That's why x stays 100 outside the function


