#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unicorns import storage
from unicorns.Unicorn import Unicorn


storage.setup()

unicorns = storage.fetchUnicorns()
for unicorn in unicorns:
    print str(unicorn.id) + ': ' + unicorn.name
print

unicorn = storage.fetchUnicorn(3)
print(str(unicorn.id) + ': ' + unicorn.name)
print("reportedBy: " + unicorn.reportedBy)
print()

unicorn.reportedBy = 'Batman'
storage.updateUnicorn(unicorn)
unicorn = storage.fetchUnicorn(3)
print(str(unicorn.id) + ': ' + unicorn.name)
print("reportedBy: " + unicorn.reportedBy)
print()

unicorn = Unicorn()
unicorn.name = 'Konstig enhörning'
unicorn.description = 'Det här är ingen vacker enhörning'
unicorn.reportedBy = 'Johan'
unicorn.spottedWhere.name = 'Niagara'
unicorn.spottedWhere.lat = 55.609183
unicorn.spottedWhere.lon = 12.994875
unicorn.spottedWhen = '2015-09-22 20:14:00'
unicorn.image = 'https://pbs.twimg.com/profile_images/512349801929650177/_hfDmaho.jpeg'
storage.addUnicorn(unicorn)
unicorn = storage.fetchUnicorn(5)
print(str(unicorn.id) + ': ' + unicorn.name)
print()

unicorns = storage.fetchUnicorns()
print("Antal enhörningar: " + str(len(unicorns)))
storage.deleteUnicorn(5)
unicorns = storage.fetchUnicorns()
print("Antal enhörningar: " + str(len(unicorns)))
