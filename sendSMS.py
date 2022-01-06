def SMS(otp, phNo):
    import json
    import requests

    # mention url
    url = "https://www.fast2sms.com/dev/bulk"

    # otp = 1776
    # phNo = 8078193145

    # create a dictionary
    my_data = {
        # Your default Sender ID
        'sender_id': 'BANKING SYSTEM',

        # Put your message here!
        'message': 'Your OTP is : ' + str(otp) + '. DO NOT SHARE YOUR OTP with anyone. \nBanking System.',

        'language': 'english',
        'route': 'p',

        'numbers': phNo
    }

    # create a dictionary
    headers = {
        'authorization': 'XhnGJuBWMSLvyaVqEPZDlYIU4kNjb8s7x1crpfgFRO6A2iow39Zmpd17VJDPXfhB34SO5Awrj8IM2vL6',
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }

    # make a post request
    response = requests.request("POST",
                                url,
                                data=my_data,
                                headers=headers)

    # load json data from source
    returned_msg = json.loads(response.text)

    # print the send message
    print(returned_msg['message'])


SMS(2224, 8078193145)
