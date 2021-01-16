from flask import Flask, request, jsonify,render_template,redirect,url_for
import json
import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv:/")
db= cluster['Online_Store']
store = db['store']
cart = db['cart']


app = Flask(__name__)
def main():
    app.run(debug=True)


def get_item_details(prod_id):
    print("priont",prod_id)
    return store.find_one({"_id":prod_id})


def get_items():
    items=[item for item in store.find({})]
    return items

def get_items_from_cart():
    return [item for item in cart.find({})]    


def update_cart_in_db(prod_id,qty):
    if cart.find_one({"_id":prod_id})==None:
        item_details=get_item_details(prod_id)
        print(item_details)
        item_details["quantity"]=qty
        cart.insert_one(item_details)
        return 
    else:
        cart.update_one({"_id":prod_id},{"$inc":{"quantity":qty}})

# @app.route('/login')
# def login():


@app.route('/')
def index():
    items=get_items()
    cart=get_items_from_cart()
    return render_template('test.html',items=items,cart=cart)


@app.route('/update',methods=['POST'])
def update_cart():
    prod_id = int(request.form.get("prod_id"))
    qty = int(request.form.get("quantity"))
    update_cart_in_db(prod_id,qty)
    return redirect(url_for('.index'))

@app.route('/update_quantity',methods=['POST'])
def update_quantity():
    if request.form.get("update") == 'delete_item':
        prod_id = int(request.form.get("prod_id"))
        cart.delete_one({"_id":prod_id})
        return redirect(url_for('.index'))
    elif request.form.get("update") == 'updated_cart':
        prod_id = int(request.form.get("prod_id"))
        qty = int(request.form.get("cart_qty"))
        print("cameee ",prod_id,qty)
        cart.update_one({"_id":prod_id},{"$set":{"quantity":qty}})
        return redirect(url_for('.index'))


@app.route('/empty_cart')
def empty_cart():
    cart.delete_many({})
    return redirect(url_for('.index'))        

if __name__ == '__main__':
    main()
