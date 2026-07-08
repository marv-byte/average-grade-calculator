storage = {}
current = 1
while True:
    grade = 0
    try:
        print("\n\nCalculate your average grade")
        print("(Only works with number-based grades!)")
        amount = input("\nHow many subjects do you have? ").strip()
        if amount == "end":
            print("------Storage------")
            for key, value in storage.items():
                print(key," -> ", value)
            print("-------------------")    
            break
        elif amount == "0":
            print("\nYou need to have at least 1 subject!")
        else:
            amount = int(amount)
            for i in range(0,amount):
                grade += int(input("Add a grade "))
            average = grade/amount
            storage[f"run{current}"] = average
            current += 1
            print("\n-------------------------------")    
            print("Your average is: ",average)
            print("-------------------------------") 
    except:
        print("\nError")
