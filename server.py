"""Server for pantry app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
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

        flash(f"Welcome back, {user.name}!")
    
    
        return redirect(f"/users/{user.user_id}")  #WORK ON REDIRECTING TO THE USERS PROFILE (WITH THE TWO FORMS -PANTRY ING AND ADD RECIPES) 

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

@app.route("/addrecipe")
def add_recipe():
    """ Enable user to add recipe on their profile"""

    recipe = crud.create_recipe()
    recipe_ingredients = crud.upload_recipe_ingredient()



if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
