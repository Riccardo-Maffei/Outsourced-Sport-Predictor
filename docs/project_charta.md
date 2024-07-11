# `Outsourced Sport Predictor` - Project Charta

## Problem Definition
Sports betting is an increasingly popular form of gambling for the world. The problem is, just like all forms of gambling, most users have a difficult time making a profit from sports betting. By making a prediction model that uses real and relevant data, we can make sports betting a safer activity for many users. Almost everyone involved in sports betting lose money in the process, often because of uninformed or biased decisions. This prediction model will undermine those decision problems for gamblers ...

## Situation Assessment
**Personnel:**
- 4 Computer Science college students

**Material:**
- Computational Hardware: High-performance servers and cloud infrastructure for model training and deployment.
- Data: Real-time sports data, including player statistics, team performance, weather conditions, and other relevant factors.
- Data Processing: Python and SQLite for data manipulation and analysis.
- Machine Learning Frameworks: TensorFlow, scikit-learn for building and training data models.
- Data Visualization: DBVisualizer, streamlit for database visualization and web development
- Version Control: Git for tracking changes and collaboration.

**Infrastructure:**
- Data Storage: SQLite for database development and storage
- Development Environment: Integrated Development Environments (IDEs) like PyCharm and Visual Studio Code.

**Project Timeline:** 2 weeks

## Project Goals and Success Criteria
The project is successful from a stakeholder perspective if they are able to win more bets with the prediction model compared to using just their own decisions.

We specifically wanted to focus on European soccer predictions, such that the scope of the project did not become too big. We also excluded doing predictions or analysis of other game statistics such as player statistics or other in-game events, as we wanted to specifically focus on the result of the games.

## Data Mining Goals
When we collected the datasets to be used in the model, we ultimately wanted to see a correlation between the players/combinations of players on a team and the likelihood of that team winning a match. In other words, we wanted to see an association between the result of a match and the players that were participating on each side.

## Project Plan
```gantt
    Title: Gantt Diagram for Sports Prediction Model
    dateFormat 2024-07-01
    tickInterval 1day
    section Project Understanding
        Define problem,     :a1, 2024-07-01, 1d
        Determine project goals     :a2, 2024-07-01, 1d
        List available resources     :a3, 2024-07-02, 1d
        Set data mining goals    :a4, 2024-07-03, 1d
        Create project plan    :a5, 2024-07-03, 1d
        Project checkpoint: milestone, m1, 2024-07-04, 4m
    section Data Acquisition and Exploration
        Acquire data :a6, 2024-07-03, 3d 
        Exploratory data analysis   :a7, 2024-07-04, 3d
        
    Data Saving and transforming
	Data base creation 2024-07-05, 2d
	DATA PROCESSING 2024-07-07, 2d
    section Modelling
        Create initial model   :a8, 2024-07-10, 1d
        Additional feature engineering :a9, 2024-07-10, 1d
        Prepare modelling report :a10, 2024-07-10, 2h
    section Evaluation
        Prepare presentation :a10, 2024-07-10, 2h
        Project presentation : milestone, m2, 2024-07-11, 4m
```

## Contact Details
- **Harrison Waldon** - waldonh@mail.gvsu.edu
- **Piotr Salustowicz** - saluspio@students.zhaw.ch
- **Connor VanDrunen** - vandrunc@mail.gvsu.edu
- **Riccardo Maffei** - mafferic@students.zhaw.ch
