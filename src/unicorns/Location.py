# -*- coding: utf-8 -*-

from pydantic import BaseModel

class Location(BaseModel):
    '''
    En enkel klass för att beskriva en plats
    '''
    name: str = ""
    lat: float = 0
    lon: float = 0