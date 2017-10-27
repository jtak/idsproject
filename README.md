# Visualizing the air quality in the capital region

For programming we used Python, and especially Pandas was a very helpful tool. However, to cover what we wanted to do, we created a few useful tools to visualize and analyze the data we found.

### Tools 
* **average_weeks.py** , creates a representation for an average week from each month for every measurement station
* **day_averages.py** , creates a file for an average air quality value for each day
* **csv_exporter.py** , reads an excel file, cleans the air quality data inserted, and outputs a clean csv file that can later be analyzed/plotted
* **month_hour_analysis.py** , counts an average air quality value for each hour for every month 
* **normalize_daily_avgs.py** , normalizes the changes in the increases and decreases of the airquality, for one to observe the proportional change
* **plottingtrafficandairquality.py** , plots airquality with line plots and traffic amounts as barplots to the same plot, and exports the plot as a .png image
* **plottingweeklyaverageaq.py** , plots airquality with line plots, and exports the plot as a .png image. Can be also used to point out differences between working days and weeekends
* **split_weekends.py** , splits the data to working days and weekends for later manipulation.
* **traffic_quantities.py** , reads data from an excel file, chooses matching measurement stations, reshapes the data to match the accuracy of the air quality data. Finally saves a clean .csv file.
* **weekly_images.py** , visualizes the level of air quality on a map with color and size changing circles on a map. The larger the circle is, the more pollution there are. 


### Data sources

Data concerning the air quailty in the capital region :

https://www.hsy.fi/fi/asiantuntijalle/avoindata/Sivut/default.aspx#k=ilmanlaatuindeksit

Data concerning the air quailty in the capital region :

http://www.hri.fi/en/dataset/liikennemaarat-helsingissa

### Interesting topics that one could continue the study on

It would be interesting to investigate the level of air quality during for example,
  
* The New Year's eve
* The time around midsummer 

Also the effect of different weather factors and nearby power plants would be interesting to bring along to the study.

