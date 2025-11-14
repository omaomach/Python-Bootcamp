products = {
    "sugar": 200,
    "milk": 100,
    "coffee": 50,
}

highest_product, highest_price = max(products.items(), key=lambda item: item[1])
print(highest_product)