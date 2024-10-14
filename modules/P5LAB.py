#Alana Allocca
#09/30/2024
#P5LAB
#Use of loops, functions and module imports

import random

#define disperseChange function
def disperseChange(change):
    
    #Convert the float value into an integer
    change = round(change * 100, 2)

    if change == 0:
        print("No Change Due")

    #Calculate the amount of each coin needed
    #integer division - //

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles * 5)

    num_pennies = change

    #Display coins owed

    if num_dollars > 0:
        print(num_dollars,  end=" ")
        if num_dollars == 1:
            print("Dollar")
        else:
            print("Dollars")
            
    if num_quarters > 0:
        print(num_quarters,  end=" ")
        if num_quarters == 1:
            print("Quarter")
        else:
            print("Quarters")

    if num_dimes > 0:
        print(num_dimes,  end=" ")
        if num_dimes == 1:
            print("Dime")
        else:
            print("Dimes")

    if num_nickles > 0:
        print(num_nickles,  end=" ")
        if num_nickles == 1:
            print("Nickel")
        else:
            print("Nickels")

    if num_pennies > 0:
        print(num_pennies,  end=" ")
        if num_pennies == 1:
            print("Penny")
        else:
            print("Pennies")

#create the main function
def main():
    #generate random float
     totalOwed = round(random.uniform(0.01, 100.00), 2)
     print(f"Total for purchase is ${totalOwed:.2f}")

     #prompt user to give amount paid
     amtpaid = int(input("Enter amount to pay: "))

     #calculate change owed
     changeOwed = amtpaid - totalOwed
     print(f"Change owed to customer: ${changeOwed:.2f}")

     #call the disperseChange function
     disperseChange(changeOwed)
    

#call the main function
if __name__ == "__main__":
    main()


