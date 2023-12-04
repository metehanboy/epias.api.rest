import importlib
from utils.authentication import Authenticatior


class epias:

    appName:str = "YepasWebService"
    debug:bool = True

    def __init__(self, **kwargs):
        
        if kwargs.get("username"):
            self.username = kwargs.get("username")
        if kwargs.get("password"):
            self.password = kwargs.get("password")

    def loadAuthenticator(self):
        authPacket:Authenticatior = importlib.import_module("utils.authentication")
        authPacket