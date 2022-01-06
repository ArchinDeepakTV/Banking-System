class banking:

    def __init__(self):
        import os
        if os.path.isfile('banking.db') == False:
            from DBLogic import CreateTables
            CreateTables()

    def numbers_to_strings(self, choice):
        switcher = {
            1: self.__newAccount(),
            2: self.__balanceCheck(),
            3: self.__phoneUpdate(),
            4: self.__mailUpdate(),
            5: self.__transaction(),
        }

        return switcher.get(choice, "nothing")

    def services(self):
        choice = int(input('''Enter Desired Service : 
                           \n1. New Account
                           \n2. Check Balance
                           \n3. Update Phone Number
                           \n4. Update Mail ID
                           \n5. Transaction'''))
        self.numbers_to_strings(choice)

    def __newAccount(self):
        from DBLogic import essentialDetails
        essentialDetails()

    def __balanceCheck(self):
        from DBLogic import balanceChecking
        balanceChecking()

    def __phoneUpdate(self):
        from DBLogic import update_phoneNo
        update_phoneNo()

    def __mailUpdate(self):
        from DBLogic import update_mailID
        update_mailID()

    def __transaction(self):
        from DBLogic import update_Balance
        update_Balance()


def main():
    banks = banking()
    banks.services()

    exitChoice = input('Would you like to view more? Y / N : ')
    if exitChoice == 'y' or exitChoice == 'Y':
        main()
        del banks
    else:
        del banks
        import time
        print('Thank You For Using BANKING SYSTEM')
        time.sleep(2)


if __name__ == "__main__":
    main()
