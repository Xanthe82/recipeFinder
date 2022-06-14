# recipeFinder
To use this app you need to install Python 3 and requests.

Python recipe search app
This group project was created by myself and Malek Aliouche for the Code First Girls 'Introduction to Python and Apps' course. The brief was as follows:

Project Brief: Search
In this project you'll create a program to search for recipes based on an ingredient. The standard project uses the Edamam Recipe API, but can be changed to use a different API after completing the required tasks.
You will not need any additional knowledge beyond what is covered in this course to complete this project.
Setup
To use the Edamam API you will need to register for an account. In your Edamam account dashboard you can find an Application ID and Application Key, which you will need to make requests to the API.
To make a request to the Edamam API use the following URL:
For example, if the App ID and App Key for me account were “ch37j44” and “a58hia” I wanted to search for “cheese”, the url would look like this:
https://api.edamam.com/search?q=cheese&app_id=ch37j44&app_key=a58hia
Required Tasks
These are the required tasks for this project. You should aim to complete these tasks before adding your own ideas to the project.
1. Read the Edamam API documentation ★ https://developer.edamam.com/edamam-docs-recipe-api
2. Ask the user to enter an ingredient that they want to search for
3. Create a function that makes a request to the Edamam API with the required ingredient as
part of the search query (also included your Application ID and Application Key
4. Get the returned recipes from the API response
5. Display the recipes for each search result
     https://api.edamam.com/search?q={INGREDIENT}&app_id={YOUR_APP_KEY}&app_key={YOUR_ APP_KEY}
 
 
 We extended the project by using the TKinter GUI framework to add a visual element to the program. We also had the results save to a txt file where each recipe title and its ingredients will be displayed.
 The app is best run with the text editor NOT maximised, as this allows content to be returned in the TKinter window and the python console. 
 When the program is run, the user will enter an ingredient and choose a dietary requirement (if any). Once the search button is clicked, the results are displayed in the TKinter window, with title, url, cuisine type and meal type for each recipe. The recipe title, all dietary labels and a clickable link for each recipe are also displayed in the console. A txt file is also created which shows recipe titles, http addresses and a list of ingredients required for each recipe. This file will be overwritten each time the app is used, unless a search returns no results.
