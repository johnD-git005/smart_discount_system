"""
Task 2: Smart Restaurant Discount System

You are helping a restaurant in Jos implement an automated discount system for their weekend promo.

The rules are:
1. Customers with a loyalty card get a 10% discount.
2. If the customer's order amount is above 20,000 NGN:
    - Loyalty card holders get an additional 5% discount.
    - Non-loyalty card holders get a free soft drink instead.
3. Students (verified with student ID) get an extra 5% discount on top of whatever they qualify for.

Customer data is stored in a dictionary like this:

customer = {
    "name": "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False
}

Write a nested if-else block that:
1. Calculates the final discount or freebie for the customer.
2. Stores the result in a dictionary called `order_summary`.
3. Prints out a summary for the cashier.
"""

customer = {
    "name": "Godiya",
    "order_amount": 0,
    "loyalty_card": False,
    "is_student": False
}

gift = None
discount = 0

if customer["loyalty_card"] == True:
	discount = customer["order_amount"] * 10 / 100
	
	if customer["order_amount"] > 20000:
		discount = customer["order_amount"] * 5 / 100
		
	if customer["loyalty_card"] == True and customer["order_amount"] > 20000 and customer["is_student"] == True:
		discount_for_loyalty_card = 10
		discount_for_order_amount = 5
		discount_for_is_student = 5
		total_for_all_discounts = 20
		discount = customer["order_amount"] * 20 / 100

if customer["loyalty_card"] == False:
	gift = "Free Drink"

if customer["is_student"] == True:
	discount = customer["order_amount"] * 5 / 100

total_discount = customer["order_amount"] - discount

order_summary = {
	"name": customer["name"],
	"order_amount": customer["order_amount"],
	"loyalty_card": customer["loyalty_card"],
	"is_student": customer["is_student"],
	"total_discount": total_discount,
	"gift": gift
	}
print(total_discount)
print(order_summary)
