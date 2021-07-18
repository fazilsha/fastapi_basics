from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"Hello":"Fast Api created by Fazil"}

@app.get("/fazil/{text}")
def say_text(text:str):
    data = text.split(" ")
    index = ["Name","Age","Country"]
    dict = {}
    if len(data) == len(index):
        for i,j in enumerate(index):
            dict[j] = data[i]
        return dict
    else:
        return {"Please provide exact three arguments with spaces":"/fazil/Name Age country"}