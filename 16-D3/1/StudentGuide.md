## Unit 16.1 - Intro to D3 Graphing

### Overview

In today's class, students will expand upon their knowledge of the D3 library and start building bar charts.

### Class Objectives

* Students will gain a high-level understanding of SVG elements and how to append/modify them using D3.

* Students will understand how to bind data to SVG elements using D3 so as to create basic bar charts from scratch.

* Students will create a bar chart with axes using D3 so as to visualize data.

- - -

### Activities Preview

* **Talk about D3**
* Try answering the following:

  1. What does D3 stand for?
  2. What language is D3 written in?
  3. What are some examples of types of charts that can be created with D3?
  4. What are some of D3's features?

* **D3 Table**
* Files/Instructions:

  * [index.html](Activities/03-Stu_D3_Table/Unsolved/index.html)

  * [table.js](Activities/03-Stu_D3_Table/Unsolved/table.js)

  * Use the starter code provided to create a table using D3 data binding.

  * Your code should use D3 data binding to create a table from the `austin_weather` data provided.
  
  * Hint: Use the `.html()` method to add several `td` elements inside each table row.

* **SVG Stickman**
* Instructions:

  * Create a new html file, then use SVG shapes to draw an SVG Stickman.

  * Hint: [SVG Shape Reference](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Basic_Shapes)

* **Data Rectangles**
* Files/Instructions:

  * [index.html](Activities/08-Stu_Data_Rectangles/Unsolved/index.html)

  * [app.js](Activities/08-Stu_Data_Rectangles/Unsolved/app.js)

  * [style.css](Activities/08-Stu_Data_Rectangles/Unsolved/style.css)

  * [README.md](Activities/08-Stu_Data_Rectangles/README.md)

  * Use the given javascript file and D3 to accomplish this following.

    1. Append an `SVG` element to the div provided in the starter html file. The SVG element should have a width of 600 px and a height of 400 px. Create a variable to reference this element.

    2. Bind the data from the given `booksReadThisYear` array and append a rectangle with a height ten times the value of the the item in the array.

  * Bonus: Using the given css file, change your javascript so that when you hover over the rectangle it changes color.

* **Upside Down Bar Chart**
* Files/Instructions:

  * [index.html](Activities/09-Stu_UpsideDownBarChart/Unsolved/index.html)

  * [app.js](Activities/09-Stu_UpsideDownBarChart/Unsolved/app.js)

  * Add code to [app.js](Activities/09-Stu_UpsideDownBarChart/Unsolved/app.js) in order to complete a bar chart using data binding.

  * Position and style each bar based on the data it represents.

  * Bonus:

    * So far we have been making vertical bar charts exclusively... But we could also apply what we have learned thus far to making horizontal bar charts! Using your newfound knowledge of data-binding and graphing using D3, see if you can create a horizontal bar chart!

    * Since the next step in creating bar charts is to flip them right-side-up, experiment with your code a little bit and see if you can figure out how to manage this.

  * Hints:

    * Look at the previous activities for reference!

    * See this [article on data-joins with D3](https://bost.ocks.org/mike/join/), written by D3 creator, Mike Bostock.

- - -

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
