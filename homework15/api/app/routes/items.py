from flask import request
from flask_api import status
from flask_api.exceptions import NotFound
from flask_login import current_user, login_required

from app import app, db
from app.models import Items

@app.route('/items/', methods=['GET', 'POST', 'PUT'])
@login_required
def all_items_handler():
    if request.method == 'GET':
        return [item.to_json() for item in current_user.items]
    else:
        user_input = request.get_json()
        items = Items(
            user_id=current_user.id,
            title=user_input['title'],
            amount=user_input['amount'],
            price=user_input['price'],
        )
        db.session.add()
        db.session.commit
        return items.to_json(), status.HTTP_201_CREATED

@app.route('/items/<int:item_id>/', methods=['GET','PUT', 'DELETE'])
@login_required
def single_item_request_handler(item_id):
    items: Items = Items.query.get(item_id)
    if items is None or items.user != current_user:
        raise NotFound ('Not found item request')
    if request.method == 'GET':
        response_data = items.to_json()
    elif request.method == 'PUT':
        user_input = request.get_json()
        items.title = user_input['title']
        items.amount = user_input['amount']
        items.price = user_input['price']
        items.is_show = user_input['is_show']
        db.session.commit()
        response_data = items.to_json()
    else:
        db.session.delete(items)
        db.session.commit()
        response_data = {'message': 'Delete successful'}
    return response_data