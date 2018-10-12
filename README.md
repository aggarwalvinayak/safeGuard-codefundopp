# Submission of Idea for Code.fun.do++
## MOTIVATION
We see dozens of large scale natural disasters happening all over the world causing mass destruction of human life, manmade and natural property, it is our duty and responsibilty as a technologically advancing society to try to predict, attempt to prevent and manage support and help for the society in the case of such diasters using the up and coming fields of historical data analytics, prediction tools and modern day daily-use technologies.
## AIM
We are making an app/web-app interface that aims to cater to the populations specific to regions suffering from any natural disaster be it an earthquake, flood, tsunami or tornados. This app would have a **bi-ended approach** using an intensive rescuer and refugee side to the app and unique features adhereing to both these ends. It is our hope that using this app we could **optimise manpower** and **resource allocation** to a disaster affected societies and structure and stabilise help and rescue support to cater to those in its urgent need.  

## ASSUMPTIONS
We have to look at a set of assumptions taking into consideration our resources, availability of data and privacy of our users along with the technological limitations:
1. We need to assume that the rescuers(Government or army services, WHO, hospital services, refugee campers,etc.) have our app downloaded and are acquainted with the interface.
2. We also need to assume that our user end population suffering from the disaster has atleast SMS availability and has offline Google map on his device to figure out his/her location.
3. We need to assume that we have a number on which the disaster-ridden people will SMS their location such that rescuers can find them. 
4. We are assuming that shortest and safest paths can be trusted based on the live user and rescuer inputs based on moral hazards and asymmetric information transfer.

## KEY FEATURES
- We build a database based on the location data we receive from the sms' sent out by the people or which we receive from the user end of the app.
- We *cluster* the population density using k-means. 
- We optimally decide safe zones/Hotspots/Camps based on past disaster data, clustered population zones and the safety of a zone based on it's Altitude data, water level data and other quantitative parameters taken into consideration on the rescuer side of the application. 
- We decide red/danger zones based on data updated by both the users or rescuers if they see blockage or destruction of surroundings or routes. 
- We make a SOS/urgent rescue feature that caters to a proiority accidents or someone stuck in an emergency and it will be directly sent to the rescuers.
- We would build integration with a map services app which would help us marking unsafe zones, relief camps and safe routes for both the users as well as the rescuers. 
- The app would give directions, safe and short routes to the users as well as send an urgent evacuation notification to users stuck in highly unsafe locations.

## IMPLEMENTATION
- On the basis of the location data received by the people we would create a cluster of people in a diameter of about 5km. The stranded people would receive the location of nearest cluster center so that they can gather at a common point so that it makes easier for resecuers to reach them with a smaller manforce
- The common point of gathering would be decided by the rescuers with help from the prediction based on current population clusters, altitude and water level data and hotspots(hospitals,helipad, resources). 
- The SOS feature is for the people who are trapped and cannot reach the safe locations without help from the rescuers. There location would be directly sent to the rescue operations team for immediate action.

![dataflow](https://user-images.githubusercontent.com/31070834/46861178-ae6d8d00-ce2f-11e8-8116-1b597a0d5a7c.png)
#### Tech Stack
- Azure SQL Database
- Azure App Service
- Bing Maps API
- Django/ Flask FrameWork in Python for Web-App
- Scikit Learn/ PyTorch




