"""Models for my_Pantry project App."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f"<User user_id={self.user_id} name={self.name}>"




class Pantry_Ingredient(db.Model):
    """A table for ingredients user has available in their pantry."""

    __tablename__ = "pantry_ingredients"

    pantry_ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    submitted_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.ingredient_id"))
    
    user = db.relationship("User", backref= "pantry_ingredients")
    ingredient = db.relationship("Ingredient", backref = "pantries")
    
    def __repr__(self):
        return f"<pantry_ingredients id={self.pantry_ingredient_id}>"



class Recipe(db.Model):
    """A table for all the recipes"""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    name = db.Column(db.String)
    image_url = db.Column(db.String)
    instructions = db.Column(db.Text)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    prep_time = db.Column(db.String)
    cooking_time = db.Column(db.String)

    user = db.relationship("User", backref= "recipes")
   
    def __repr__(self):
        return f"<recipe id={self.recipe_id} items={self.name}>"


class Recipe_Ingredient(db.Model):
    """A table for all the recipe ingredient"""

    __tablename__ = "recipe_ingredients"

    quantity = db.Column(db.String)
    recipe_ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'))

    recipe = db.relationship("Recipe", backref= "recipe_ingredients")
    ingredient = db.relationship("Ingredient", backref = "recipe_ingredients")


    def __repr__(self):
        return f"<recipe_ingredient id={self.recipe_ingredient_id}>"



class Ingredient(db.Model):
    """A table for all the ingredients"""

    __tablename__ = "ingredients"

    ingredient_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String, nullable = True)
    description = db.Column(db.Text, nullable = True)

    def __repr__(self):
        return f"<ingredients id={self.ingredient_id} name={self.name}>"



def connect_to_db(flask_app, db_uri="postgresql:///pantry", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)