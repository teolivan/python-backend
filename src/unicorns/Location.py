# -*- coding: utf-8 -*-

class Location:
    '''
    En enkel klass för att beskriva en plats
    '''
    
    def __init__(self):
        self.name: str = ""
        self.lat: float = 0
        self.lon: float = 0