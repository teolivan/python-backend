# -*- coding: utf-8 -*-

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return {"hej": "då"}
