from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    },
    {
        "name": "PMGV Store",
        "items": [
            {
                "name": "PC",
                "price": 2515.99
            }
        ]
    }
]

@app.route("/store") # http://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores}

@app.route("/store", methods=['POST'])
def create_store():
    return {"stores": stores}