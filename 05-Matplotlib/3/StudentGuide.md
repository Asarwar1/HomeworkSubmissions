## Unit 5.3 - Introduction to Statistics

### Overview

Today's class formally treats a number of topics from basic statistics, including measures of central tendency; variance; standard errors; and error bars.

### Class Objectives

* Students will be able to define **mean**, **median**, and **mode**, and choose which one is most appropriate to describe a given data set.

* Students will be able to explain the meaning of variance and standard deviation.

* Students will be able to describe standard error and the difference between a sample and a population.

* Students will be able to add error bars to their plots.

* Students will be able to fit lines to their data.

- - -

### Activities Preview

* **Handling Outliers**

* Files/Instructions:

  * [README](Activities/04-Stu_Quartiles_and_Outliers/README.md).

  * [04-Stu_Quartiles_and_Outliers/quartile_outliers.ipynb](Activities/04-Stu_Quartiles_and_Outliers/Unsolved/quartile_outliers.ipynb)

  * [04-Stu_Quartiles_and_Outliers/stats.py](Activities/04-Stu_Quartiles_and_Outliers/Unsolved/stats.py)

  * Take a look at the list in the in the `quartile_outliers` notebook. Identify the median, upper quartile, and lower quartiles by hand.

    * Use code to determine the lower and upper quartiles and be sure to account for both odd and even lengths of a data set.

    * Reference <https://en.wikipedia.org/wiki/Quartile> to choose a method for best handling this.

    * Use [numpy.percentile](https://het.as.utexas.edu/HET/Software/Numpy/reference/generated/numpy.percentile.html) to help with the calculations.

    * The difference between the upper and lower quartile is called the **interquartile range**, or IQR.

    * Like the standard deviation, the IQR describes how "spread out" the data set is.

    * Calculate the IQR for this list.

    * Determine the outliers

    * Lower outliers are points that fall below the result of the equation Q1 - 1.5 \* IQR

    * Upper outliers are points that above the result of the equation Q3 + 1.5 \* IQR

    * * Finally create a box plot of that data.

* **SEM and Error Bars**

* Files/Instructions:

    * [README](Activities/06-Stu_Standard_Error/README.md).

    * [06-Stu_Standard_Error/samples.ipynb](Activities/06-Stu_Standard_Error/Unsolved/samples.ipynb)

    * Open the starter file provided, and begin by inspecting the data. Which column contains house prices?

    * Create a number of samples of house prices.

        * If you work with the `sample.ipynb` file, this step is done for you.

    * Calculate the means for each sample.

    * Calculate the standard error for each sample.

    * Create a plot displaying the means for each sample, with the standard error as error bars.

* **Student's _t_-test**

* Files/Instructions:

  * [README.md](Activities/08-Stu_Students_t_test/README.md)

  * [wba_data.csv](Activities/08-Stu_Students_t_test/Resources/wba_data.csv)

  * [general_heights](Activities/08-Stu_Students_t_test/Resources/general_heights.csv)

  * Using the data, read both into a Pandas DataFrame.

  * Print the mean height of WBA players (last column in the DataFrame).

  * Print the mean height of women sampled.

  * Using a T-test, determine if difference in sample height means is significant or not and print a message stating the case.

  * Plot an error bar of the height means and include the standard error of the means.

  * Use an integer index starting at 0 for the X-axis and the list of means as the Y-axis.

* **Fits & Regression**

* Files/Instructions:

  * [README](Activities/10-Stu_Fits_and_Regression/README.md).

  * [crime_data.csv](Activities/10-Stu_Fits_and_Regression/Resources/crime_data.csv)

  * Import `stats` from the scipy module, along with `numpy` and `pandas`.

  * Use Pandas to read in the data.

  * Use `iloc` to isolate the year column.

  * Use `iloc` to isolate the total violent crime rate, murder rate, and aggravated assault rate columns.

  * Use `stats.linregress` to perform a linear regression with the year and violent crime rate columns.

  * Use `stats.linregress` to perform a linear regression with the year and murder rate columns.

  * Finally, use `stats.linregress` to perform a linear regression with the year and aggravated assault rate columns.

  * Use the information returned by `stats.linregress` to create an equation for a line describing each of the linear regressions you performed (see the hint below).

    * You should end up with three separate lines.

  * Use `subplots` to create a figure with subplots that share an x-axis.

  * Use `plot` to plot each of the lines you created against the year.

  * Display the plot.

  * Bonus: Use the line you created for the total violent crime rate to determine what the violent crime rate will be in 2019.

  * Hints:

    * See the documentation for [stats.linregress](https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.stats.linregress.html).

    * Recall that `stats.linregress` returns a slope, called `m`, and a y-intercept, called `b`. These let you define a line for each fit by simply writing: `fit = m * year + b`, for each linear regression you perform.

- - -

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
