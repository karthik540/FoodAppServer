from twilio.rest import Client


client = Client('AC634981f305b221cfcb81004c328a2a36', 'fd2ebc6910246263f2cb63ad3626df4f')
verify = client.verify.services('VA33585eb9e37d5d986f0d422c89d824b4')


####    Phone Code Authentication...
def sendVerificationCode(phone_number):
    verify.verifications.create(to= phone_number, channel='sms')
    return {'flag' : True , 'message' : 'Verification Code Sent'}

####    Phone Code Verification...
def checkVerificationCode(verification_code , phone_number):
    result = verify.verification_checks.create(to= phone_number, code= verification_code)

    if result.status == "approved":
        return {'flag' : True , 'message' : 'Verification Code Sent'}
    return {'flag' : False , 'message' : 'Verification Code Failed'}
