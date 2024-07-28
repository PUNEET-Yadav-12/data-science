#............ indentation matters  here..........
# ..
name =input ("plz enter your name:")
print("hello ",name)
message ="""
How may i help you!
Please select any of these option
Type 1>>>> CHECK BALANCE
Type 2>>>> DEPOSIT
Type 3>>>> WITHDRAWL
"""
print(message)
task=int(input("plz enter your option:"))
if task>=1 and task<=3:
    print("welcome you in virtual bank program")
    available_amount = 5000
    if task==1:
    # check balance program
        print("your available amount is: ",available_amount,"INR")
       #......this pass is used if we do not want to make a body here

    elif task==2:
    # deposit amount
        deposit_amount=int(input("plz enter deposit amount:"))
        if deposit_amount>0:    
            available_amount+=deposit_amount
            print("you have successfully deposit amount of :",deposit_amount,"in your bank account")
            print("your new avialble amount is:",available_amount)
        else:
            print("plz enter valid amount!")
    else:
    #withdrawl amount
        # print("please enter the amount you want to withdraw: ")
        withdrawl_amount=int(input("plz enter the withdrawl amount:"))
        if withdrawl_amount<=available_amount:
            available_amount-=withdrawl_amount
            print("you have successfully withdrawed ",withdrawl_amount,"INR")
            print("new available amount is: ",available_amount,"INR") 
           
        else:
            print("you have not sufficient value")
            print("your available amount is ",available_amount,"INR")
else:   
    print("plz input  option in between 1 to 3")

# ..................................................................
    # ####.................HOMEWORK===write the program withot any help atleat 3 times........
    # ........................................................................................
