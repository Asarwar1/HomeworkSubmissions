## Unit 12.3 - Rendering Your Data With Flask

### Overview

Today's class will introduce students to rendering templates with Flask, teaching them everything they need to know to display their data on a webpage.

### Class Objectives

* Students will become comfortable rendering templates with Flask using data retrieved from a Mongo database.

* Students will be able to use Beautiful Soup to scrape data

* Students will use PyMongo to save data to a Mongo database

* Students will use Flask to render templates

- - -

### Activities Preview

* **Rendering A String With Flask**
* Files/Instructions:

  * [02-Stu_Render_String/templates/index.html](Activities/02-Stu_Render_String/Unsolved/templates/index.html)

  * [02-Stu_Render_String/templates/bonus.html](Activities/02-Stu_Render_String/Unsolved/templates/bonus.html)

  * [02-Stu_Render_String/app.py](Activities/02-Stu_Render_String/Unsolved/app.py)

  * Create a webpage that will return a welcome message with a name returned from your flask app.

  * Add a paragraph underneath to display a hobby of your own; this will also be returned from the back end..

  * Create a link to a bonus page that routes you to an entirely new static html page and also returns both your name and hobby from the back end.

  * **Bonus**: Add a link back to the home page in your bonus page.

  * **Hints**: Consult the [Flask Render Docs](http://flask.pocoo.org/docs/0.12/quickstart/#rendering-templates) for reference.

* **Rendering A List**
* Files/Instructions:

  * [04-Stu_Render_List/index.html](Activities/04-Stu_Render_List/Unsolved/templates/index.html)

  * Create a web page that will display a list of your top five favorite movies.

  * Add style to your webpage by using [bootstrap cards](https://getbootstrap.com/docs/4.0/components/card/) add whatever info you like.

* **Rendering A Dictionary**
* Files/Instructions:

  * [06-Stu_Render_Dict/index.html](Activities/06-Stu_Render_Dict/Unsolved/templates/index.html)

  * [06-Stu_Render_Dict/app.py](Activities/06-Stu_Render_Dict/Unsolved/app.py)

  * Create a list of dictionaries that include the name and type of animal.

  * Loop through the list and display an un ordered list on the webpage.

  * Each line should include the name of the animal and type.

  * Add some CSS styling to each list item.

* **Rendering Data From Mongodb**
* Files/Instructions:

  * [10-Stu_Render_From_Mongo/app.py](Activities/08-Stu_Render_From_Mongo/Unsolved/app.py)

  * [10-Stu_Render_From_Mongo/template/index.html](Activities/08-Stu_Render_From_Mongo/Unsolved/templates/index.html)

  * Create a file called `insert_data.py` and setup a connection to mongo using pymongo.

  * Next, insert at least five store items that each include, type, cost, and stock into a mongo databases and collection.

  * Run the file (Why would we not want this in the app.py file?).

  * Setup a Flask app that makes a connection to the database and collection you created.

  * Return to a list of all the full inventory.

  * Display the type of item and cost of the item on the webpage.

  * **Bonus**: Display how much potential revenue (cost \* stock) would be made for each item.

  * **Hints**: Use [bootstrap cards](https://getbootstrap.com/docs/4.0/components/card/) to clean up the look.

* **Scrape and Render**
* Files/Instructions:

  * [10-Stu_Scrape_Weather/templates/index.html](Activities/10-Stu_Scrape_Weather/Unsolved/templates/index.html)

  * [10-Stu_Scrape_Weather/app.py](Activities/10-Stu_Scrape_Weather/Unsolved/app.py)

  * [10-Stu_Scrape_Weather/scrape_costa.py](Activities/10-Stu_Scrape_Weather/Unsolved/scrape_costa.py)

  * [10-Stu_Scrape_Weather/README.md](Activities/10-Stu_Scrape_Weather/README.md)

- - -

### Helpful terminal commands
* Find instances of Mongo `ps aux | grep mongod`
* Kill process `kill -9 [pid]`
* Drop Mongo Database `use <db name here>` then `db.runCommand( { dropDatabase: 1 } )`

- - -

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
