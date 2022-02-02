"""CRUD operations."""

from model import db, User, Recipe, RecipeIngredient, PantryIngredient, Ingredient, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_recipe(name, image, instructions, created_at, updated_at, prep_time, cooking_time, user = None):
    """Function which allows the user to create recipes"""

    #recipe can either be uploaded by the user or it can be from the preseed database
    if not user:
        user_id = None
    else:
        user_id = user.user_id
    
    recipe = Recipe(
        user_id = user_id,
        name = name,
        image = image,
        instructions = instructions,
        created_at = created_at,
        updated_at = updated_at,
        prep_time = prep_time,
        cooking_time = cooking_time

    )
    return recipe
    
    

def upload_recipe_ingredient(quantity, recipe, ingredient):
    """Create and return a new recipe"""

    recipe_ingredient = RecipeIngredient(quantity = quantity,  recipe = recipe.recipe.id, ingredient = ingredient.ingredient.id)

    return recipe_ingredient

def display_recipes():
    """Display all the recipes in the database"""

    
    return Recipe.query.all()




def read_recipe_ingredient():
    """Go through recipe ingredients and see if they match pantry ingredients"""


def load_pantry_ingredients():
    """Add all the ingredients user enters"""










if __name__ == '__main__':
    from server import app
    connect_to_db(app)