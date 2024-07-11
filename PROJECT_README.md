<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- Title -->
<div style="text-align: center;">
    <h1>
    OUTSOURCED TEAM
    </h1>
    <h2>
    SPORT PREDICTOR
    </h2>
</div>

## Table of contents

<!-- TOC -->
  * [Table of contents](#table-of-contents)
  * [About The Project](#about-the-project)
  * [Development](#development)
    * [Web Scraping](#web-scraping)
    * [Data Mining](#data-mining)
    * [Model Programming](#model-programming)
    * [Application Development](#application-development)
  * [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Model Creation](#model-creation)
    * [Web Application](#web-application)
  * [Usage](#usage)
  * [Roadmap](#roadmap)
  * [Sources](#sources)
<!-- TOC -->

<!-- ABOUT THE PROJECT -->
## About The Project

The main goal of the first two weeks of summer school was to develop a machine learning algorithm, 
which would solve a specific task. Multiple examples were given, for example a predictor for rent cost, 
a model that would recognise plants, etc.

The choice of the team was to develop a model that would return the outcome of a soccer match, 
when provided with the team composition and other conditions such as the referee, stadium, attendance, ...

This readme encapsulates the procedures the team went through to develop the model, as well as a guide to use it.

[Back To Table of Contents](#table-of-contents)

<!-- DEV -->
## Development

This section includes a short insight into the process of building the sports predictor model

### Web Scraping

The first task in the project development was retrieving the data. The team was split in two, 
with one group searching the web for an already prepared database to download, the other gathering
webpages with interesting data. After a list of potential webpages was made, the second team started scraping.
The data was mostly gathered from the official FIFA website and stored in csv files for later usage.

[Back To Table of Contents](#table-of-contents)

### Data Mining

While the second team was scraping the web, the first one searched it for downloadable, already organised databases. 
A very good one was found on [Kaggle](https://www.kaggle.com/datasets/davidcariboo/player-scores?resource=download) and
chosen as the major source of data for training the model.

[Back To Table of Contents](#table-of-contents)

### Model Programming

The first step for the programming of the predictor model was to clean up the data, 
for example by standardizing it, so that the model would be able to recognise all the inputs it was given.

After the cleanup, the amount of inputs and outputs were defined:

Inputs:
* Referee
* Stadium
* Competition Type
* Attendance

For 11 home players, 7 home reserves, 11 away players, 7 away reserves, 

* Home_Type
* Home_Position
* Home_Position_2
* Home_Sub_Position
* Home_Foot
* Home_Height
* Home_Rating
* Home_Age

Outputs:
* Goals for home Club
* Goals for away Club

The data was then split in training and test subsets, which allowed for a reliable
evaluation for the model predictions. After applying optimisers and loss functions,
multiple models were trained and evaluated. 
The one with the best accuracy was chosen for further use in the GUI Application

[Back To Table of Contents](#table-of-contents)

### Application Development

Another step in the development of our predictor was the creation of an interface, 
which would allow the user to easily enter the data for retrieving the prediction.
After considering various options, for example a JavaFX application, it was opted to use StreamLit.
This would allow for easy creation of a web application with great looking, modern graphics.


[Back To Table of Contents](#table-of-contents)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Ensure you have python installed on your machine
  ```sh
  python --version
  ```
If a version number is returned, skip the following passage, otherwise install python (including pip); 
depending on your OS, the installation steps may change.

Once you installed pip and python, install StreamLit
  ```sh
    pip install streamlit
  ```


### Model Creation

Once you cloned the repository, go to the 
[Kaggle Page](https://www.kaggle.com/datasets/davidcariboo/player-scores?resource=download) 
and download the Databank. Place the .csv files that were contained into the zip in the directory

"./Sports-Predictor/data_open/Transfermarket".

In order to create your own model, execute Files 1 - 9, located under 

"./Sports-Predictor/modelling/All Code and Data with Model and results".


[Back To Table of Contents](#table-of-contents)


### Web Application

To start the web application, simply path to the directory where the application python file is located. 
In this specific case, if not moved somewhere else by the user, the file is located under

"./Sports-Predictor/GUI/".

Once located in the correct directory, run the streamlit_GUI file with StreamLit

  ```sh
    streamlit run streamlit_GUI.py
  ```

This will start the application in the default browser. 
From there you will be able to enter the various parameters required by the model

[Back To Table of Contents](#table-of-contents)



<!-- USAGE EXAMPLES -->
## Usage

The first usage that comes up to mind is gambling. With accurate predictions, 
the probability of losing a bet significantly decreases. 
On the other hand, gamblers betting on the disadvantaged team will face increased rewards, 
in the case their team wins.

The predictor could also be used for training the football clubs. 
Since the model has extensive parameters, a coach could analyse the skills their players
have to improve, in order to increase the chances of success.

[Back To Table of Contents](#table-of-contents)



<!-- ROADMAP -->
## Roadmap

- [x] Scrape Data from the internet
- [x] Download already prepared Dataset from the internet 
- [x] Setup DataBank 
- [x] Create Machine Learning Model
- [x] Create User Interface to interact with the model
- [ ] Integrate Model in the User Interface

[Back To Table of Contents](#table-of-contents)


<!-- ACKNOWLEDGMENTS -->
## Sources

* [Football Data from Transfermarkt](https://www.kaggle.com/datasets/davidcariboo/player-scores?resource=download)
* [Readme Example](https://github.com/othneildrew/Best-README-Template)

[Back To Table of Contents](#table-of-contents)