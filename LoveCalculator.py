print("----Welcome to Love Calculator----")
print("\n")
person1 = input("Enter your name: ")
person2 = input("Enter your crush's name: ")

together = person1 + person2
together_lower = together.lower()
print("\n")

T = together_lower.count("t")
R = together_lower.count("r")
U = together_lower.count("u")
E = together_lower.count("e")

first = T + R + U + E

L = together_lower.count("l")
O = together_lower.count("o")
V = together_lower.count("v")
E = together_lower.count("e")

second = L + O + V + E

result = str(first) + str(second)
# print("Your Love Percentage is", result, "%")

if "ARITT" in person1.upper() and "RIKHITHA" in person2.upper():
  print("Your Love Percentage is Infinite, you are her true lover !!")
else:
  print("Your Love Percentage is", result, "%")