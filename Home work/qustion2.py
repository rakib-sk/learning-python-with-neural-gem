'''Create a program that asks a user for the name of a fruit, its price per unit (can be a decimal
like 10.50), and the quantity they bought (an integer). Calculate the total cost. Using a single
f-string, print a message that looks exactly like this:
You bought 5 Kgs of Mango at 80.50 per Kg, for a total cost of 402.50 Taka.'''

fruit_name = input("Enter a fruit name: ")
fruit_weight = int(input("Enter fruit weight: "))
fruit_price = float(input("Enter fruit price: "))
fruit_unit = float(input("Enter unit: "))
print(f"You bought {fruit_weight} of {fruit_name} at {fruit_unit} per kg, for a total cost of {fruit_price} TAKA")

