from flask import *
import requests
# twiml == Twilio's markup language
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse

app = Flask("recipeBot")

# messages route
@app.route('/', methods=['POST', 'GET'])
def message():
  # get the value from SMS input & convert to lowercase
  food_input = request.values.get('Body', '').lower()
  # search meal by name
  api = "https://www.themealdb.com/api/json/v1/1/search.php?s=" + food_input
  # search by first letter
  # api = "https://www.themealdb.com/api/json/v1/1/search.php?f=" + food_input

  # make a GET request to the api -- use json formatting
  api_data = requests.get(api).json()

  # Twilio language:
  # create a response SMS to communicate with Twilio library: MessagingResponse
  twilio_response = MessagingResponse()
  media_msg = Message()
  ingredients_msg = Message()
  instructions_msg = Message()
  
  # print themealDB API data
  recipe = api_data['meals'][0]

  # send image of prepared recipe
  if recipe['strMealThumb'] != '':
    media_msg.media(recipe['strMealThumb'])

  # recipe ingredients msg
  recipe_ingredients = ""
  recipe_ingredients += "\n --------------------------- \n"
  # add recipe name & origin:
  recipe_ingredients += "Follow the recipe for: \n" + recipe['strMeal'] + "\n"
  recipe_ingredients += "\nRecipe Origin: \n" + recipe['strArea'] + "\n"
  recipe_ingredients += "\n --------------------------- \n"
  
  # print measures + ingredients for recipe
  recipe_ingredients += "\nIngredients: \n"

  for index in range(1,14):
    measureKey = "strMeasure" + str(index)
    ingredientsKey = "strIngredient" + str(index)

    measureData = recipe[measureKey]
    ingredientsData = recipe[ingredientsKey]

    recipeLine = measureData + " " + ingredientsData
    if recipeLine != "" or recipeLine != " ":
      recipe_ingredients += recipeLine + "\n"
  recipe_ingredients += "\n --------------------------- \n"


  # recipe instructions msg
  recipe_instructions = ""
  recipe_instructions += "\n --------------------------- \n"
  # print recipe instructions
  recipe_instructions += "\nRecipe Instructions: \n" 
  if 'strInstructions' != " ":
    recipe_instructions += recipe['strInstructions']
  recipe_instructions += "\n --------------------------- \n"
  # watch video instructions
  recipe_instructions += "\nWatch Recipe Video: \n"
  if 'strYoutube' != " ":
    recipe_instructions += recipe['strYoutube']
  recipe_instructions += "\n --------------------------- \n"
  # recipe source link
  recipe_instructions += "\nRecipe Source: \n"
  if 'strSource' != " ":
    recipe_instructions += recipe['strSource']
  recipe_instructions += "\n --------------------------- \n"


  # add content to msg body
  ingredients_msg.body(recipe_ingredients)
  instructions_msg.body(recipe_instructions)

  twilio_response.append(media_msg)
  twilio_response.append(ingredients_msg)
  twilio_response.append(instructions_msg)
  return str(twilio_response)


if __name__ == '__main__':
  app.run(debug=True)