from flask import *





app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    return jsonify({"print":"TESTE DE API GET"})


@app.route("/teste")
def index():
    return jsonify({"print":"FUNCIONANDO!!"})



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