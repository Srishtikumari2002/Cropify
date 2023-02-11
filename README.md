# Cropify - Crop Predictor Tool

## Introduction
A crop predictor is a tool that utilizes AI algorithms and data analysis to predict the crop best suited for given weather data, soil conditions, and other relevant factors. The goal of this technology is to help farmers make more informed decisions about which crops to grow. This might save farmers money on fertilizer while also avoiding the risky practice of cultivating the same crops on the same plot of land over and over, depleting the soil of its natural resources.
<br>
Overall, the use of a crop prediction model can have a significant impact on the success and profitability of a farm. By providing farmers with the information they need to make informed decisions, this technology has the potential to increase crop yields, reduce costs, and minimize risks. As such, it is an essential tool for modern agriculture and a valuable resource for farmers looking to maximize their returns.

## Methodology
Our project uses a combination of machine learning models, including Support Vector Regression and Random Forest Regressor, to predict the following using datasets obtained from various sources, including Kaggle:
* Rainfall
* Temperature
* Crop prediction
* Crop production yield
We have also used an OpenWeatherMap API to get the humidity data of a particular location as it was not in the given dataset. 

## Flow of the code

## Results
* Testing accuracy of 80% for rainfall and temperature prediction.
* Testing accuracy of 25% for crop production yield prediction.
*  Testing accuracy of 99% for crop prediction based on geolocation and season.
* Room for improvement and we are actively working to improve the accuracy of our model.

## Constraints
* Currently, our model can predict the temperature of 8 cities. Therefore our crop prediction model can also only predict for 8 locations.
* Insufficient data for N, K, and P composition for different locations.
* The free package of OpenWeatherMap api only allows weather for the next 8 days from the current datetime.
* Insufficient data to predict the yield of the predicted crops.
* Insufficient data to predict the selling price of the predicted crops.

## Future Work
* Incorporate satellite images of the land in our model and use Convolutional Neural Network to improve the accuracy of our predictions.
* Implement a disease prediction feature to help farmers identify potential threats to their crops.

## Conclusion
We believe that our project has the potential to revolutionize the way farmers make decisions about what to grow in their fields. We hope that our project will provide farmers with the information they need to make informed decisions and maximize their profits.

## Contributors
Srishti
<br>
Pratyaksha
<br>
Radha
