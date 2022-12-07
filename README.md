# OutfitApp

this application generates outfits for users based on clothing they upload and was developed in Python, 
JavaScript, and HTML with the Flask framework and contains two distinctive pages, an add page (which we are
currently on) and a generate page.

The add page is extremely intuitive for the user thanks to a machine learning model that I developed in Python with
the TensorFlow library that classifies images users upload into several distincitive categories of clothing. However, if the
model is below a certain confidence level, the application prompts the user to manually enter the item's category. After an
item is added, it is stored on a SQL database.

When we move to the generate page, we are prompted for a location and days of our trip before receiving potential
outfit recommendations. The program has a sizeable room for improvement and optimization, I have developed a 
web scraper that retrieves the weather of the location that the user inputted along with dominant-color recognition
functionality in order to potentially make the recommendations weather-observant and color-coordinated.
