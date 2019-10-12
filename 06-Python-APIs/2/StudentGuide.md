## Unit 6.2 - Working with Weather & City APIs

### Overview

Today's class introduces the class to a number of new APIs whilst also discussing API wrappers, exception handling, and using Pandas with API responses.

### Class Objectives

* Students will create applications from scratch using nothing but their knowledge of Python and an API documentation
* Students will load JSON from API responses into a Pandas DataFrame
* Students will be able to use `try` and `except` blocks to handle errors

- - -

### Activities Preview

* **JSON Traversal**
* Files/Instructions:

  * [youtube_response.json](Activities/01-Stu_JSONTraversalReview/Resources/youtube_response.json)

  * [Stu_JSON_Traversal.ipynb](Activities/01-Stu_JSONTraversalReview/Unsolved/Stu_JSON_Traversal.ipynb)
  
  * [Activities/README.md](Activities/01-Stu_JSONTraversalReview/README.md)

  * Load the provided JSON file.

  * Retrieve the video's title.

  * Retrieve the video's rating.

  * Retrieve the link to the video's thumbnail.

  * Retrieve the number of views.

    * Hints: In order to load in the data from an external JSON file, simply import the `json` library before using the `json.open(<FILE PATH>)` and `json.load(<JSON VARIABLE>)` methods.

* **Requests Review**
* File/Instructions:

  * [Stu_RequestReview.ipynb](Activities/02-Stu_RequestReview/Unsolved/Stu_RequestReview.ipynb)
  
  * [02-Stu_RequestReview/README.md](Activities/02-Stu_RequestReview/README.md)

  * Make a request to the following endpoint [http://nyt-mongo-scraper.herokuapp.com/api/headlines](http://nyt-mongo-scraper.herokuapp.com/api/headlines) and store the response.

  * JSON-ify the response.

  * Print the JSON representations of the first and last posts.

  * Print number of posts received.

* **Weather in Burundi**
* File/Instructions:

  * [Stu_Burundi.ipynb](Activities/04-Stu_Burundi/Unsolved/Stu_Burundi.ipynb)
  
  * [04-Stu_Burundi/README.md](Activities/04-Stu_Burundi/README.md)

  * Save all of your "config" information within some variables. This includes your API key, the base URL, and the query terms desired.

  * Build your query URL. Check the documentation to figure out how to request temperatures in Celsius.

  * Make your request and save the API response.

  * Retrieve the current temperature in Burundi from the JSON response.

  * Print the temperature to the console.

    * Hint: You can find the [OpenWeatherMap Documentation](https://openweathermap.org/current) using the link provided.

    * Bonus: Augment your code to report the temperature in both Fahrenheit and Celsius.

* **TV Ratings**
* File/Instructions:

  * [Stu_TVRatings.ipynb](Activities/06-Stu_TVRatings/Unsolved/Stu_TVRatings.ipynb)
  
  * [06-Stu_TVRatings/README.md](Activities/06-Stu_TVRatings/README.md)

  * You may use the list provided in the starter file or create your own.

  * Request information from the TVmaze API Show Search endpoint (<https://www.tvmaze.com/api#show-search>) on each show and store the name and rating information into lists.

  * Put this data into a dictionary, and load that dict into a Pandas DataFrame.

  * Use matplotlib to create a bar chart comparing the ratings of each show.

* **Making Exceptions**
* File/Instructions:

  * [08-Stu_MakingExceptions/Stu_MakingExceptions.ipynb](Activities/08-Stu_MakingExceptions/Unsolved/Stu_MakingExceptions.ipynb)
  
  * [08-Stu_MakingExceptions/README.md](Activities/08-Stu_MakingExceptions/README.md)

  * Without removing any of the lines from the starter code provided, create `try` and `except` blocks that will allow the application to run without terminating.

* **Map Wrap**
* Files/Instructions:

  * [cities.csv](Activities/10-Stu_MapWrap/Resources/cities.csv)
  
  * [10-Stu_MapWrap/README.md](Activities/10-Stu_MapWrap/README.md)

  * Install the Openweathermapy API wrapper.

  * Read in the cities.csv using the Python CSV library in order to create a list of cities.

  * Create a settings dictionary with your API key and the preferred units of measurement.

  * Get data for each city that is listed within `cities.csv`.

  * Create a list to get the temperature, latitude, and longitude in each city.

  * Create a Pandas DataFrame with the results.

  * Print your summaries to verify that everything went smoothly.

  * Hints:

    * Don't forget to utilize the Openweathermapy documentation where needed: <http://openweathermapy.readthedocs.io/en/latest/>

    * We used the Python CSV library heavily in Week 3.  You can see the documentation for that library at <https://docs.python.org/3.7/library/csv.html>.

  * Bonus:

    * If you finish early, the `*` syntax should be reviewed.

    * Pass a `columns` parameter to `pd.DataFrame` to provide labels for the temperature and coordinate data.

* **Two Calls**
* File/Instructions:

  * [Stu_TwoCalls.ipynb](Activities/12-Stu_TwoCalls/Unsolved/Stu_TwoCalls.ipynb)
  
  * [12-Stu_TwoCalls/README.md](Activities/12-Stu_TwoCalls/README.md)

  * Retrieve a list of the lending types the world bank keeps track of, extract the ID key from each of them, and store all IDs in a list.

  * Next, determine how many countries are categorized under each lending type and store this data in a dictionary using the ID as the key and the count as the value.

    * The data for number of countries is stored in the first element of the response list.

  * Finally, print the number of countries of each lending type.

- - -

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
