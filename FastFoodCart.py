MENU = {
  "pizza": {
      "ingredients": {
          "dough": 1,
          "cheese": 1,
          "veggies": 1,
      },
      "cost": 120,
  },
  "burger": {
      "ingredients": {
          "bun": 1,
          "cheese": 1,
          "patty": 1,
      },
      "cost": 60,
  },
  "chicken": {
      "ingredients": {
          "chicken": 1,
          "spices": 1,
      },
      "cost": 150,
  },
  "fries": {
      "ingredients": {
          "potato": 2,
          "oil": 1,
      },
      "cost": 40,
  },
  "combo1": {
      "ingredients": {
          "dough": 1,
          "cheese": 1,
          "veggies": 1,
          "potato": 2,
          "oil": 1,
      },
      "cost": 150,
  },
  "combo2": {
      "ingredients": {
          "bun": 1,
          "cheese": 1,
          "patty": 1,
          "chicken": 1,
          "spices": 1,
      },
      "cost": 190,
  },
  "fried rice": {
      "ingredients": {
          "rice": 1,
          "veggies": 1,
          "spices": 1,
      },
      "cost": 100,
  },
  "fried noodles": {
      "ingredients": {
          "noodles": 1,
          "veggies": 1,
          "spices": 1,
      },
      "cost": 90,
  },
  "biriyani": {
      "ingredients": {
          "rice": 1,
          "chicken": 1,
          "spices": 1,
      },
      "cost": 130,
  }
}

resources = {
  "dough": 10,
  "cheese": 10,
  "veggies": 15,
  "bun": 10,
  "patty": 10,
  "chicken": 10,
  "spices": 15,
  "potato": 20,
  "oil": 10,
  "rice": 10,
  "noodles": 10,
}

profit = 0

def is_resource_sufficient(order_ingredients):
  for item in order_ingredients:
      if order_ingredients[item] > resources.get(item, 0):
          print(f"Sorry, there is not enough {item}.")
          return False
  return True

def process_payment(total_cost):
  print(f"Total to pay: ₹{total_cost}")
  print("Please insert Indian coins.")
  total = int(input("How many ₹10 coins?: ")) * 10
  total += int(input("How many ₹5 coins?: ")) * 5
  total += int(input("How many ₹2 coins?: ")) * 2
  total += int(input("How many ₹1 coins?: ")) * 1
  return total

def is_transaction_successful(money_received, cost):
  if money_received >= cost:
      change = money_received - cost
      print(f"Here is ₹{change} in change.")
      global profit
      profit += cost
      return True
  else:
      print("Sorry, that's not enough money. Money refunded.")
      return False

def make_food(item_name, ingredients, quantity):
  for item in ingredients:
      resources[item] -= ingredients[item] * quantity
  print(f"Here is your {quantity} x {item_name} 🍽️. Enjoy!")

def print_report():
  print("\n📦 Resource Report:")
  for item, amount in resources.items():
      print(f"{item.title()}: {amount}")
  print(f"💰 Money: ₹{profit}")

# Main loop
is_on = True
while is_on:
  print("\nMenu: pizza, burger, chicken, fries, combo1, combo2, fried rice, fried noodles, biriyani")
  choice = input("What would you like? Type item name or 'report' or 'off': ").lower()

  if choice == "off":
      is_on = False
  elif choice == "report":
      print_report()
  elif choice in MENU:
      try:
          quantity = int(input(f"How many {choice}s would you like?: "))
      except ValueError:
          print("Please enter a valid number.")
          continue

      selected = MENU[choice]
      required_ingredients = {item: selected["ingredients"][item] * quantity for item in selected["ingredients"]}
      total_cost = selected["cost"] * quantity

      if is_resource_sufficient(required_ingredients):
          payment = process_payment(total_cost)
          if is_transaction_successful(payment, total_cost):
              make_food(choice, selected["ingredients"], quantity)
  else:
      print("Invalid selection. Please choose a valid item.")
