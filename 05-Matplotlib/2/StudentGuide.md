## Unit 5.2 - Plotting With Pandas

### Overview

Today's lesson plan introduces students to Pandas plotting, a quick and effective means through which to create charts using DataFrames.

### Class Objectives

* Students will  feel comfortable creating plots using the `DataFrame.plot()` method

* Students will understand the advantages and disadvantages of creating charts using the `DataFrame.plot()` method.

* Students will  be able to work their way through a complex data set using Pandas and then chart some visualizations based upon the cleaned DataFrame.

- - -

### Activities Preview

* **PyPlot Warmup**

* File/Instructions:

  * [plot_drills.ipynb](Activities/01-Stu_PlotsReview/Unsolved/plot_drills.ipynb)

  * What kinds of plots match the datasets below?

  ```
  # DATASET 1
  gyms = ["Crunch", "Planet Fitness", "NY Sports Club", "Rickie's Gym"]
  members = [49, 92, 84, 53]

  # DATASET 2
  x_lim = 2 * np.pi
  x_axis = np.arange(0, x_lim, 0.1)
  sin = np.sin(x_axis)

  # DATASET 3
  gyms = ["Crunch", "Planet Fitness", "NY Sports Club", "Rickie's Gym"]
  members = [49, 92, 84, 53]
  colors = ["yellowgreen", "red", "lightcoral", "lightskyblue"]
  explode = (0, 0.05, 0, 0)

  # DATASET 4
  x_axis = np.arange(0, 10, 0.1)
  x_axis = np.arange(0, 10, 0.1)
  times = []
  for x in x_axis:
    times.append(x * x + np.random.randint(0, np.ceil(max(x_axis))))
  ```

  * Create a plot for each of the datasets above, making certain to provide each chart with a title and labels

* **Battling Kings**

* Files/Instructions:

  * [battling_kings.ipynb](Activities/03-Stu_BattlingKings/Unsolved/battling_kings.ipynb)

  * [got.csv](Activities/03-Stu_BattlingKings/Unsolved/Resources/got.csv)

  * Use Pandas to load the `got.csv` data set.

  * Create a Series containing the number of times each king was an attacker.

  * Create a Series containing the number of times each king was a defender.

  * Combine these two variables into a single Series. _Hint_: How should you combine these two Series? Can you add Series in Pandas?

  * Use your combined data to retrieve labels for your x-ticks.

  * Create a red bar chart, and set its x-tick labels appropriately.

  * Add a title and labels to your plot.

  * Display your plot. Who participated in the most battles? The least?

* **Bike Trippin**

* Files/Instructions:

  * [bike_trippin.ipynb](Activities/05-Stu_BikeTrippin/Unsolved/bike_trippin.ipynb)

  * [trip.csv](Activities/05-Stu_BikeTrippin/Resources/trip.csv)

  * Create a bar chart using Pandas and MatplotLib that visualizes how many individual bike trips were taken by each gender.

  * Create a pie graph using Pandas and MatplotLib that can be used to visualize the trip duration of a single bike split up by gender.

  * Hint: There is a buggy value stored within the "gender" column of the original DataFrame. In order to create an accurate chart, this value will need to be found and removed.

* **Miles Per Gallon**

* Files/Instructions:

  * [mpg.ipynb](Activities/06-Stu_MilesPerGallon/Solved/mpg.ipynb)

  * [MPG.csv](Activities/06-Stu_MilesPerGallon/Resources/mpg.csv)

  * Create a scatter plot using the data provided, Pandas, and MatplotLib which compares the MPG of a vehicle with its horsepower.

* **Winner Wrestling**

* Files/Instructions:

  * The rest of class will be dedicated to creating a plot using Pandas and MatplotLib that allows its viewers to visualize the recent career of professional wrestlers.

  * This mini-project has been broken down into three parts and was designed to work alongside each other in groups.

  * In this first part, students will take four separate CSV files and merge them together. They will then need to rename and style the columns so that they reflect the data properly.

  * In the second part, groups will create new columns for their DataFrame which will inform readers of how many matches a wrestler has won, lost, drawn, and taken part in over the course of their career.

  * In the final part, the class will take the DataFrame they created and, using MatplotLib, chart the number of wins and losses an individual wrestler had over the course of their recent career.

  * The instructions for each part are contained in the corresponding unsolved Jupyter notebook file.

  * [winning_wrestlers.ipynb](Activities/08-Stu_WinnerWrestling-Part1/Solved/winning_wrestlers.ipynb)

  * [WWE-Data-2013.csv](Activities/08-Stu_WinnerWrestling-Part1/Resources/WWE-Data-2013.csv)

  * [WWE-Data-2014.csv](Activities/08-Stu_WinnerWrestling-Part1/Resources/WWE-Data-2014.csv)

  * [WWE-Data-2015.csv](Activities/08-Stu_WinnerWrestling-Part1/Resources/WWE-Data-2015.csv)

  * [WWE-Data-2016.csv](Activities/08-Stu_WinnerWrestling-Part1/Resources/WWE-Data-2016.csv)

  * [winning_wrestlers.ipynb](Activities/10-Stu_WinnerWrestling-Part2/Solved/winning_wrestlers.ipynb)

  * [WWE-Data-2013.csv](Activities/10-Stu_WinnerWrestling-Part2/Resources/WWE-Data-2013.csv)
  
  * [WWE-Data-2014.csv](Activities/10-Stu_WinnerWrestling-Part2/Resources/WWE-Data-2014.csv)
  
  * [WWE-Data-2015.csv](Activities/10-Stu_WinnerWrestling-Part2/Resources/WWE-Data-2015.csv)
  
  * [WWE-Data-2016.csv](Activities/10-Stu_WinnerWrestling-Part2/Resources/WWE-Data-2016.csv)

  * [winning_wrestlers.ipynb](Activities/10-Stu_WinnerWrestling-Part3/Solved/winning_wrestlers.ipynb)

  * [WWE-Data-2013.csv](Activities/10-Stu_WinnerWrestling-Part3/Resources/WWE-Data-2013.csv)
  
  * [WWE-Data-2014.csv](Activities/10-Stu_WinnerWrestling-Part3/Resources/WWE-Data-2014.csv)
  
  * [WWE-Data-2015.csv](Activities/10-Stu_WinnerWrestling-Part3/Resources/WWE-Data-2015.csv)
  
  * [WWE-Data-2016.csv](Activities/10-Stu_WinnerWrestling-Part3/Resources/WWE-Data-2016.csv)

- - -

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
