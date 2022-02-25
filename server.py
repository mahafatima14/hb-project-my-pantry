"""Server for pantry app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
from datetime import datetime
import crud

# configure a Jinja2 setting to make it throw errors for undefined variables
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
    
@app.route("/")
def homepage():
    """View homepage."""
    return render_template("homepage.html")


@app.route("/newusers", methods=["POST"])
def register_user():
    """Create a new user."""
    
    email = request.form.get("email")
    password = request.form.get("password")
    name = request.form.get("name")

    if not crud.does_this_user_exist_already(email):
        crud.create_user(email, password, name)
        flash("Account created! Please log in.")
    else:
        flash("This user already exists! Please try again")
    
   
    return redirect("/")


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
        
        return redirect("/")
     
    else:
        # Log in user by storing the user's email and name in session
        session["user_email"] = user.email
        session["user_name"] = user.name
        session["user_id"] = user.user_id

        flash(f"Welcome back, {user.name}!")
        
        return redirect(f"/users/{user.user_id}")  

@app.route("/logout")
def logout():
    """Log out."""

    # removing the user from the session
    # session.clear()
    if session.get("user_email"):
        del session["user_email"]
    
    if session.get("user_name"):
        del session["user_name"]
        
    flash("You are logged out!")

    return redirect("/")

@app.route("/recipes")
def show_recipes():
    """Show all recipes"""

    
    recipes = crud.display_recipes()

    return render_template('allrecipes.html', recipes = recipes)

@app.route("/recipes/<recipe_id>")
def show_recipe(recipe_id):

    user = session.get("user_email")
    if user:
        recipe = crud.get_recipe_by_id(recipe_id)
        return render_template("recipedetails.html", recipe = recipe) 
    else:
        flash("Please log in to view all recipes!")
        return redirect("/")


       
@app.route("/users")
def show_users():
    """Display all users"""

    user = session.get("user_email")
    if user:
        users = crud.display_users()
        return render_template('allusers.html', users = users)
    else:
        flash("Please log in to continue!")
        return redirect("/")



    

@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a particular user."""

    user = session.get("user_email")
    if user == user:
        user = crud.get_user_by_id(user_id)
        ingredients = crud.display_ingredients() 
        return render_template("userdetail.html", user = user, ingredients = ingredients)    
    else:
        flash("Please log in to continue!")
        return redirect("/")
    

@app.route("/addrecipe", methods=["POST"])
def add_recipe():
    """ Enable user to add recipe on their profile and loads it to the database"""
    user_email = session.get("user_email")
   
    #grab all the element for create_recipe from the userdetail.html form
    user = crud.get_user_by_email(user_email)
    name = request.form.get("recipename")
    instructions = request.form.get("recipe_instructions")
    image_url = request.form.get("recipe_image")
    cooking_time = request.form.get("recipe_cookng_time")
    prep_time = request.form.get("recipe_prep_time")
    ingredients = request.form.getlist("addingredients")
    # quantities = request.form.getlist("quantity") # quantities[0] should be the quantity of ingredients[0], and so on
    now = datetime.now()
    created_at = now.strftime("%H:%M:%S")
    updated_at = created_at
    
    recipe = crud.create_recipe(name, image_url, instructions, created_at, updated_at, prep_time, cooking_time, user)

    for ingredient in ingredients:
        db_ingredient = crud.get_ingredient_by_name(ingredient)

        quantity = request.form.get("quantity_"+ingredient)

        # if not db_ingredient:
        #     db_ingredient = crud.create_ingredient(name, image if image, description if description)
       
        if db_ingredient:
            recipe_ingredient = crud.upload_recipe_ingredient(quantity,recipe.recipe_id, db_ingredient.ingredient_id)
            

    return redirect("/recipes")

@app.route("/pantryitems", methods=["POST"])
def upload_pantry_form():
    """Uploads the pantry form"""
    user_id = session.get("user.user_id")
    user = crud.get_user_by_id(user_id)
    now = datetime.now()

    pantry_ingredients = request.form.getlist("addpantryingredients")
    # recipes = []
    recipes = {}
    for ingredient in pantry_ingredients:
        db_ingredient = crud.get_ingredient_by_name(ingredient)
        pantry_ingredient = crud.upload_pantry_ingredient(submitted_at = now, user_id = user, ingredient = db_ingredient)
        ingredient_recipes = crud.find_recipes_by_ingredient_id(db_ingredient.ingredient_id)
        recipes.setdefault(ingredient, ingredient_recipes)
        
        # find_recipes_by_ingredient_id(db_ingredient.ingredient_id) will return a list of recipes for this ingredient otherwise it'll return []
        # take the list from the above step and just extend it to recipes OR
        # recipes.setdefault(ingredient, recipes)
        
        # setdefault(key, value) is a dict method that takes in a key that you're looking for in your dictionary, and IF that key doesn't exist, 
        # it'll set the key to be the value set as the second argument 

    return render_template("recipesfound.html", recipes = recipes)












if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
