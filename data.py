from pydantic import BaseModel
#to take the class and validate it 

class product(BaseModel ):
    id : int
    name : str
    description : str
    price : float
    quantity : int
    
    # def __init__(self, id, name, description, price, quantity):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity

        