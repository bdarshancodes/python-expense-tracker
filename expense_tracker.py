#A simple console-based expense tracking app using Python
while True:
    print("Welcome\n")

    name=input("Hello, plese enter your beautiful name\n")
    print("Here is your menu: 1.ADD 2. View, 3. Total, 4. Exit\n" )
    menu=int(input("choose option from menu\n"))

    if menu==1:
        reason=input("please enter reason for expense!\n")
        amount=float(input("enter the amount of expense\n"))
        with open("reason.txt","a") as f:
            f.write(f"{reason}:{amount}\n")
    elif menu==2:
        with open("reason.txt","r") as f:
            for line in f:
                print("→", line.strip())
                
    elif menu==3:
        total=0
        with open("reason.txt","r") as f:
            for line in f:
                try:
                    reason,amount=line.strip().split(":")
                    total +=float(amount)
                except  ValueError:
                    print("skipping bad line",line.strip())
        print(f"total expense:{total}")

    elif menu==4:
        print("thanks for  visiting welcome again....Good bye!\n")
        break
    else:
        print("Please select right option!\n")

