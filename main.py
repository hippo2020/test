'''
Date: 2023-03-20 20:20:46
LastEditors: jhao
LastEditTime: 2023-03-20 20:21:36
FilePath: \python\hello.py
'''
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

