#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import datetime
import random

fileObject = open("Bank Data.txt", "r")
data = fileObject.readlines()
datetime_object = datetime.datetime.now()

print("Do you want to make a transaction?")
transaction_answer = str(input())

#if transaction_answer != "yes" or transaction_answer != "no":
while transaction_answer != "yes" or transaction_answer != "no":
        
    
    if transaction_answer == "yes" or transaction_answer == "no":
        if transaction_answer == "yes":
            print("Would you like to make a deposit or a withdrawal?")
            transaction_type = str(input())
            while transaction_type != "deposit" or transaction_type != "withdrawal": 
                if transaction_type == "deposit":
                    print("Enter amount you want to deposit:")
                    deposit_amount = str(input())
                    while deposit_amount.isnumeric() == False:  
                        print("Please enter numerics only.")
                        deposit_amount = str(input())
                    if deposit_amount.isnumeric() == True:
                        old_amount = str(data[5].replace("R",""))
                        account_number = str(data[1])
                        account_holder = str(data[3])
                        transaction_number = str(random.randint(000000, 999999))
                        new_amount = float(old_amount) + float(deposit_amount)
                        fileObject = open("Bank Data.txt", "w")
                        data[5] = str("R" + "%.2f" % float(new_amount))
                        fileObject.writelines(data)
                        fileObject.close()
                        fileObject2 = open("Transaction Log.txt", "r")
                        
                        data2 = fileObject2.read()
                        fileObject2.seek(0)
                        fileObject2.close()
                        
                        fileObject2 = open("Transaction Log.txt", "a+")
                        if len(data2) > 0 :
                            fileObject2.write("\n" + "\n")
                        log_string = str("Transaction Type: " + str(transaction_type) + "\n" + "Transaction Number: " + str(transaction_number) + "\n" + "Account Number: " + str(account_number) + "Account Owner: " + str(account_holder) + "Date of Transaction: " + str(datetime_object) + "\n" + "Old Amount: R" + "%.2f" % float(old_amount) + "\n" + "Deposited Amount: R" + "%.2f" % float(deposit_amount) + "\n" + "New Amount: R" + "%.2f" % float(new_amount))
                        fileObject2.write(str(log_string))
                        fileObject2.close()
                        print("New balance is: R" + "%.2f" % float(new_amount))    
                        break
                    break

                elif transaction_type == "withdrawal":
                    print("Enter amount you want to withdraw:")
                    withdrawal_amount = str(input())
                    while withdrawal_amount.isnumeric() == False:
                        print("Please enter numerics.")
                        withdrawal_amount = str(input())
                        
                    if withdrawal_amount.isnumeric() == True:
                        old_amount = str(data[5].replace("R",""))
                        while float(withdrawal_amount) > float(old_amount):
                            print("Please enter sufficient funds, check balance.")
                            withdrawal_amount = str(input())

                        
                        account_number = str(data[1])
                        account_holder = str(data[3])
                        transaction_number = str(random.randint(000000, 999999))        
                        new_amount = float(old_amount) - float(withdrawal_amount)
                        fileObject = open("Bank Data.txt", "w")
                        data[5] = str("R" + "%.2f" % float(new_amount))
                        fileObject.writelines(data)
                        fileObject.close()
                        fileObject2 = open("Transaction Log.txt", "r")
                        
                        data2 = fileObject2.read()
                        fileObject2.seek(0)
                        fileObject2.close()
                        
                        fileObject2 = open("Transaction Log.txt", "a+")
                        if len(data2) > 0 :
                            fileObject2.write("\n" + "\n")
                        fileObject2 = open("Transaction Log.txt", "a+")
                        log_string = str("Transaction Type: " + str(transaction_type) + "\n" + "Transaction Number: " + str(transaction_number) + "\n" + "Account Number: " + str(account_number) + "Account Owner: " + str(account_holder) + "Date of Transaction: " + str(datetime_object) + "\n" + "Old Amount: R" + "%.2f" % float(old_amount) + "\n" + "Deposited Amount: R" + "%.2f" % float(withdrawal_amount) + "\n" + "New Amount: R" + "%.2f" % float(new_amount))
                        fileObject2.write(str(log_string))
                        fileObject2.close()
                        print("New balance is: R" + "%.2f" % float(new_amount))
                        break
                    break


                else:
                    print("Please choose a transaction type.")
                    transaction_type = str(input())
            break
        elif transaction_answer == "no":
            print("Current Balance: R" + "%.2f" % float(data[5].replace("R","")))
            break
       
    print("Please enter yes or no")
    transaction_answer = str(input())


# In[ ]:




