import routine
import hashlib
from wxserv import global_wx_serv

@routine.routine("/")
def index(signature, timestamp, nonce, echostr):
    list = [global_wx_serv.get_token(), timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    print("handle/GET func: hashcode, signature: ", hashcode, signature)
    if hashcode == signature:
        return echostr
    else:
        return "wrong signature"
