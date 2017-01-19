import requests
import json

class WxServ(object):

    def __init__(self):
        self.__token = "ro9er_weixin_token"
        self.__key = "Wo8e8HAbkD5aXh7B9Dd45p29pBV4x89eKI81YVmg2Ba"
        self.__appId = "wx4c7f5b9e6ae924b2"
        self.__secret = "c6e8082daa0feb702763f41dfd55385d"

    def get_token(self):
        return self.__token

    def get_access_token(self):
        req_str = "https://api.weixin.qq.com/cgi-bin/token"
        param = {"grant_type": "client_credential",
                 "appid": self.__appId,
                 "secret": self.__secret}
        result = requests.get(req_str, param)
        res_json = result.json()
        if "access_token" in res_json:
            self.__token = res_json["access_token"]
            print(self.__token)
        else:
            print("error get token")

global_wx_serv = WxServ()

if __name__ == "__main__":
    serv = WxServ()
    serv.get_token()