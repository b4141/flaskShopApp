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
        "imgs": ["p1.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 3,
        "price": 10
    },
    {
        "id": "2",
        "name": "product 2",
        "description": "this is product number 2",
        "imgs": ["p2.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 20
    },
    {
        "id": "3",
        "name": "product 3",
        "description": "this is product number 3",
        "imgs": ["p3.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 30
    },
    {
        "id": "4",
        "name": "product 4",
        "description": "this is product number 4",
        "imgs": ["p4.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 40
    },
    {
        "id": "5",
        "name": "product 5",
        "description": "this is product number 5",
        "imgs": ["p5.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 50
    },
    {
        "id": "6",
        "name": "product 6",
        "description": "this is product number 6",
        "imgs": ["p6.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 60
    },
    {
        "id": "7",
        "name": "product 7",
        "description": "this is product number 7",
        "imgs": ["p7.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 70
    },
    {
        "id": "8",
        "name": "product 8",
        "description": "this is product number 8",
        "imgs": ["p8.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 80
    },
    {
        "id": "9",
        "name": "product 9",
        "description": "this is product number 9",
        "imgs": ["p9.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 90
    },
    {
        "id": "10",
        "name": "product 10",
        "description": "this is product number 10",
        "imgs": ["p10.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 100
    },
    {
        "id": "11",
        "name": "product 11",
        "description": "this is product number 11",
        "imgs": ["p11.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 110
    }
]
