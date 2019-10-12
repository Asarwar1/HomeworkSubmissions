## Unit 10.2 - Advanced Usage of the SQLAlchemy ORM

### Overview

Today's lesson introduces students to some more of the nitty-gritty details of working with the SQLAlchemy ORM, including how to create complex queries, update rows, perform joins, and use ORM methods to perform queries.

### Class Objectives

* Students will be able to use the SQLAlchemy ORM to create classes that model tables.

* Students will be able to perform database CRUD operations using the SQLAlchemy ORM.

* Students will be able to reflect existing databases.

* Students will be able to use the SQLAlchemy Inspector to view table names in the database.

* Students will be able to plot the query results from the ORM.

- - -

### Activities Preview

* **Shark Search**
* File/Instructions:

  * [sharks.sql](Activities/02-Stu_SharkSearch/Resources/sharks.sql)

  * [README](Activities/02-Stu_SharkSearch/README.md)

* **What a Cruddy Database**
* Instructions:

  * Within a Python file, create new SQLAlchemy class called `Garbage` that holds the following values...

    * `__tablename__`: Should be "garbage_collection"

    * `id`: The primary key for the table that is an integer and automatically increments

    * `item`: A string that describes what kind of item was collected

    * `weight`: A double that explains how heavy the item is

    * `collector`: A string that lets users know which garbage man collected the item

  * Create a connection and a session before adding a few items into the SQLite database crafted.

  * Update the values within at least two of the rows added to the table.

  * Delete the row with the lowest weight from the table.

  * Print out all of the data within the database.

  * Bonus: Modify the application so that items can be added, updated, queried, or removed according to user inputs.

* **Reflecting on SQL**
* File/Instructions:

  * [Activities/06-Stu_Reflecting/Resources/demographics.sqlite](Activities/06-Stu_ReflectingOnSQL/Resources/demographics.sqlite)

  * Create engine using the `demographics.sqlite` database file.

  * Declare a Base using `automap_base()` and use this new Base class to reflect the database's tables.

  * Assign the demographics table/class to a variable called `Demographics`.

  * Create a session and use this session to query the `Demographics` table and display the first five locations.

  * Bonus: Query and print the number of unique locations in the table.

  * Hint: For the bonus, look into counting and grouping operations in SQLAlchemy.

* **Salary Exploration**
* File/Instructions:

  * [database.sqlite](Activities/08-Stu_SalaryExplore/Resources/database.sqlite)

  * Using the attached SQLite file, use an inspector to collect the following information...

  * The names of all of the tables within the database.

  * The column names and data types for the `Salaries` table.

  * Reflect the database, create a session, and query the `Salaries` table to collect the number of salaries that are over 50k per year.

* **Emoji Plotting**
* File/Instructions:

  * [emoji.sqlite](Activities/09-Par_EmojiPlotting/Resources/emoji.sqlite)

  * Use the inspector to explore the database and print out the table names stored within it.

  * Using the inspector, print out the column names and types for each of the tables contained within the SQLite file.

  * Reflect the database into a SQLAlchemy class and start a session that can be used to query the database.

  * Using Matplotlib, create a horizontal bar chart and plot the emoji score in descending order. Use `emoji_char` as the y-axis labels and plot only the top 10 emojis ranked by score.

  * Create the same kind of chart using Pandas to plot the data instead of Matplotlib.

- - -

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
