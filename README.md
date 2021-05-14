# Analysis into Viability of Opening Bike Shop in Manhattan or DMV Area

042621NYCDS Phase 1 Final Project 

### Overview

With this analysis, we seek to identify parameters that will help us identify both a location and market to target with a new bike shop.

![City-street-bicycle-parking_1920x1200.jpg](https://raw.githubusercontent.com/ismizu/Phase_1_Project/main/images/City-street-bicycle-parking_1920x1200.jpg)

### Business Problem

The goal of the project is to determine an optimal location for bike shops between the Manhattan area in New York City and the DMV (Washington D.C., Maryland, and Virginia areas) as well as which segment of the market to target.

### Repository Structure

- The datasets that we utilized can be found in the /data folder.
- All visualizations can be found in the /images folder.
- All functions can be found in the helper_funcs.py file

### Big Questions

- Where should the business be located?
- Which segment of the market should we focus on?

### Analysis Focus

1. The analysis focused on yelp data pulled for the locations of the NYC and the DC area.
2. Our analysis of this data was primarily focused on price and review counts per location.

___

# Data Analysis 

___

### Data Imported from Yelp API Key

Utilizing various parameters, we gather and parse the results from Yelp before saving them to a csv file. Yelp limits API calls to return a maximum of fifty businesses per request. Therefore, we pass the functions through a loop that will continue until the appropriate number of businesses are gathered.

### Evaluating Our Data

We convert the price points to a value between one and four, with four being the most expensive. The percentages also factor out Yelp businesses that did not include a value for price.

![price_percentages.png](https://raw.githubusercontent.com/ismizu/Phase_1_Project/main/images/price_percentages.png)

Overall, the percentage of bike shops per price point is relatively similar for both locations. However, there is one notable difference. The DC area does not contain any bike shops within the highest price point. Based on this observation, a high-end bike shop in that area seems more favorable.

To further investigate this initial observation, we view the percentage of reviews that bike shops in both areas currently hold.

![review_percentages.png](https://raw.githubusercontent.com/ismizu/Phase_1_Project/main/images/review_percentages.png)

There are two observations that we observe in the above graph.
1. The DC area's ratings show a steady, upward trend, showing that bike shops are consistently rated at higher levels.
2. The NYC area's ratings are not consistent and shift in an unfavorable pattern. They have a much higher percentage of bike shops with a rating of 1. In addition, the number of bike shops with high ratings begin to cap off at the rating of 4 before decreasing.

This shows us that a higher percentage of bike shops in the DC area are seen favorably when compared to those in the NYC area. This further builds on our hypothesis that the DC area is better for our bike shop.

An additional consideration that we investigated was the availability of bike routes (denoted in blue lines) in the area as well as the location of bike shops along those paths.
First, we view the Manhanttan area.

![ny_bike.png](https://raw.githubusercontent.com/ismizu/Phase_1_Project/main/images/ny_bike.png)

From this map, it is clear that the area holds quite extensive bike routes. However, another notable observation is the concentration of bike shops surrounding them. Not only is there an extensive system of bike routes, but a flurry of bike shops along them. This brings into question how well a new bike shop might do, considering the competition it would face.

Seeing this, we now observe the DC area.

![dc_bike_map.png](https://raw.githubusercontent.com/ismizu/Phase_1_Project/main/images/dc_bike_map.png)

In a similar vein, the DC area contains an extensive network of bike routes. However, one notable difference is the lower concentration of bike shops. Compared to our mapping of the NYC area, DC contains a considerably lower availability of bike shops.

___

# <center> Final Analysis </center>

___

Thus far, the DC area shows more favorable results based on our analysis of the average ratings, available price points, and concentration of current shops.
However, in choosing to target the high-end market, we also observe the relation between price and ratings.

![price_vs_rating.png](https://raw.githubusercontent.com/ismizu/Phase_1_Project/main/images/price_vs_rating.png)

Here, we observe a negative trend between the price point and average rating. As the price point increases, the average review falls.

Without data on bike shops in DC with a price level of four, we can only assume that the DMV will continue this trend. We hypothesize that the reason for this trend is that wealthier customers tend to be more discerning and therefore demand a higher quality experience. However, we cannot make any concrete conclusions due to a lack of available data. What is notable is the trend's consistency between the available NY and DMV data. As such, with all other results pointing in the direction of the DC high-end market, we choose to target this market.

## Summary

- The lower to mid-tier market seems to be well serviced in Washington DC whereas there appears to be a gap in the market for high end premium bicycle stores.
- High end shoppers are likely more discerning and demand a superior shopping and customer service experience.

## Presentation Slides

[Presentation Slides](https://docs.google.com/presentation/d/1yTAREqBblU3qVb57jxPP8lo16aFZC9Sn9vWm6kTLmlA/edit?usp=sharing)

## Contributors

[Adam Cumurcu](https://github.com/AdamCumurcu)\
[Isana Mizuma](https://github.com/ismizu)
