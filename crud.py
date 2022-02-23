"""CRUD operations."""

from model import db, User, Recipe, RecipeIngredient, PantryIngredient, Ingredient, connect_to_db

def create_user(email, password, name):
    """Create and return a new user."""

    user = User(email=email, password=password, name=name)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):
    """Return a user by user ID."""
    
    return User.query.get(user_id)

def display_users():
    """Display all users"""

    return User.query.all()

def does_this_user_exist_already(email):
    """Return a boolean we can use for the if-statement in server.py."""

    if get_user_by_email(email):
        return True
    else:
        return False

def display_ingredients():
    """Display all ingredients from the ingredients table"""

    return Ingredient.query.all()


def get_ingredient_by_name(name):
    """Display all ingredients by name from the ingredients table"""

    return Ingredient.query.filter_by(name = name).first()

def get_ingredient_by_id(ingredient_id):
    """display all ingredients from the ingredients table by their id"""


    return Ingredient.query.get(ingredient_id)
    
def does_the_password_match(email, password):
    """Return a boolean we can use for the if-statement in server.py."""

    if User.query.filter(User.email == email).first() and (
        User.query.filter(User.password == password).first()):
            return True
            # return User.query.filter(User.email == email).first()
    else:
        return False



def create_recipe(name, image, instructions, created_at, updated_at, prep_time, cooking_time, user):
    """Function which allows the user to create recipes"""

    #recipe can either be uploaded by the user or it can be from the preseed database
    
    recipe = Recipe(
        user = user,
        name = name,
        image_url = image,
        instructions = instructions,
        created_at = created_at,
        updated_at = updated_at,
        prep_time = prep_time,
        cooking_time = cooking_time
    )
    db.session.add(recipe)
    db.session.commit()
    
    return recipe
    
def get_recipe_by_id(recipe_id):
    """Get recipe by its id"""

    return Recipe.query.get(recipe_id)

def upload_recipe_ingredient(quantity, recipe_id, ingredient_id):
    """Create and return a new recipe"""

    recipe_ingredient = RecipeIngredient(quantity=quantity, recipe_id=recipe_id, ingredient_id=ingredient_id)
    db.session.add(recipe_ingredient)
    db.session.commit()
    
    return recipe_ingredient

def display_recipes():
    """Display all the recipes in the database"""

    
    return Recipe.query.all()

def get_recipe_by_user_id(user_id):
    """Return the recipe based on user ID"""

    return Recipe.query.get(user_id)


def upload_pantry_ingredient(submitted_at,user_id,ingredient_id):
    """Add the pantry ingredients to the database under the user_id"""

    pantry_ingredients = PantryIngredient(submitted_at = submitted_at, user_id = user_id, ingredient_id = ingredient_id)
    db.session.add(pantry_ingredients)
    deb.session.commit()

    return pantry_ingredients









if __name__ == '__main__':
    from server import app
    connect_to_db(app)