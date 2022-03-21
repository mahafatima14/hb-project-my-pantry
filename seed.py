"""seeding data into our database"""
import os
# from datetime import datetime

import crud
import model
import server

os.system("dropdb pantry")
os.system("createdb pantry")
 
model.connect_to_db(server.app)
model.db.create_all()

model.connect_to_db(server.app) 
model.db.create_all()


def load_users():
    """Users"""
    #seed the first user in the database and add to the session:
    first_user = model.User(name = "Ron Weasley", email = "test@test.test", password = "test")
    model.db.session.add(first_user)

    #seed the second user to the database and add to the session:
    second_user= model.User(name = "Harry Potter", email = "test1@test.test", password = "test")
    model.db.session.add(second_user)

    #commit users to the database
    model.db.session.commit()


load_users()

def load_recipes():
    """Recipes to use for the Pantry App"""

    #create recipes and add then to the database:
    chicken_soup = model.Recipe(
        name = 'Chicken Soup',
        image_url = '/static/img/chicken_soup.jpg',
        instructions ='Put the chicken, carrots, celery and onion in a large soup pot and cover with cold water. Heat and simmer, uncovered, until the chicken meat falls off of the bones (skim off foam every so often).Take everything out of the pot. Strain the broth. Pick the meat off of the bones and chop the carrots, celery and onion. Season the broth with salt, pepper and chicken bouillon to taste, if desired. Return the chicken, carrots, celery and onion to the pot, stir together, and serve.',
        created_at = '1 day ago',
        updated_at= '1 day ago',
        prep_time = '5 mins',
        cooking_time = '10 mins',
        user_id = 1
      
        

    )
    model.db.session.add(chicken_soup)
    model.db.session.commit()


    chocolatechip_cookies = model.Recipe(
        name ='Chocolate Chip cookies',
        image_url ='/static/img/chocolatechip.jpg',
        instructions = 'Preheat oven to 350 degrees F (175 degrees C). Cream together the butter, white sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Dissolve baking soda in hot water. Add to batter along with salt. Stir in flour, chocolate chips, and nuts. Drop by large spoonfuls onto ungreased pans.Bake for about 10 minutes in the preheated oven, or until edges are nicely browned.',
        created_at = '1 day ago',
        updated_at = '1 day ago',
        prep_time = '20 mins',
        cooking_time = '10 mins',
        user_id = 2
      
    )
    model.db.session.add(chocolatechip_cookies)
    model.db.session.commit() 

    chicken_macaroni_salad = model.Recipe(
        name ='Cold Chicken Macaroni Salad',
        image_url ='/static/img/macaroni_salad.jpg',
        instructions = 'Bring a large pot of water to a boil and add chicken; continue to boil until no longer pink in the middle, 15 to 20 minutes. Let sit until cool enough to handle, then dice into small bite-sized pieces. While chicken cooks, bring a second large pot of lightly salted water to a boil. Cook elbow macaroni in the boiling water, stirring occasionally, until tender yet firm to the bite, about 8 minutes. Drain and rinse under cool water.At the same time, place eggs in a saucepan and cover with water. Bring to a boil, remove from heat, and let eggs stand in hot water for 15 minutes.Remove eggs from hot water and hold under cold running water to cool. Peel and dice eggs.Mix mayonnaise, sugar, vinegar, onion salt, salt, mustard, and pepper together in a large bowl. Mix in diced eggs, pasta, and chicken, adding a little more mayonnaise if too dry. Chill for at lest 1 hour, or up to 8 hours or overnight before serving.',
        created_at = '3 day ago',
        updated_at = '3 day ago',
        prep_time = '15 mins',
        cooking_time = '20 mins',
        user_id = 2
      
    )
    model.db.session.add(chicken_macaroni_salad)
    model.db.session.commit() 

    greek_salad = model.Recipe(
        name ='Greek Salad',
        image_url ='/static/img/salad.jpg',
        instructions = 'Bring a large pot of water to a boil and add chicken; continue to boil until no longer pink in the middle, 15 to 20 minutes. Let sit until cool enough to handle, then dice into small bite-sized pieces. While chicken cooks, bring a second large pot of lightly salted water to a boil. Cook elbow macaroni in the boiling water, stirring occasionally, until tender yet firm to the bite, about 8 minutes. Drain and rinse under cool water.At the same time, place eggs in a saucepan and cover with water. Bring to a boil, remove from heat, and let eggs stand in hot water for 15 minutes.Remove eggs from hot water and hold under cold running water to cool. Peel and dice eggs.Mix mayonnaise, sugar, vinegar, onion salt, salt, mustard, and pepper together in a large bowl. Mix in diced eggs, pasta, and chicken, adding a little more mayonnaise if too dry. Chill for at lest 1 hour, or up to 8 hours or overnight before serving.',
        created_at = '3 day ago',
        updated_at = '3 day ago',
        prep_time = '15 mins',
        cooking_time = '20 mins',
        user_id = 2
      
    )
    model.db.session.add(greek_salad)
    model.db.session.commit() 

    easy_beef = model.Recipe(
        name ='Easy Ginger Beef',
        image_url ='/static/img/beef_stew.jpg',
        instructions = 'Bring a large pot of water to a boil and add chicken; continue to boil until no longer pink in the middle, 15 to 20 minutes. Let sit until cool enough to handle, then dice into small bite-sized pieces. While chicken cooks, bring a second large pot of lightly salted water to a boil. Cook elbow macaroni in the boiling water, stirring occasionally, until tender yet firm to the bite, about 8 minutes. Drain and rinse under cool water.At the same time, place eggs in a saucepan and cover with water. Bring to a boil, remove from heat, and let eggs stand in hot water for 15 minutes.Remove eggs from hot water and hold under cold running water to cool. Peel and dice eggs.Mix mayonnaise, sugar, vinegar, onion salt, salt, mustard, and pepper together in a large bowl. Mix in diced eggs, pasta, and chicken, adding a little more mayonnaise if too dry. Chill for at lest 1 hour, or up to 8 hours or overnight before serving.',
        created_at = '3 day ago',
        updated_at = '3 day ago',
        prep_time = '15 mins',
        cooking_time = '20 mins',
        user_id = 2
      
    )
    model.db.session.add(easy_beef)
    model.db.session.commit() 

load_recipes()


def load_ingredients():
    """ Ingredients in the database """

    #create ingredients and add them to the Ingredienst table in the database:
    whole_chicken = model.Ingredient(
        name = 'whole chicken',
        image = '',
        description = ''
    )
    model.db.session.add(whole_chicken)
    
    carrot = model.Ingredient(
        name = 'carrot',
        image = '',
        description = ''   
    )
    model.db.session.add(carrot)

    celery = model.Ingredient(
        name = 'celery',
        image = '',
        description = ''
    )
    model.db.session.add(celery)

    onion = model.Ingredient(
        name = 'onion',
        image = '',
        description = ''
    )
    model.db.session.add(onion)

    chicken_bouillon = model.Ingredient(
        name = 'chicken bouillon',
        image = '',
        description = ''
    )
    model.db.session.add(chicken_bouillon)

    butter = model.Ingredient(
        name = 'butter',
        image = '',
        description = ''
    )
    model.db.session.add(butter)

    white_sugar = model.Ingredient(
        name = 'white sugar',
        image = '',
        description = ''
    )
    model.db.session.add(white_sugar)
   
    brown_sugar = model.Ingredient(
        name = 'brown sugar',
        image = '',
        description = ''
    )
    model.db.session.add(brown_sugar)

    eggs = model.Ingredient(
        name = 'eggs',
        image = '',
        description = ''
    )
    model.db.session.add(eggs)

    vanilla_extract = model.Ingredient(
        name = 'vanilla extract',
        image = '',
        description = ''
    )
    model.db.session.add(vanilla_extract)

    baking_soda = model.Ingredient(
        name = 'baking soda',
        image = '',
        description = ''
    )
    model.db.session.add(baking_soda)

    salt = model.Ingredient(
        name = 'salt',
        image = '',
        description = ''
    )
    model.db.session.add(salt)

    peper = model.Ingredient(
        name = 'pepper',
        image = '', 
        description = ''
    )
    model.db.session.add(peper)
    
    all_purpose_flour = model.Ingredient(
        name = 'all purpose flour',
        image = '',
        description = ''
    )
    model.db.session.add(all_purpose_flour)

    semi_sweet_chocolate_chips =model.Ingredient(
        name = 'semi sweet chocolate chips',
        image = '',
        description = ''
    )
    model.db.session.add(semi_sweet_chocolate_chips)

    walnuts = model.Ingredient(
        name = 'walnuts',
        image = '',
        description = ''
    )
    model.db.session.add(walnuts)
    model.db.session.commit()

    mayonnaise = model.Ingredient(
        name = 'Mayonnaise',
        image = '',
        description = ''
    )
    model.db.session.add(mayonnaise)
    model.db.session.commit()

    vineger = model.Ingredient(
        name = 'Distilled white vineger',
        image = '',
        description = ''
    )
    model.db.session.add(vineger)
    model.db.session.commit()

    mustard = model.Ingredient(
        name = 'yellow mustard',
        image = '',
        description = ''
    )
    model.db.session.add(mustard)
    model.db.session.commit()

    bell_peppers = model.Ingredient(
        name = 'Bell Peppers',
        image = '',
        description = ''
    )
    model.db.session.add(bell_peppers)
    model.db.session.commit()

   
load_ingredients()




def load_recipe_ingredients():
    """Add ingredients to recipes"""
    #~~~~~~~~~~~~~~~Recipe1~~~~~~~~~~~~~~~~~~~~~
    #grab the chickensoup recipe by querying for it from the recipes table and save it in recipe_chickensoup variable
    recipe_chickensoup = model.Recipe.query.filter_by(name = 'Chicken Soup').first()

    #grab the chickensoup ingredients by querying for them from the Ingredients table and save them to the recipe_chickensoup_ingredients variable
    recipe_chickensoup_ingredients = model.Ingredient.query.filter((model.Ingredient.name == 'whole chicken') | (model.Ingredient.name == 'carrot') | (model.Ingredient.name == 'onion') | (model.Ingredient.name == 'celery') | (model.Ingredient.name == 'chicken bouillon') | (model.Ingredient.name == 'salt') | (model.Ingredient.name == 'pepper')).all()
    
    #loop over the ingredients and add them to the recipe_ingredients table, under the right name and ingredient
    for ingredient in recipe_chickensoup_ingredients:
        recipe_ingredient = model.RecipeIngredient(recipe = recipe_chickensoup, ingredient = ingredient)
        model.db.session.add(recipe_ingredient)

    #~~~~~~~~~~~~~~~~Recipe2~~~~~~~~~~~~~~~~~~~~
    
    recipe_chocolatechip = model.Recipe.query.filter_by(name = 'Chocolate Chip cookies').first()
    recipe_chocolatechip_ingredients = model.Ingredient.query.filter((model.Ingredient.name == 'butter') | (model.Ingredient.name =='vanilla extract') | (model.Ingredient.name == 'eggs') | (model.Ingredient.name == 'brown_sugar') | (model.Ingredient.name == 'semi_sweet_chocolate_chips') | (model.Ingredient.name == 'all_purpose_flour') | (model.Ingredient.name == 'walnuts') | (model.Ingredient.name == 'salt') | (model.Ingredient.name == 'baking soda')).all()

    for ingredient in recipe_chocolatechip_ingredients:
        recipe_ingredient = model.RecipeIngredient(recipe = recipe_chocolatechip, ingredient = ingredient)
        model.db.session.add(recipe_ingredient)
    #~~~~~~~~~~~~~~Recipe3~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    recipe_chickenmacaronisalad = model.Recipe.query.filter_by(name = 'Cold Chicken Macaroni Salad').first()
    recipe_chickenmacaronisalad_ingredients = model.Ingredient.query.filter((model.Ingredient.name == 'whole chicken') | (model.Ingredient.name == 'salt') | (model.Ingredient.name == 'pepper') | (model.Ingredient.name == 'onion') | (model.Ingredient.name == 'celery') | (model.Ingredient.name == 'carrot') | (model.Ingredient.name == 'Mayonnaise') | (model.Ingredient.name == 'Distilled white vineger') | (model.Ingredient.name == 'Bell Peppers') | (model.Ingredient.name == 'yellow mustard'))
    
    for ingredient in recipe_chickenmacaronisalad_ingredients:
        recipe_ingredient = model.RecipeIngredient(recipe = recipe_chickenmacaronisalad, ingredient = ingredient)
        model.db.session.add(recipe_ingredient)
    
    
    
    model.db.session.commit()      



load_recipe_ingredients()



