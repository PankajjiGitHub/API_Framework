from .api_handler import RequestHandler

# This module handles product operations such as creating, listing, and deleting products.
class ProductClient:
    def __init__(self):
        self.req = RequestHandler()

    # Method to Get a list of products, optionally limited by a number
    def list_products(self, limit=None):
        params = {}
        if limit:
            params["limit"] = limit
        return self.req.send("GET", "/products", params=params)

    #Method to Create Product
    def create_product(self, payload):
        return self.req.send("POST", "/products", json=payload)

    #Method to Delete Product
    def delete_product(self, product_id):
        return self.req.send("DELETE", f"/products/{product_id}")
