from datetime import datetime

import crud
import model
import server

os.system("dropdb pantry")
os.system("createdb pantry")

model.connect_to_db(server.app)
model.db.create_all()

def load_recipes:
    """Recipes to use for the Pantry App"""

    recipe_one = {
        'name': 'Chicken Soup'
        'image_url':
        'instructions': 'Put the chicken, carrots, celery and onion in a large soup pot and cover with cold water. Heat and simmer, uncovered, until the chicken meat falls off of the bones (skim off foam every so often).Take everything out of the pot. Strain the broth. Pick the meat off of the bones and chop the carrots, celery and onion. Season the broth with salt, pepper and chicken bouillon to taste, if desired. Return the chicken, carrots, celery and onion to the pot, stir together, and serve.'
        'created_at': 
        'updated_at':

    }
    model.db.session.add_all(recipe_one)
    model.db.session.commit()