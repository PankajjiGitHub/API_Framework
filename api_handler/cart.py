from .api_handler import RequestHandler

#This module handles cart operations such as adding products, retrieving user carts, and deleting carts.
class CartClient:
    def __init__(self):
        self.req = RequestHandler()

    # Method to Add Product to Cart
    def add_cart(self, user_id, products):
        body = {"userId": user_id, "products": products}
        return self.req.send("POST", "/carts", json=body)
    
    # Method to Get User Cart Details
    def get_user_carts(self, user_id):
        return self.req.send("GET", f"/carts?userId={user_id}")

    # Method to Delete Cart
    def delete_cart(self, cart_id):
        return self.req.send("DELETE", f"/carts/{cart_id}")
