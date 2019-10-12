## Unit 15.1 - Introduction to Plotly.js

### Overview

Today's lesson plan introduces students to [Plotly.js](https://plot.ly/javascript/), a high-level wrapper around d3.js.

### Class Objectives

* Students will be able to use arrow functions, `.map()`, and `forEach()` for data manipulation.

* Students will learn to use Plotly to create the fundamental charts: Box, scatter, bar, pie, and line plots.

* Students will use Plotly's `layout` object to customize the appearance of their charts.

* Students will annotate charts with labels; text; and hover info.

- - -

### Activities Preview

* **A Flicker of the Eye**
* Files: [Activities/03-Stu_First_Chart/Unsolved](Activities/03-Stu_First_Chart/Unsolved)

* **Multiple Traces**
* Files/Instructions:

  * [Activities/05-Stu_Multi_Trace/Unsolved](Activities/05-Stu_Multi_Trace/Unsolved)

  * In ancient Rome, their gods were often counterparts or imports of Greek gods. For example, the Greek god Zeus became in Rome Jupiter via an etymological transformation from Zeus to Zeus Pater ("Father Zeus") to Iupiter (classical Latin lacked a "J" consonant).

  * In today's world, are these gods better known by their Roman names or Greek names? To answer this question, your task is to plot the number of search results, of both Roman and Greek names, returned for each god.

  * To accomplish this task, you will need to create two traces, one for Roman gods, and another for Greek gods.

  * In order to define the data for each plot point in a trace, use the `map()` method on the dataset.

  * Examine `data.js` to determine how you will do this.

* **Horizontal Bar Chart**
* Files/Instructions:

  * [index.html](Activities/07-Stu_HBar/Unsolved/index.html)

  * [plots.js](Activities/07-Stu_HBar/Unsolved/plots.js)

  * [data.js](Activities/07-Stu_HBar/Unsolved/data.js)

  * Sort the data array of objects by `greekSearchResults`.

  * Slice the top 10 objects from the array.

  * Create a horizontal bar chart that plots the top 10 greek gods based on their search results in descending order.
  
  * Hints:

    * Use the following links to help you figure out how to sort the array of objects by the `greekSearchResults` values.

      * [Stackoverflow sorting objects](https://stackoverflow.com/a/979289)

      * [mdn docs on the sort function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

    * After sorting, slice the first 10 objects for your plots.

      * [mdn docs on the slice function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)

* **Scatter Plots**
* Files/Instructions:

  * [plots.js](Activities/08-Stu_Scatter/Unsolved/plots.js)

  * [data.js](Activities/08-Stu_Scatter/Unsolved/data.js)

  * [index.html](Activities/08-Stu_Scatter/Unsolved/index.html)

  * Alter the html to incorporate a div to hold you plot as well as the script tags to incorporate `data.js` and `plot.js` files.

  * Create a scatter plot to plot the `high_jump`, `discus_throw`, and `long_jump` vs the `year`.

  * Use three separate traces for this data.
  
  * Bonus: Customize the marker colors and symbol for each trace.


- - -

### Copyright

Trilogy Education Services © 2019 All Rights Reserved.
