# In this version 0.0.01 dates and times will always be the date and 
# time the entry is added, not the transation, later the ability to 
# change this will be added (maybe).

import os
import csv
import datetime

if os.path.exists('./ledger.csv') == True:
    with open('ledger.csv', 'r') as f:
        reader = csv.reader(f)

else:
    with open('ledger.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',',
                                quotechar="|", quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['Date', 'Description', 'Amount', 'Current Balance'])
        csvwriter.writerow(["0000-00-00", "Initial Creation", "0", "0"])

with open('ledger.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        balance = (row[-1])
    print(f'''--==== Welcome to your terminal checkbook! ====--
    
Your current balance is {balance}.
        ''')

while True:
    print('''What would you like to do?

    1) View Current Balance
    2) Record a Debit (Withdraw)
    3) Record a Credit (Deposit)
    4) View Ledger
    5) Exit
    
    ''')

    choice = input("What is your Choice? ")
    while choice not in ["1", "2", "3", "4", "5"]:
        print(f"Invalid Choice: {choice}")
        choice = input ("what is your choice")

    if choice == "1":
        with open('ledger.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                balance = (row[-1])
        print(f'''
Your current balance is {balance}.
        ''')

    elif choice == "2":
        desc = input(f"Description of Transation: ")
        debit = input(f"How much is the Debit? ")
        while not debit.isdigit():
            debit = input("Error. Please input a valid Number: ")
        with open('ledger.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                balance = (row[-1])
        with open('ledger.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar="|", quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerow([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), desc , "-" + debit, int(balance) - int(debit)])

    elif choice == "3":
        desc = input(f"Description of Transation: ")
        credit = input(f"How much is the Credit? ")
        while not credit.isdigit():
            credit = input("Error. Please input a valid Number: ")
        with open('ledger.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                balance = (row[-1])
        with open('ledger.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar="|", quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerow([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), desc , credit, int(balance) + int(credit)])
    elif choice == "4":
            with open('ledger.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    print("")
                    print(row)
                    print("")

    elif choice == '5':
        break

