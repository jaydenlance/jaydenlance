#write a program that gets user input and adds ksh. to her account if she is between 25-30 years


age= input("what is your age ? ")
gender = input("what gender are you :male/female")
account_balance = 0

if (int(age) > 25) and (int(age) < 30 ):
    account_balance = account_balance + 10,000
    print("confirmed you have recieved 10,000")
else:
    print("sorry no money for you")   

acc_bal = input("Enter your acc_bal")

if(int(acc_bal) > 100000 and int(acc_bal)) < 250000:
    acc_bal = acc_bal - 25000
    print("we have deducted ksh 2500")
elif int(acc_bal) > 500000 and int(acc_bal) < 25000:
    acc_bal = acc_bal - (0.3*acc_bal)
    print("we have deducted 30 percent")
elif int(acc_bal) > 1000000:
    acc_bal = acc_bal - 15000
    print("we have deducted ksh. 15000")
else :
    print("no deduction done")    



