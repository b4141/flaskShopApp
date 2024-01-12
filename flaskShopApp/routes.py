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
        "name": "ANASTASIA",
        "description": "Eyelash Mascara",
        "imgs": ["p1-1.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 3,
        "price": 10.99,
        "reviewsNumber": 123,
        "ingredients": "None"
    },
    {
        "id": "2",
        "name": "HOURGLASS",
        "description": "Body Cream",
        "imgs": ["p2-1.png", "p2-1.png", "p2-1.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 3,
        "price": 20.99,
        "reviewsNumber": 123,
        "ingredients": "None"
    },
    {
        "id": "3",
        "name": "stila",
        "description": "Eye Liner",
        "imgs": ["p3-1.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 30.99,
        "reviewsNumber": 123,
        "ingredients": "None"
    },
    {
        "id": "4",
        "name": "Unlocked",
        "description": "Instant Extensions Mascara",
        "imgs": ["p4-2.png"],
        "fullDescription": "The look of lash extensions in an instant. This mascara is the ultimate formula for when more is more: more definition, more lift and more length to transform lashes with impossibly real results. Using film-forming technology, it coats each lash in lightweight fibers that lock in place for a high-impact, fanned-out finish and smudge-proof wear.",
        "rating": 3,
        "price": 40.99,
        "reviewsNumber": 123,
        "ingredients": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    },
    {
        "id": "5",
        "name": "product 5",
        "description": "this is product number 5",
        "imgs": ["p5-1.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 50.99,
        "reviewsNumber": 123,
        "ingredients": "None"
    },
    {
        "id": "6",
        "name": "product 6",
        "description": "this is product number 6",
        "imgs": ["p6-1.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 60.99,
        "reviewsNumber": 123,
        "ingredients": "None"
    },
    {
        "id": "7",
        "name": "product 7",
        "description": "this is product number 7",
        "imgs": ["p7-1.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 70.99,
        "reviewsNumber": 123,
        "ingredients": "None"
    },
    {
        "id": "8",
        "name": "product 8",
        "description": "this is product number 8",
        "imgs": ["p8-1.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 80.99,
        "reviewsNumber": 123,
        "ingredients": "None"
    },
    {
        "id": "9",
        "name": "product 9",
        "description": "this is product number 9",
        "imgs": ["p9-1.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 90.99,
        "reviewsNumber": 123,
        "ingredients": "None"
    },
    {
        "id": "10",
        "name": "product 10",
        "description": "this is product number 10",
        "imgs": ["p10-1.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 100.99,
        "reviews-Umber": 102,
        "ingredients": "None"
    },
    {
        "id": "11",
        "name": "product 11",
        "description": "this is product number 11",
        "imgs": ["p4-1.png"],
        "fullDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "rating": 5,
        "price": 110.99,
        "reviews-Umber": 102,
        "ingredients": "None"
    }
]
