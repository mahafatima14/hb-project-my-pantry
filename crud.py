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


def does_the_password_match(email, password):
    """Return a boolean we can use for the if-statement in server.py."""

    if User.query.filter(User.email == email).first() and (
        User.query.filter(User.password == password).first()):
            return True
            # return User.query.filter(User.email == email).first()
    else:
        return False



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
    
    

def upload_recipe_ingredient(quantity, recipe_id, ingredient_id):
    """Create and return a new recipe"""

    recipe_ingredient = RecipeIngredient(quantity=quantity,  recipe_id=recipe_id, ingredient_id=ingredient_id)
    db.session.add(recipe_ingredient)
    db.session.commit()
    
    return recipe_ingredient

def display_recipes():
    """Display all the recipes in the database"""

    
    return Recipe.query.all()

def get_recipe_by_user_id(user_id):
    """Return the recipe based on user ID"""

    return Recipe.query.get(user_id)


# def load_pantry_ingredients():
#    """Add all the ingredients user enters"""



# def read_recipe_ingredient():
#     """Go through recipe ingredients and see if they match pantry ingredients"""













if __name__ == '__main__':
    from server import app
    connect_to_db(app)