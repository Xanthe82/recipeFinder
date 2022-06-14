import tkinter as tk
import requests
window = tk.Tk() # Setting up the tkinter root which displays as a window
window.title("Recipe search")
window.configure(bg="#9A86A4") # Background colour

intro_label = tk.Label(window, text="Search for recipes by ingredient and dietary requirement, and save the results", bg="#9A86A4", pady=5)
intro_label.pack()

def recipe_search(ingredient):
    app_id = "3f80760a"
    app_key = "d5d8ee211bdc9487f658b56a186bf632"
    result = requests.get(f"https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}")
    data = result.json()
    return (data["hits"])

def run():
    ingredient = ingred_entry.get() # The ingredient typed into the entry is stored as a variable
    dietary = clicked.get() # The input gained from selecting a drop-down menu item is stored as variable
    results = recipe_search(ingredient)

    info = tk.Text(window, bg="#B1BCE6", pady=5, padx=20)  # Setting up a text box to display the search results
    info.pack()  # Putting it onto the screen

    ret_recipes = []                                # empty list to append search results to
    for result in results:
        recipe = result['recipe']

        if dietary == "No dietary requirements" or dietary == "Select dietary requirement":    # append all results if no dietary requirements or no selection
            ret_recipes.append(recipe)

        elif dietary in recipe['healthLabels']:     # only append suitable results for specific dietary
            ret_recipes.append(recipe)

        else:                                       # else, the list remains empty
            continue

    print('There are {} results'.format(len(ret_recipes)))                        # print number of recipes returned to the console and tkinter window
    info.insert(tk.END, 'There are {} results'.format(len(ret_recipes)) + "\n")

    if len(ret_recipes) != 0:                                   # if ret_recipes is NOT empty, then:
        file = open("recipes.txt", "w+")                         # open the recipes.txt file to write to it

        for ret_recipe in ret_recipes:
            info.insert(tk.END, ret_recipe['label'] + "\n")
            info.insert(tk.END, "\t" + ret_recipe["url"] + "\n")
            info.insert(tk.END, '\t' + 'Cuisine: {}'.format(" ".join(ret_recipe['cuisineType'])).title() + '\n')
            info.insert(tk.END, '\t' + 'Meal: {}'.format(" ".join(ret_recipe['mealType'])).title() + '\n')        # Display title, url, meal type and cuisine in window
            file.write("\n" + ret_recipe['label'] + "\n")
            file.write("\t" + ret_recipe['url'] + "\n")
            for food in ret_recipe['ingredientLines']:
                file.write('-' + food + '\n')  # Save recipe name, url and list of ingredients to recipes.txt
            print(ret_recipe['label'])
            print(ret_recipe['healthLabels'])
            print(ret_recipe['url'])  # Print all titles, urls and healthLabels in the console


    if len(ret_recipes) > 0:     # only display message when the file has been written to
        file_label = tk.Label(window, text="Recipe details have been saved to the recipes.txt file", bg="#B7E5DD", pady=5)
        file_label.pack()


ingred_search_label = tk.Label(window, text="Enter ingredient:", bg="#B7E5DD", pady=5) # Instruction label
ingred_search_label.pack()
ingred_entry = tk.Entry(window) # Text can be entered here to specify the ingredient
ingred_entry.pack()

diets = ["No dietary requirements", "Vegetarian", "Gluten-Free", "Peanut-Free", "Egg-Free", "Fish-Free", "Dairy-Free", "Sugar-Conscious", "Pork-Free", "Red-Meat-Free", "Pescatarian"] # List for the drop-down box options
clicked = tk.StringVar() # The type of data to be stored
clicked.set("Select dietary requirement") # Default text that will show on the menu
drop = tk.OptionMenu(window, clicked, *diets) # The dropdown menu will display the diets list as clickable options
drop.pack()

search_button = tk.Button(window, text="Search recipes", highlightbackground="#ea86b6", command=run, padx=5, pady=5)
search_button.pack() # Creating a button to search for results which when clicked, triggers the run() function

window.mainloop()