import pytest
from api_handler.product import ProductClient
from api_handler.cart import CartClient
from api_handler.json_validator import validate_response
from utils.user_input import ip_quantity
import random

@pytest.fixture(scope="module")
def product_client():
    return ProductClient()

@pytest.fixture(scope="module")
def cart_client():
    return CartClient()

def test_full_flow(product_client, cart_client):
    user = 1

    product_payload = {
        "title": "Test Product API",
        "price": 99.99,
        "description": "Created during test",
        "image": "https://i.pravatar.cc",
        "category": "electronics"
    }
    # Create a product
    created = product_client.create_product(product_payload)
    prod_id = created.get("id")
    assert prod_id is not None
    assert validate_response(created, "product_res.json")

    # add the product to the cart with user given quantity
    qty = ip_quantity()
    products_to_add = [{"productId": prod_id, "quantity": qty}]
    cart_resp = cart_client.add_cart(user, products_to_add)
    assert cart_resp["userId"] == user
    assert cart_resp["products"][0]["quantity"] == qty
    assert validate_response(cart_resp, "cart_res.json")
    cart_id = cart_resp["id"]

    #validate item quantity in cart
    cart_details = cart_client.get_user_carts(user)
    assert cart_id in cart_details["cart_id"]
    assert cart_details[prod_id]["totalQuantity"] == qty

    # Delete the cart
    del_resp = cart_client.delete_cart(cart_id)
    assert del_resp.get("id") == cart_id

    #validate cart deletion
    cart_detail_on_delete = cart_client.get_user_carts(user)
    assert cart_id not in cart_detail_on_delete["cart_id"]





    
