class Calculator:
  def add(self, a, b):
    return a + b

  def sub(self, a, b):
    return a - b

  def mul(self, a, b):
    return a * b

  def div(self, a, b):
    if b == 0:
      return "Error: divide by zero"
    return a / b


print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

opt = int(input("Choose: "))

if opt >= 1 and opt <= 4:
   num1 = float(input("First number: "))
   num2 = float(input("Second number: "))

   c = Calculator()

   if opt == 1:
      ans = c.add(num1, num2)
   elif opt == 2:
      ans = c.sub(num1, num2)
   elif opt == 3:
      ans = c.mul(num1, num2)
   elif opt == 4:
      ans = c.div(num1, num2)

   print("Result =", ans)
else:
   print("Invalid option")
