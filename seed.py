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

    chicken_soup = Recipe(
        name = 'Chicken Soup',
        image_url = '',
        instructions ='Put the chicken, carrots, celery and onion in a large soup pot and cover with cold water. Heat and simmer, uncovered, until the chicken meat falls off of the bones (skim off foam every so often).Take everything out of the pot. Strain the broth. Pick the meat off of the bones and chop the carrots, celery and onion. Season the broth with salt, pepper and chicken bouillon to taste, if desired. Return the chicken, carrots, celery and onion to the pot, stir together, and serve.',
        created_at = '1 day ago',
        updated_at= '1 day ago',
        prep_time = '5 mins',
        cooking_time = '10 mins'
        

    )
    model.db.session.add_all(chicken_soup)
    model.db.session.commit()

    chocolatechip_cookies = Recipe(
        name ='Chocolate Chip cookies',
        image_url ='',
        instructions = 'Preheat oven to 350 degrees F (175 degrees C). Cream together the butter, white sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Dissolve baking soda in hot water. Add to batter along with salt. Stir in flour, chocolate chips, and nuts. Drop by large spoonfuls onto ungreased pans.Bake for about 10 minutes in the preheated oven, or until edges are nicely browned.',
        created_at = '1 day ago',
        updated_at = '1 day ago',
        prep_time = '20 mins',
        cooking_time = '10 mins'
    )
    model.db.session.add_all(chocolatechip_cookies)
    model.db.session.commit() 


def load_ingredients():
    """ Ingredients in the database """

    whole_chicken = Ingredient(
        name = 'whole chicken',
        image = '',
        description = ''
    )
    model.db.session.add(whole_chicken)
    
    carrot = Ingredient(
        name = 'carrot',
        image = '',
        description = ''   
    )
    model.db.session.add(carrot)

    celery = Ingredient(
        name = 'celery',
        image = '',
        description = ''
    )
    model.db.session.add(celery)

    onion = Ingredient(
        name = 'onion',
        image = '',
        description = ''
    )

    chicken_bouillon = Ingredient(
        name = 'chicken bouillon',
        image = '',
        description = ''
    )
    butter = Ingredient(
        name = 'butter',
        image = '',
        description = ''
    )
    white_sugar = Ingredient(
        name = 'white sugar',
        image = '',
        description = ''
    )
    brown_sugar = Ingredient(
        name = 'brown sugar',
        image = '',
        description = ''
    )
    eggs = Ingredient(
        name = 'eggs',
        image = '',
        description = ''
    )
    vanilla_extract = Ingredient(
        name = 'vanilla extract',
        image = '',
        description = ''
    )
    baking_soda = Ingredient(
        name = 'baking soda',
        image = '',
        description = ''
    )
    salt = Ingredient(
        name = 'salt',
        image = '',
        description = ''
    )
    peper = Ingredient(
        name = 'pepper',
        image = '', 
        description = ''
    )
    
    all_purpose_flour = Ingredient(
        name = 'all_purpose_flour',
        image = '',
        description = ''
    )
    semi_sweet_chocolate_chips = Ingredient(
        name = 'semi_sweet_chocolate_chips',
        image = '',
        description = ''
    )
    walnuts =  Ingredient(
        name = 'walnuts',
        image = '',
        description = ''
    )
model.db.session.commit()


def load_recipe_ingredients():
    """Add ingredients to recipes"""

    recipe_chickensoup = Recipe.query.filter_by(Recipe.name == 'chicken_soup').first()
    recipe_chickensoup_ingredients = Ingredient.query.filter(Ingredient.name == 'whole chicken', Ingredient.name == 'carrot', Ingredient.name == 'onion', Ingredient.name == 'celery', Ingredient.name == 'chicken bouillon', Ingredient.name == 'salt', Ingredient.name == 'pepper').all()

    
    






    # chicken_soup.ingredients.append(whole_chicken)

    # recipe_chocolatechip = Recipe.query.filter_by(Recipe.name == 'chocolate_chip').first()
    # recipe_chocolatechip_ingredients = Ingredient.query.filter(Ingredient.name == 'butter',Ingredient.name =='Vanilla extract')

         



