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
        #session["user_id"] = user.user_id

        flash(f"Welcome back, {user.name}!")
        
        return redirect(f"/users/{user.user_id}")  

@app.route("/logout")
def logout():
    """Log out."""

    # removing the user from the session
    del session["user_email"]
    del session["user_name"]

    flash("You are logged out!")

    return redirect("/")

@app.route("/recipes")
def show_recipes():
    """Show all recipes"""

    recipes = crud.display_recipes()

    return render_template('allrecipes.html', recipes = recipes)


@app.route("/users")
def show_users():
    """Display all users"""

    users = crud.display_users()
    

    return render_template('allusers.html', users = users)



@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a particular user."""

    
    user = crud.get_user_by_id(user_id)
    ingredients = crud.display_ingredients() 

    return render_template("userdetail.html", user = user, ingredients = ingredients)    


@app.route("/addrecipe", methods=["POST"])
def add_recipe():
    """ Enable user to add recipe on their profile"""
   
    #grab all the element for create_recipe from the userdetail.html form
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
    

    quantity = '1' # default value for now
    recipe = crud.create_recipe(name,image_url,instructions,cooking_time,prep_time,created_at,updated_at)

    for ingredient in ingredients:
        db_ingredient = crud.get_ingredient_by_name(ingredient)
        # if not db_ingredient:
        #     db_ingredient = crud.create_ingredient(name, image if image, description if description)
        # recipe_ingredient = crud.upload_recipe_ingredient(quantity, recipe.recipe_id, db_ingredient.ingredient_id)
        
        if db_ingredient:
            recipe_ingredient = crud.upload_recipe_ingredient(quantity,recipe.recipe_id, db_ingredient.ingredient_id)
            print(recipe_ingredient, '^^^^^^ RECIPE INGREDIENT ^^^^^')

    #call the crud function create_recipe and pass in the arguements to create a recipe
    #recipe = crud.create_recipe(name,image_url,instructions,cooking_time,prep_time,created_at,updated_at)
    
    
  
    
    
    return redirect("/recipes")















if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
