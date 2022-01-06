def CreateTables():
    # importing necessary function
    from LiteTable import create_tables

    # for creating a single table for the user
    create_tables()


def essentialDetails():
    # importing necessary function
    from LiteInsert import accInfo

    accNo = UniqueAccNumber()
    name = input('Enter Customer Name : ')
    mailID = input('Enter Customer Mail_ID : ')
    phoneNo = int(input('Enter Customer Phone Number : '))
    branchCode = 1
    cif = cifs(accNo)
    ifsc = 'SBI'+str(branchCode)
    fathersName = input("Enter Customer Father's Name : ")
    dob = input('Enter Customer Date of Birth : ')
    balance = 0.0
    accInfo(accNo, name, branchCode, cif, ifsc,
            mailID, phoneNo, dob, fathersName, balance)


def update_phoneNo():
    # importing necessary function
    from Random import random_id
    from Clearing import clear
    from LiteUpdate import update_phoneNumber
    from NewMailingSystem import mails
    from sendSMS import SMS
    from LiteSearchDB import readPhoneNumber

    clear()
    accNo = int(input('Enter Customer Account Number : '))
    newPhoneNo = int(input('Enter Customer New Phone Number : '))

    option1 = input(
        'Can you receive an otp on your old phone number? Y / N : ')
    if option1 == 'y' or option1 == 'Y':
        otp = int(random_id()*1000000)
        oldPhoneNumber = readPhoneNumber(accNo)

        SMS(otp, oldPhoneNumber)  # sending otp via SMS

        otpEntered = int(
            input('Enter OTP received in your old phone number : '))
        if otp == otpEntered:
            update_phoneNumber(accNo, newPhoneNo)
            print('Phone Number Updated.')

    else:
        option1 = input(
            'Can you receive an otp on your registered Mail ID? Y / N : ')
        if option1 == 'y' or option1 == 'Y':
            otp = int(random_id()*1000000)
            mails(accNo, otp)  # sending otp via mail
            otpEntered = int(input('Enter OTP received in your Mail ID : '))
            if otp == otpEntered:
                update_phoneNumber(accNo, newPhoneNo)
                print('Phone Number Updated.')
        else:
            print('Please Contact the Bank Branch for updating your details.')


def update_mailID():
    # importing necessary function
    from Clearing import clear
    from LiteUpdate import update_mailID
    from NewMailingSystem import mails
    from Random import random_id

    clear()
    accNo = int(input('Enter Customer Account Number : '))
    newMailID = input("Enter Customer's New Mail ID : ")
    confirmNewMailID = input("Confirm Customer's New Mail ID : ")
    if newMailID == confirmNewMailID:
        # we can send an OTP to mail to confirm the mail ID
        otp = int(random_id()*1000000)
        mails(accNo, otp)  # sending otp via mail
        otpEntered = int(input('Enter OTP received in your Mail ID : '))
        if otp == otpEntered:
            update_mailID(accNo, newMailID)
            print('Mail ID Updated.')
    else:
        print("Entered Mail ID's don't match. Please Try Again.")
        update_mailID()


def update_Balance():
    # importing necessary function
    from LiteUpdate import update_balance

    accNo = int(input('Enter Customer Account Number : '))
    newBalance = int(input('Enter Customer New Phone Number : '))
    update_balance(accNo, newBalance)


def balanceChecking():
    # importing necessary function
    from LiteSearchDB import readBalance

    accNo = int(input('Enter Customer Account Number : '))
    print('ACCOUNT BALANCE : ', readBalance(accNo))


def cifs(accNo):
    # importing necessary function
    from LiteSearchDB import readCIF
    from Random import random_id

    cif = int(random_id() * 100000)
    already_exists = readCIF(accNo, cif)
    if already_exists == -1:
        cifs()
    return cif


def UniqueAccNumber():
    # importing necessary function
    from LiteSearchDB import readAccNumber
    from Clearing import clear
    from Random import random_id

    accNo = int(random_id() * 100000)
    already_exists = readAccNumber(accNo)
    if already_exists == -1:
        UniqueAccNumber()
    clear()
    return accNo
