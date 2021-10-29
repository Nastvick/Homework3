from flask_api import exceptions
import json


def get_item_index_or_404(data, item_id):
    for i in range(len(data)):
        if data[i]["id"] == item_id:
            return i
    raise exceptions.NotFound("Not found item request")

def item_to_json(item):
    return {
        'id': item['id'],
        'title': item['title'],
        'amount': item['amount'],
        'price': item['price'],
    }

def get_user_input_json(data):
    return json.loads(data)