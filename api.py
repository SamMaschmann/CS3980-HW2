from fastapi import FastAPI
import requests

apiurl = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
response = requests.get(apiurl)
response_dict = response.json()

for item in response_dict.get("data"):
    print(item.get("Year") + ": " + str(item.get("Population")))


app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return { "message": "Hello World"}