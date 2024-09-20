import time

print("Please Insert YOUR CARD")

time.sleep(5)

password=1234

pin=int(input("Enter Your ATM PIN = "))

balance = 5000

if pin ==password:
    while True: 
        print("""
            1 == Balance
            
            2 == Withdraw Balance
            
            3 == Deposit Balance
            
            4 == EXIT
            
            """)
        try:
            option = int(input("Please Enter Your Choice =  "))
        except:
            print("Please Enter Valid Option")
            
        if option==1:
            print(f"YOUR CURRENT BALANCE IS {balance}")
            
            print("======================================================================")
            print("======================================================================")
            print("======================================================================")
        if option==2:
            withdraw_amount=int(input("Please Enter withdraw_amount=   "))
            balance = balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"Your Current Balance is {balance}")
            
            print("======================================================================")
            print("======================================================================")
            print("======================================================================")
        if option==3:
            deposit_amount = int(input("Please Enter deposit_amount =  "))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited to your account ") 
            print(f"Your Current Balance is {balance}")
            
            print("======================================================================")
            print("======================================================================")
            print("======================================================================")
            
        if option == 4:
            break
        print("======================================================================")

else:
    print("WRONG PIN PLEASE TRY AGAIN LATER")
