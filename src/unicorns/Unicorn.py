# -*- coding: utf-8 -*-

from .Location import Location
import json

from pydantic import BaseModel

class Unicorn(BaseModel):
    '''
    En enkel klass för att representera en enhörning
    '''
    
    id: int = 0
    name: str = ""
    description: str = ""
    reported_by: str = ""
    spotted_where: Location  =  Location()
    spotted_when: str | None = None
    image: str = ""
    
    def from_db(self, data: list) -> None:
        '''
        Populerar en enhörning med data från en databasförfrågan.
        '''
        
        self.id = data[0]
        self.name = data[1]
        self.description = data[2]
        self.reported_by = data[3]
        self.spotted_where.name = data[4]
        self.spotted_where.lat = data[5]
        self.spotted_where.lon = data[6]
        self.spotted_when = data[7]
        self.image = data[8]
    
    def to_dict(self, nested = False):
        '''
        Skapar en dictionary med värden från denna enhörning. Bra att använda
        när man matar in enhörningar i databaser.
        
        Med en liten fix kan vi göra den här lämplig även för JSON-representation.
        '''
        
        if nested:
            location = {
                'name': self.spotted_where.name,
                'lat': self.spotted_where.lat,
                'lon': self.spotted_where.lon
            }
            unicorn =  {
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'reportedBy': self.reported_by,
                'spottedWhere': location,
                'spottedWhen': self.spotted_when,
                'image': self.image
            }
        else:
            unicorn =  {
                    'id': self.id,
                    'name': self.name,
                    'description': self.description,
                    'reportedBy': self.reported_by,
                    'spottedWhereName': self.spotted_where.name,
                    'spottedWhereLat': self.spotted_where.lat,
                    'spottedWhereLon': self.spotted_where.lon,
                    'spottedWhen': self.spotted_when,
                    'image': self.image
                }
                
        return unicorn
