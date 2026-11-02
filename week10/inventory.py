#1. The most surprising thing about Python lists was zero-indexing and negative indexing. I expected index 1 to be the first item so learning that list[0] is the first item and list[-1] gets the last item took a bit to adjust to but it makes grabbing specific data much simpler.

#2. A real business situation where a Python list would save time is managing inventory or order logs instead of manually updating an Excel sheet. Instead of manually editing rows using methods in Python automates, saving time and preventing formula errors

#------Exercise 1-----
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

#-----Exercise 2------

print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

#-----Exercise 3-----

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


#----Exersise 4-----

inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

#----Exercise 5------

coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("Tuples are useful for coordinates because they cannot be changed, so the latitude and longitude stay fixed together.")
print(coords)

#-----Exersise 6----

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

#------Exersise 7-----

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(prices)
print(discounted)

#-----Exercise 8-----

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))