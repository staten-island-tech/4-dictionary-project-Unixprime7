martwal = [
    {
    "name": "Pikachu-stuffed toy/plushie",
    "price": 3,
    "size": '7"',
    "description": "If you don't buy me, I will find you",
    },
    {
    "name": "Rock/Large-Pebble/Tiny-Boulder",
    "price": 5,
    "size": "Rock",
    "description": "Rock",
    },
    {
    "name": "N/A",
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
    if buying == "Pikachu":
     print(martwal[0]["name"])
    elif buying == "Rock":
     print(martwal[1]["name"])
    elif buying == "Actual_Product_Trust":
     print(martwal[2]["name"])

    cart.append(buying)

    keep_shopping = input("Would you like to buy something else? ")
    if keep_shopping != "yes":
      still_buying = 0

print("imagine buying", *cart)
print("u just got scammed at martwal ez")