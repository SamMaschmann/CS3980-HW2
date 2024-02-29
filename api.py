from fastapi import FastAPI
from starlette.responses import FileResponse
import requests

apiurl = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
response = requests.get(apiurl)
response_dict = response.json()

for item in response_dict.get("data"):
    print(item.get("Year") + ": " + str(item.get("Population")))


app = FastAPI()

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.get("/style.css")
async def read_index():
    return FileResponse('style.css')