choice = int(input("which operation you want to perform: \n 1. add \n 2. subtract \n 3. multiply \n 4. division \n 5. exit \nEnter a number between 1 and 5:"))
answer = 0
while(choice != 5):
  if(choice > 5 or choice <= 0):
    print("Enter number between 1 and 5")
  else:
    n1 = int(input("Get the first number:"))
    n2 = int(input("Get the second number:"))
    if choice == 1:
      answer = n1 + n2
    elif choice == 2:
      answer = n1 - n2
    elif choice == 3:
      answer = n1 * n2
    elif choice == 4:
      answer = n1 / n2
    elif choice  == 5:
      exit()
    print (answer)

  choice = int(input("which operation you want to perform: \n 1. add \n 2. subtract \n 3. multiply \n 4. division \n 5. exit \nEnter a number between 1 and 5:"))
