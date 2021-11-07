from flask import *



app = Flask(__name__)


def draco_today():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://www.mir4draco.com/')
        value_draco = page.query_selector('//*[@id="app"]/div/div/main/div/div[3]/div[1]/div/div[1]/div/div/div/a/div[2]/span[1]').inner_text()
        # print("DRACO "+ value_draco)
        browser.close()

    json = {
        "value": value_draco,
        "color": "purple"
    }

    return json





@app.route("/")
def index():
    
    vl = draco_today()

    return vl







if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)



# from typing import Optional
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")

# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")

# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}