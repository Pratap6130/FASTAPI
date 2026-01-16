# from fastapi import FastAPI
# from data import product
# from database import getData

# app = FastAPI()


# #database whih have products and handled by class from data.py
# products = [
#     product(id = 1,
#             name = "laptop",
#             description = "HP Victus",
#             price = 70000,
#             quantity = 5
#             ),

#     product(id = 2,
#             name = "laptop",
#             description = "HP Pavvilion",
#             price = 60000,
#             quantity = 10
#             ),

#     product(id = 3,
#             name = "Tablet",
#             description = "Samsung Galaxy Tab A7",
#             price = 6000,
#             quantity = 8
#             ),
#     product(id = 4,
#             name = "Mobile",
#             description = "samsung s21",
#             price = 50000,
#             quantity = 10
#             )
# ]

# # @app.get('/')
# # def getData():
# #     return "Yuhhu!, welcome home!"


# @app.get("/newPage")
# def newPageData():
#     return "Welcome to new page"   #always return , cause it is response

# @app.get("/all_products")
# def get_Products():
#     return products

# @app.get("/products")
# def get_Products():
#     return getData()
    

# @app.get("/products/{id}")  #path parameter
# def get_Products(id: int):
#     #return products[id - 1]  #list index start from 0, so id - 1
#     for i in products:
#         if i.id == id:
#             return i #return product object if id matches
#     return "404, Product not found"

# @app.post('/products')
# def add_Product(product: product):
#     products.append(product)
#     return {"new product added successfluuy"}


# @app.put("/products")
# def update_product(id:int, product: product):
#     for i in range(len(products)):
#         if products[i].id == id:
#             products[i] = product
#             return {"Product updated successfully"}
#     return "Product not found"

# @app.delete("/products")
# def delete_product(id:int):
#     for i in range(len(products)):
#         if products[i].id == id:
#             products.pop(i)
#             return {"Product deleted successfully"}
#     return "Product not found"


# from fastapi import FastAPI
# from data import product
# from database import getData, add_data, update_data, delete_data
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# app.add_middleware(CORSMiddleware, 
#                    allow_origins=["http://localhost:3000"], 
#                    allow_methods=["*"])

# @app.get("/products")
# def get_Products():
#     return getData()


# @app.get("/Products/{id}") 
# def get_ListOfProducts(id: int):
#     products = getData()
#     for i in products:
#         if i.id == id:
#             return i 
#     return "404, Product not found"
    

# @app.post('/Products')
# def add_Product(product: product):
#     return add_data(product)


# @app.put("/Update_Products")
# def update_product(id:int, product: product):
#     return update_data(id, product)


# @app.delete("/products")
# def delete_product(id:int):
#     return delete_data(id)



from fastapi import FastAPI
from data import product
from database import getData, add_data, update_data, delete_data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, 
                   allow_origins=["http://localhost:3000"], 
                   allow_methods=["*"]
                   )

@app.get("/products/")
def get_Products():
    return getData()


@app.get("/products/{id}") 
def get_ListOfProducts(id: int):
    products = getData()
    for i in products:
        if i.id == id:
            return i 
    return "404, Product not found"
    

@app.post('/products/')
def add_Product(product: product):
    return add_data(product)


@app.put("/products/{id}")
def update_product(id:int, product: product):
    return update_data(id, product)


@app.delete("/products/{id}")
def delete_product(id:int):
    return delete_data(id)








