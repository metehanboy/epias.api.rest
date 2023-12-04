# -*- coding: utf-8 -*-
from pathlib import Path

class Authenticatior:

    def __init__(self,username,password):

        self.username = username
        self.password = password


        print(Path.cwd())