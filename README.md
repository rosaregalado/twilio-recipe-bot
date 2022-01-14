Twilio Recipe Bot
-------------------------------------------------------------------------

For people who need a quick food recipe or want to learn how to to cook, 
my twilio recipe bot automatically responds with the ingredients and instructions to the requested food recipe.

Tech Stack:
-------------------------------------------------------------------------
Python, Flask <br />
themealDB API *Database API to get food recipes from around the world*<br />
Twilio MessagingResponse library (Programmable SMS using TwiML)<br />


How it Works:
-------------------------------------------------------------------------
1 - Send text message to twilio phone number: name of a food recipe <br />
(e.g. Salmon, Pizza, Peanut butter cookies)<br />
<br />
2 - Receive an automatic response with: <br />
  a. Name of recipe<br />
  b. Origin of recipe<br />
  c. Ingredients needed<br />
  d. Instructions<br />
  e. Video Instructions tutorial URL<br />
  f. Recipe source URL <br />
  g. Image of cooked meal<br />


Demo:
-------------------------------------------------------------------------
![](recipe-bot.gif)




