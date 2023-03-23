'''
Date: 2023-03-20 20:20:46
LastEditors: jhao
LastEditTime: 2023-03-23 20:33:32
FilePath: \python\main.py
'''
from typing import Optional
from fastapi import FastAPI

app=FastAPI()

fake_items_db=[{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}]

@app.get("/items/{skip}&{limit}")
async def read_item(skip:int=0,limit:int=10):
    return fake_items_db[skip:skip+limit]

