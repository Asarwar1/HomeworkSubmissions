## Unit 6.1 - APIs

### Overview

Today's lesson introduces students to JSON traversal and the fundamentals of making API requests with the [requests library](http://docs.python-requests.org/en/master/), using the [OMDb](https://www.omdbapi.com/) and [New York Times](https://developer.nytimes.com/) APIs.

### Class Objectives

* Students will be able to make GET requests with `requests`.

* Students will be able to convert JSON into a Python dictionary.

* Students will read and apply API documentation.

* Students will sign up for and use an API key.

- - -

### Activities Preview

* **Requesting SpaceX**
* File/Instructions:

  * [02-Stu_SpaceX/Stu_SpaceX.ipynb](Activities/02-Stu_SpaceX/Unsolved/Stu_SpaceX.ipynb)
  
  * [Activities/02-Stu_SpaceX/README.md](Activities/02-Stu_SpaceX/README.md)

  * Take a few minutes to explore the SpaceX API: <https://github.com/r-spacex/SpaceX-API/wiki>

  * Once you understand the structure of the API and its endpoint, choose one of the endpoints and do the following:

  * Retrieve and print the JSON for _all_ of the records from your chosen endpoint.

  * Retrieve and print the JSON for a _specific_ record from your chosen endpoint.

* **Requesting a Galaxy Far Far Away**
* File/Instructions:

  * [Stu_FarFarAway.ipynb](Activities/04-Stu_FarFarAway/Unsolved/Stu_FarFarAway.ipynb)

  * [04-Stu_FarFarAway/README.md](Activities/04-Stu_FarFarAway/README.md)

  * Using the starter file provided, collect the following pieces of information from the Star Wars API.

  * The name of the character

  * The number of films they were in

  * The name of their first starship

  * Once the data has been collected, print it out to the console.

  * Hints:

    * It would be in the programmer's best interest to print out the JSON from the initial request before anything else. This will let them know what keys they should reference.

    * The "starship" values are links to another API call. This means that the programmer will need to create a request based off of the values of a previous request.

  * Bonus: Come up with a way in which to collect and print out all of the film names a character was in.

* **Number Facts**
* File/Instructions:

  * [05-Par_NumberFacts/Par_NumberFacts.ipynb](Activities/05-Par_NumberFacts/Unsolved/Par_NumberFacts.ipynb)
  
  * [05-Par_NumberFacts/README.md](Activities/05-Par_NumberFacts/README.md)

  * Using the [Numbers API](http://numbersapi.com), create an application that takes in a user's inputs and returns a number fact based upon it.

  * Hints:

    * The URL to make your request to must have `?json` at its end so that the data format returned is JSON. The default response for this API is pure text.

    * Make sure to read through the documentation when creating your application. Some types require more or less data than others.

* **Study the OMDb API**
* Instructions:

  * Read the OMDb documentation, and make a few API calls to get some information about your favorite movie.

  * You are free to duplicate the demonstration from earlier or explore more freely as you wish. Just be sure to print two or three properties of the JSON you retrieve.

* **Movie Questions**
* File/Instructions:

  * [08-Stu_MovieQuestions/Stu_MovieQuestions.ipynb](Activities/08-Stu_MovieQuestions/Unsolved/Stu_MovieQuestions.ipynb)
  
  * [08-Stu_MovieQuestions/README.md](Activities/08-Stu_MovieQuestions/README.md)

  * Use the OMDb API to retrieve and print the following information.

  * Who was the director of the movie **Aliens**?

  * What was the movie **Gladiator** rated?

  * What year was **50 First Dates** released?

  * Who wrote **Moana**?

  * What was the plot of the movie **Sing**?

* **Iterative Requests**
* File/Instructions:

  * [10-Stu_MovieLoop/Stu_MovieLoop.ipynb](Activities/10-Stu_MovieLoop/Unsolved/Stu_MovieLoop.ipynb)
  
  * [10-Stu_MovieLoop/README.md](Activities/10-Stu_MovieLoop/README.md)

  * Consider the following list of movie titles.

    ```python
    movies = ["Aliens", "Sing", "Moana"]
    ```

  * Make a request to the OMDb API for each movie in the list. Then:

    1. Print the director of each movie

    2. Save the responses in another list

* **Retrieving Articles**
* File/Instructions:

  * [12-Stu_RetrieveArticles/Stu_Retrieve_Articles.ipynb](Activities/12-Stu_RetrieveArticles/Unsolved/Stu_Retrieve_Articles.ipynb)
  
  * [12-Stu_RetrieveArticles/README.md](Activities/12-Stu_RetrieveArticles/README.md)

  * Save the NYT API endpoint to a variable. Make sure you include the right query parameter to retrieve JSON data!

  * Register for and save your API Key to a variable.

  * Decide on a search term, and save it to a variable.

  * Limit your search to articles published within a range of dates—for example, only articles published in 2014. _Hint_: Read the documentation on `end_date`.

  * Build your query URL, and save it to a variable.

  * Retrieve your list of articles with a GET request.

  * Take a look at the documentation. How do you get ahold of the articles in the response?

  * Store each article in the response inside of a list.

  * Print a `snippet` from each article.

  * As a bonus, try to figure out how we could get 30 results. _Hint_: Look up the `page` query parameter. If you get a message saying you've exceeded your rate limit, don't fret—you've solved the problem.

- - -

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
