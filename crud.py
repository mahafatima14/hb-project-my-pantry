"""CRUD operations."""

from model import db, User, Recipe, Recipe_Ingredient, Pantry_ingredient, Ingredient, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def read_recipe_ingredient():
    """Go through recipe ingredients and see if they match pantry ingredients"""









if __name__ == '__main__':
    from server import app
    connect_to_db(app)