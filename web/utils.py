from django.core.signing import TimestampSigner ,BadSignature,SignatureExpired

def genrate_token (email) :
    signer=TimestampSigner()
    token=signer.sign(email)
    return token

def validate_token (token,max_age=3600):
    signer=TimestampSigner()
    try:
        email=signer.unsign(token,max_age=max_age)
        return email
    except BadSignature:
        return False
    except SignatureExpired:
        return False