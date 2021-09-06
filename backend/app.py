from flask import *
import os




app = Flask(__name__)


@app.route("/api/teste", methods=["GET", "POST"])
def hello():
    return jsonify({"print":"TESTE DE API GET"})


@app.route("/")
def index():
    return jsonify({"print":"FUNCIONANDO!!"})



if __name__ == "__main__":
    port = os.environ.get("PORT",5000)
    app.run(host="0.0.0.0", port=5000, debug=True)



# from typing import Optional
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")

# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")

# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}