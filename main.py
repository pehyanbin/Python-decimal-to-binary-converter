while True:
  print("Assign the boolean values for your variables here. \n\nType 1 for True and 0 for False.\n\n")

  a = int(input("A : "))
  if a == 1:
    a = True
  elif a == 0:
    a = False
  else:
    print("Only type 1 or 0 in the input. Please try again. ")
    continue

  b = int(input("B : "))
  if b == 1:
    b = True
  elif b == 0:
    b = False
  else:
    print("Only type 1 or 0 in the input. Please try again. \n\n")
    continue

  print("Select your operation : \n\n1. AND\n2. OR\n3. NOT\n4. XOR")
  operation = int(input())

  print("\nOutput : ")

  if operation == 1:
    print(a and b)
  elif operation == 2:
    print(a or b)
  elif operation == 3:
    print("Not A : ", not a)
    print("Not B : ", not b)
  elif operation == 4:
    print(a ^ b)
  else:
    print("Out of range. Please try again. ")
    continue;

  print("\n\nDo you want to continue ? ")
  choice = int(input("Type any key to continue and 0 to exit. "))

  if choice == 0:
    break 
  else:
    print("\n\n======================================================\n")