# -*- coding: utf-8 -*-

from fastapi import FastAPI
from unicorns import storage
from unicorns import Unicorn
from unicorns import Location

app = FastAPI()

@app.get("/setup")
async def setup():
    return storage.setup()


@app.get("/")
async def get_all_unicorns():
    return storage.fetch_unicorns()

@app.get("/{id}")
async def get_singular_unicorn(id):
    return storage.fetch_unicorn(id)

@app.post("/")
async def post_unicorn(unicorn : Unicorn):
    return storage.add_unicorn(unicorn)

@app.put("/{id}")
async def change_unicorn(unicorn : Unicorn):
    return storage.update_unicorn(unicorn)

@app.delete("/{id}")
async def delete_unicorn():
    return storage.delete_unicorn()


