from flask import render_template, flash, redirect, url_for, request, jsonify, session
# from flaskShopApp import app, db
from flaskShopApp import app
# from flaskShopApp.forms import 
# from flaskShopApp.modles import 
# from flaskShopApp.utils import * 


@app.route("/")
def index():
    return redirect(url_for("products"))


@app.route("/products/")
def products():
    return render_template("products.html", title="all products", products=allProducts)


@app.route("/productPage/<productId>")
def productPage(productId):
    #search_product_by_id
    for product in allProducts:
        if product["id"] == productId:
            return render_template("productPage.html", title=f"{product['name']}", product=product)

    return render_template("404.html", title="404")









allProducts = [
    {
        "id": "1",
        "name": "product 1",
        "description": "this is product number 1",
        "img": "p1.jpg",
        "price": 10
    },
    {
        "id": "2",
        "name": "product 2",
        "description": "this is product number 2",
        "img": "p2.jpg",
        "price": 20
    },
    {
        "id": "3",
        "name": "product 3",
        "description": "this is product number 3",
        "img": "p3.jpg",
        "price": 30
    },
    {
        "id": "4",
        "name": "product 4",
        "description": "this is product number 4",
        "img": "p4.jpg",
        "price": 40
    },
    {
        "id": "5",
        "name": "product 5",
        "description": "this is product number 5",
        "img": "p5.jpg",
        "price": 50
    },
    {
        "id": "6",
        "name": "product 6",
        "description": "this is product number 6",
        "img": "p6.jpg",
        "price": 60
    },
    {
        "id": "7",
        "name": "product 7",
        "description": "this is product number 7",
        "img": "p7.jpg",
        "price": 70
    },
    {
        "id": "8",
        "name": "product 8",
        "description": "this is product number 8",
        "img": "p8.jpg",
        "price": 80
    },
    {
        "id": "9",
        "name": "product 9",
        "description": "this is product number 9",
        "img": "p9.jpg",
        "price": 90
    },
    {
        "id": "10",
        "name": "product 10",
        "description": "this is product number 10",
        "img": "p10.jpg",
        "price": 100
    },
    {
        "id": "11",
        "name": "product 11",
        "description": "this is product number 11",
        "img": "p11.jpg",
        "price": 110
    }
]
