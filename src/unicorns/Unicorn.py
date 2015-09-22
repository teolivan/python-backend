# -*- coding: utf-8 -*-

from Location import Location
import json

class Unicorn:
    '''
    En enkel klass för att representera en enhörning
    '''
    
    id = 0
    name = ""
    description = ""
    reportedBy = ""
    spottedWhere =  Location()
    spottedWhen = 0
    image = ""

    def __init__(self):
        pass
    
    def fromDB(self, data):
        '''
        Populerar en enhörning med data från en databasförfrågan.
        '''
        
        self.id = data[0]
        self.name = data[1]
        self.description = data[2]
        self.reportedBy = data[3]
        self.spottedWhere.name = data[4]
        self.spottedWhere.lat = data[5]
        self.spottedWhere.lon = data[6]
        self.spottedWhen = data[7]
        self.image = data[8]
    
    def toDict(self):
        '''
        Skapar en dictionary med värden från denna enhörning. Bra att använda
        när man matar in enhörningar i databaser.
        '''
        
        return {
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'reportedBy': self.reportedBy,
                'spottedWhereName': self.spottedWhere.name,
                'spottedWhereLat': self.spottedWhere.lat,
                'spottedWhereLon': self.spottedWhere.lon,
                'spottedWhen': self.spottedWhen,
                'image': self.image
                }