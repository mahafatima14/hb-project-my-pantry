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

def load_recipes():
    """Recipes to use for the Pantry App"""

    chicken_soup = model.Recipe(
        name = 'Chicken Soup',
        image_url = '',
        instructions ='Put the chicken, carrots, celery and onion in a large soup pot and cover with cold water. Heat and simmer, uncovered, until the chicken meat falls off of the bones (skim off foam every so often).Take everything out of the pot. Strain the broth. Pick the meat off of the bones and chop the carrots, celery and onion. Season the broth with salt, pepper and chicken bouillon to taste, if desired. Return the chicken, carrots, celery and onion to the pot, stir together, and serve.',
        created_at = '1 day ago',
        updated_at= '1 day ago',
        prep_time = '5 mins',
        cooking_time = '10 mins'
        

    )
    model.db.session.add(chicken_soup)
    model.db.session.commit()

    chocolatechip_cookies = model.Recipe(
        name ='Chocolate Chip cookies',
        image_url ='',
        instructions = 'Preheat oven to 350 degrees F (175 degrees C). Cream together the butter, white sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Dissolve baking soda in hot water. Add to batter along with salt. Stir in flour, chocolate chips, and nuts. Drop by large spoonfuls onto ungreased pans.Bake for about 10 minutes in the preheated oven, or until edges are nicely browned.',
        created_at = '1 day ago',
        updated_at = '1 day ago',
        prep_time = '20 mins',
        cooking_time = '10 mins'
    )
    model.db.session.add(chocolatechip_cookies)
    model.db.session.commit() 

load_recipes()


def load_ingredients():
    """ Ingredients in the database """

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
        name = 'all_purpose_flour',
        image = '',
        description = ''
    )
    model.db.session.add(all_purpose_flour)

    semi_sweet_chocolate_chips =model.Ingredient(
        name = 'semi_sweet_chocolate_chips',
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

load_ingredients()

def load_recipe_ingredients():
    """Add ingredients to recipes"""

    recipe_chickensoup = model.Recipe.query.filter_by(name = 'Chicken Soup').first()
    recipe_chickensoup_ingredients = model.Ingredient.query.filter((model.Ingredient.name == 'whole chicken') | (model.Ingredient.name == 'carrot') | (model.Ingredient.name == 'onion') | (model.Ingredient.name == 'celery') | (model.Ingredient.name == 'chicken bouillon') | (model.Ingredient.name == 'salt') | (model.Ingredient.name == 'pepper')).all()

    
    


    for ingredient in recipe_chickensoup_ingredients:
        recipe_ingredient = model.Recipe_Ingredient(recipe = recipe_chickensoup, ingredient = ingredient)
        # recipe_chickensoup.recipe_ingredients.append(recipe_ingredient)
        model.db.session.add(recipe_ingredient)
    
    
    model.db.session.commit()

load_recipe_ingredients()

    
    # recipe_chocolatechip = Recipe.query.filter_by(Recipe.name == 'chocolate_chip').first()
    # recipe_chocolatechip_ingredients = Ingredient.query.filter(Ingredient.name == 'butter',Ingredient.name =='Vanilla extract')

         



