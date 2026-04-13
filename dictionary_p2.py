martwal = [
    {
    "name": "Pikachu",
    "price": 3,
    "size": '7"',
    "description": "If you don't buy me, I will find you",
    },
    {
    "name": "Rock",
    "price": 5,
    "size": "Rock",
    "description": "Rock",
    },
    {
    "name": "Actual_Product_Trust",
    "price": 99999,
    "size": "N/A",
    "description": "pls speed I need this",
    }
]


print("Product options:  Pikachu, Rock, Actual_Product_Trust")

still_buying = 1
cart = []

while still_buying == 1:
    buying = input("What would you like to buy? ")
    for product in martwal:
       if buying == product['name']:
          print("You just purchased", buying)
          cart.append(buying)

    keep_shopping = input("Would you like to buy something else? ")
    if keep_shopping != "yes":
      still_buying = 0

print("imagine buying", *cart)
print("u just got scammed at martwal ez")