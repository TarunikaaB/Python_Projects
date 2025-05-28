def add(a, b):
  return a + b
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  return a / b
operations = { "+": add, "-": subtract, "*": multiply, "/": divide,}
def calculator():
   should_accumulate = True
   num1 = float(input("What is the first number?:"))
   while should_accumulate:
      for symbol in operations:
         print(symbol)
      operation_symbol = input("Pick an operations:")
      num2 = float(input("What is the second number?:"))
      answer = operations[operation_symbol](num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")
      choice = input(f"Type 'Y' to continue calculating with {answer}, or Type 'N' to start a new calculation.")
      if choice == "Y":
         num1 = answer
      else:
         should_accumulate = False
         print("\n" * 20)
         calculator()
calculator()
