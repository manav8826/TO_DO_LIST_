## put nd delete ---HTTP verbs 
## wroking with API --JSON



from flask import Flask,jsonify,request


app=Flask(__name__)

#intinial data in my  to do list 

items = [
    {'id': 1, 'name': 'item one', 'description': 'This is item one.'},
    {'id': 2, 'name': 'item two', 'description': 'This is item two.'}
]


@app.route('/')
def home():
    return " welcome to the TO DO List App "

## get: reterive all the items 

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

## get : retrive a sepcific item by ID

@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error" : "item not found"})
    return jsonify(item)

## POST  cretae a new task  --API KIND OF 

@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error" : "item not found"})
    new_item={
        "id": items[-1]["id"]+1 if items else 1,
        "name": request.json['name'],
        "description":request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)


## PUT : update and existing elemet

@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error" : "item not found"})
    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])
    return jsonify(item)

## delete : delete an item

@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_items(item_id):
    global items 
    items=[item for item in items if item["id"]==item_id]
    return jsonify({"result" : "item deleted"})
    



if __name__=='__main__':
    app.run(debug=True)
    