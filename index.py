import routine
import hashlib
import functools
from wxserv import global_wx_serv

@routine.routine("/")
def index(signature, timestamp, nonce, echostr):
    list = [global_wx_serv.get_token(), timestamp, nonce]
    list.sort()
    str_hash = functools.reduce(lambda a,b: a + b, list, "")
    sha1 = hashlib.sha1()
    sha1.update(str_hash.encode("utf-8"))
    hashcode = sha1.hexdigest()
    print("handle/GET func: hashcode, signature: ", hashcode, signature)
    if hashcode == signature:
        print("ws index success")
        return echostr
    else:
        print("ws index fail")
        return "wrong signature"
