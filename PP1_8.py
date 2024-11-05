
def q1():
  bool1 = True
  bool2 = False
  print(bool1 and bool2)
  print(bool1 or bool2)
def q2():
  inp = input("Enter an integer: ")
  inp = int(inp)
  print(inp != 0)

def q3():
  num = flaot(input("Enter a number: "))
  print(num <= 10 and num >= 0)
def q4():
  food = input("Input food: ")
  drink = input("Input drink: ")
  print(not food == "pizza" or not drink == "drink")

def q5():
  num = input("Enter an integer: ")
  num = int(num)
  tof = num % 2 == 0
  print(f"The integer {num} is {tof}.")

#Do not edit code after this
#Comment out the following code when running tests
'''
#q1()
#q2()
#q3()
#q4()
#q5()
'''
