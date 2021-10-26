import json
from flask import Flask, request, Response

app = Flask(__name__)

def get_data():
    with open('storage11.json', 'r') as f:
        return json.load(f)

def store_data(data):
    with open('storage11.json','w') as f:
        return json.dump(data, f)

@app.route('/items/', methods = ['GET'])
def get_items():
    return Response(
        json.dumps(get_data()),
        mimetype = 'application/json'
    )

@app.route('/items/', methods = ['POST'])
def create_item():
    data = get_data()

    latest_id = max([inv['id'] for inv in data], default=0) + 1
    data.append({
        "id": latest_id,
        "title": request.get_json()["title"],
        "amount": request.get_json()["amount"]
    })
    store_data(data)
    return Response(
        json.dumps({
            "item_id": latest_id}),
        mimetype='application/json'
    )

@app.route('/items/int:item_id/', methods=['GET'])
def get_single_item(item_id):
    data = get_data()
    for i in range(len(data)):
        if data[i]["id"] == item_id:
            return Response(
                json.dumps(data[i]),
                mimetype='application/json',
                )
    return Response ("Not found item", status=404)

@app.route('/items/<int:item_id>/', methods=['PUT'])
def update_item(item_id):
    data = get_data()
    for i in range(len(data)):
        if data[i]["id"] == item_id:
            data[i]["title"] = request.get_json()["title"]
            data[i]["amount"] = request.get_json()["amount"]
            store_data(data)
            break
    else:
        return Response("Not found item", status=404)

    return Response(status=200)

@app.route('/items/<int:item_id>/', methods=['DELETE'])
def delete_item(item_id):
    data = get_data()
    for i in range(len(data)):
        if data[i]["id"] == item_id:
            del data[i]
            store_data(data)
            return Response(status=204)

    return Response("Not found item", status=404)



