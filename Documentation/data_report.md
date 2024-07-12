# Outsourced Sport Predictor - Data Report


## Raw data
### Overview Raw Datasets
| Name | Quelle | Storage location |
|----------------|-----------------------------------------|--------------------------------------------------------------------------|
| Main Dataset | A collection of club football games and player data scraped off [transfermarkt](https://www.transfermarkt.com/) by David Cariboo. | [This Dataset is stored here on kaggle](https://www.kaggle.com/datasets/davidcariboo/player-scores?resource=download) |

### Main Dataset Details
This dataset contains multiple .csv files, including the scores, venues, referees, players, and player positions played for over 60,000 club games and over 30,000 players' heights, dominant feet, birth dates, red card records, and yellow card records. The data set was scraped off the website transfermarkt weekly by David Cariboo and posted on the website Kaggle. Transfermarkt is a website dedicated to compiling data on football games and football players. Kaggle is a website dedicated to providing computer scientists with tools and data sets to work with. To download this data, head to [this website](https://www.kaggle.com/datasets/davidcariboo/player-scores?resource=download), and click on the download button at the top of the page. On Kaggle, the dataset is listed with a CC0 license, making it available for public use. 

#### Data Catalog

To store this data in a database, we used the program SQLite.

#### Appearances Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 | appearance_id | Text | Two groups of numbers separated by an underscore, non-repeating | Numerical tag for identifying a unique appearance of a player  |
| 2 |  player_id | Integer | Min: 10 Max: 1.24 million  | Integer tag for identifying players across tables  |
| 3  | game_id  | Integer  | Min: 2.21 million Max: 4.35 million  | Integer tag for identifying games across tables  |
| 4  | player_club_id  | Integer  | Min: 1 Max: 102,000  | Integer tag for identifying a player's club ID in a given game across tables  |
| 5  | player_current_club_id  | Int | Min: -1 Max: 837,000 | Integer tag for identifying a player's current club ID across tables  |
| 6  | date  | Date  | Special Date type with the syntax YYYY/MM/DD | Date that the game stored in the game_id was played  |
| 7  | player_name  | Text |  In the syntax firstname lastname or lastname |  first and last name of the given player (player_id) if both names are available|
| 8  | competition_id  | Text | 3 to 4 letter abbreviation | Abbreviation tags storing the type of competition of the given game (game_id) to be used across tables |
| 9  | yellow_cards  | Integer | Min: 0 Max: 2  |  The amount of yellow cards the given player (player_id) received in the given game (game_id) |
| 10 | red_cards  | Integer | Min: 0 Max: 1 |  The amount of yellow cards the given player (player_id) received in the given game (game_id) |
| 11 | goals  | Integer | Min: 0 Max: 6  | The number of goals scored by the given player (player_id) in the given game (game_id)  |
| 12 | assists  | Integer | Min: 0 Max: 6  | The number of assists from the given player (player_id) in the given game (game_id) |
| 13 | minutes_played  | Integer  | Min: 1 Max: 135  | The amount of time the given player (player_id) played in the given game (game_id) |

#### Club Games Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 | game_id  | Integer | Min: 2.21 million Max: 4.35 million  | Integer tag for identifying games across tables  |
| 2 | club_id  | Integer | Min: 1 Max: 113,000  | Integer tag for identifying clubs across tables, in this case, club_id specifically refers to the home team |
| 3 | own_goals | Integer | Min: 0 Max: 19 | Integer value storing the number of goals scored by the home team |
| 4 | own_position | Real | Min: 1.0 Max: 21.0  | Real value storing the rating of the home team |
| 5 | own_manager_name | Text | Syntax: firstname lastname or lastname | first and last name of the home club manager if both names are available |
| 6 | opponent_id | Integer | Min: 1 Max: 113,000 | Club Id for the away team |
| 7 | opponent_goals | Integer | Min: 0 Max: 19 | Integer value storing the number of goals scored by the away team |
| 8 | opponent_position | Real | Min: 1.0 Max: 21.0 | Real value storing the rating of the away team |
| 9 | opponent_manager_name | Text | Syntax: firstname lastname or lastname | first and last name of the away club manager if both names are available  |
| 10 | hosting | Text | Categories: "home", "away" | Categorical variable stored as text of which team hosted the match |
| 11 | is_win | Integer | Categories: 0, 1  | Categorical variable stored as an integer of whether or not the home team won (1) or lost (0) |

#### Clubs Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 | club_id | Integer | Min: 3 Max: 83,700 | Integer tag for identifying clubs across tables |
| 2 | club_code | Text | Multiple words of text, with words separated by '-' | Text storing a shortened version of the club name |
| 3 | name | Text | Multiple words of text, with words separated  by spaces | Text storing the full version of the club name |
| 4 | domestic_competiton | Text | 2 to 4 letter abbreviation | Text storing the name of the domestic (local) competition that the club competes in |
| 5 | total_market_value | Integer | All values in this column are null | Integer value meant to store the total market value of the club team, however, all values in this column are null |
| 6 | squad_size | Integer | Min: 0 Max: 41 | Integer value that stores the number of players in the club team |
| 7 | average_age | Real | Min: 18.3 Max: 29.3 | Real number that stores the average age of players in the club team |
| 8 | foreigners_number | Integer | Min: 0 Max: 26 | Integer value that stores the number of foreigners on a given club team |
| 9 | foreigners_percentage | Real | Min: 24.0 Max: 100.0 | Real number that stores the percentage of foreigners in a club team |
| 10 | national_team_players | Integer | Min: 0 Max: 21 | Integer value that stores the number of players that also play for a national team in a given club team |
| 11 | stadium_name | Text | Multiple syntaxes: words not separated, words separated by spaces, and words separated by '-' | Text storing the name of the home stadium of the club |
| 12 | stadium_seats | Integer | Min: 1312 Max: 81,400 | Integer value storing the number of seats in the home stadium of the club |
| 13 | net_transfer_record | Text | Text starting with a '+' or '-', the local currency of the club, and a numerical value between -1.0 million and 99.4 million  | Text storing the total losses or gains made by the club through transfers |
| 14 | coach_name | Text | All values null | Text that should store the first and last name of the home club coach, however, all values null |
| 15 | last_season | Integer |  Min: 2012 Max: 2023 | Integer value storing the last recorded year the club played. |
| 16 | filename | Text | all file names end with .json.gz  | Text storing the name of the file where the data in the table was found |
| 17 | url | Text | full website url required | Text storing the website where the data was scraped from |

#### Competitions Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 | competition_id  | Text | 3 to 4 letter abbreviation | Abbreviation tags storing the type of competition of the given game (game_id) to be used across tables|
| 2 | competition_code | Text | Multiple words of text, with words separated by '-' | Text storing a shortened version of the name of the given competition |
| 3 | name | Text | Multiple words of text, with words separated by spaces | Text storing the full version of the given competition's name |
| 4 | sub_type | Text | Multiple words of text, with words separated by '_' | Text storing the specific type of the given competition  |
| 5 | type | Text | Multiple words of text, with words separated by '_' | Text storing the general type of the given competition  |
| 6 | country_id | Integer | Min: -1 Max: 190 | Integer tag storing the country that the competition took place in |
| 7 | country_name | Text | Multiple words of text, with words separated by spaces | Text storing the name of the country where the competition took place |
| 8 | domestic_leauge_code | Text | 3 to 4 letter abbreviation or null | Text storing a code for identifying the type of domestic competitions and null for non-domestic competitions |
| 9 | confederation | Text | Static Value: Europa | Static text value identifying the confederation in which the competition took place |
| 10 | url | Text | full website url required | Text storing the website where the data was scraped from |
| 11 | is_major_national_leauge | Text | Categorical Values: '0', '1' | Categorical values stating whether the competition is part of the major national league (1) or not (0) |

#### Game Events Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 | game_event_id | Text | One long string with a mixture of numbers and letters | Text tag to keep track of the game event across tables |
| 2 |  date | Date | Special Date type with the syntax YYYY/MM/DD | Date that the event stored in the game_event_id was played  |
| 3 | game_id | integer | Min: 2.21 million Max: 4.35 million  | Integer tag for identifying games across tables  |
| 4 | minute | integer | Min: -1 Max: 120  | The minute at which the given event occurred, with -1 for before the clock starts|
| 5 | type | text | Categorical variable: 3 categories, each labeled with a one-word string  | Text storing the type of event that occurred |
| 6 | club_id | Integer | Min: 3 Max: 83,700 | Integer tag for identifying clubs across tables |
| 7 | player_id | integer | Min: 10 Max: 1.24 million  | Integer tag for identifying players across tables  |
| 8 | description | text |  Strings separated by spaces and commas | A short description of the event that occurred |
| 9 | player_in_id | integer | Min: 10 Max: 1.24 million  | Integer tag for identifying the player id for the main player involved with the event  |
| 10 | player_asisst_id | integer | | Min: 10 Max: 1.24 million  | Integer tag for identifying the player id for the player who helped assists involved with the event  |

#### Game Lineups Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 | game_lineups-ID |Text | One long string with a mixture of numbers and letters | Text tag to keep track of the game lineups across tables |
| 2 | date | Special Date type with the syntax YYYY/MM/DD | Date that the game stored in the game_id was played  |
| 3 | game_id | Integer | Min: 2.21 million Max: 4.35 million  | Integer tag for identifying games across tables  |
| 4 | club_id | Integer | Min: 1 Max: 113,000 | Integer tag for identifying clubs across tables |
| 5 | player_id | Integer | Min: 10 Max: 1.24 million  | Integer tag for identifying players across tables  |
| 6 | player_name | Text |  In the syntax firstname lastname or lastname |  first and last name of the given player (player_id) if both names are available|
| 7 | position | Text | Categorical variables of text separated by spaces | General title of the position the the given player (player_id) plays |
| 8 | type |  Text |  Categorical variables of text separated by '_' | Stores if the player is on the starting lineup or a substitute |
| 9 | number | Integer |  Min: 0 Max: 58 | Integer value that stores the given player's (player_id) jersey number  |
| 10 | team_captain | Integer  | Min:0 Max:1  |  Categorical variable stating whether the given player is a team captain (1) or not (0) |

#### Games Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 | game_id | Integer | Min: 2.21 million Max: 4.35 million  | Integer tag for identifying games across tables  |
| 2 | date | Date | Special Date type with the syntax YYYY/MM/DD | Date that the game stored in the game_id was played  |
| 3 | competition_id | Text | 3 to 4 letter abbreviation | Abbreviation tags storing the type of competition of the given game (game_id) to be used across tables |
| 4 | season | Text | Years between 2012 and 2023 | Season the competition took place in by year |
| 5 | round | Text | Categorical variables, text separated by spaces | Name of the round that the given game (game_id) took place in |
| 6 | attendance | Integer | Min: 1 Max: 99,400 | Recorded attendance for the given game (game_id) |
| 7 | referee | Text | Multiple Syntaxes: firstname lastname, lastname, title firstname lastname, firstname lastname1 lastname2  | Name of the referee during the given game (game_id) |
| 8 | home_club_id | Integer | Min: 1 Max: 113,000 | Integer tag for identifying clubs across tables, in this case, specifically the home team |
| 9 | away_club_id | Integer | Min: 2 Max: 113,000 | Integer tag for identifying clubs across tables, in this case, specifically the away team |
| 10 | home_club_goals | Integer | Min: 0 Max: 15| Integer value storing the number of goals scored by the home team |
| 11 | away_club_goals | Integer | Min: 0 Max: 19 | Integer value storing the number of goals scored by the away team |
| 12 | home_club_position | Integer | Min: 1 Max: 21 | Integer value storing the rating of the home team |
| 13 | away_club_position | Integer | Min: 1 Max: 21 | Integer value storing the rating of the away team |
| 14 | home_club_manager_name | Text | General Syntax: firstname lastname | Name of the home team manager during the given game (game_id) |
| 15 | away_club_manager_name | Text | General Syntax: firstname lastname  | Name of the away team manager during the given game (game_id) |
| 16 | stadium | Text | General Syntax: words separated by spaces | Name of the stadium where the given game (game_id) took place |
| 17 | url | Text | full website url required | Text storing the website where the data was scraped from |
| 18 | home_club_formation | Text | All values null  | This should be the year the given club was formed, however, all values in this column are null |
| 19 | away_club_formation | Text | All values null | This should be the year the given club was formed, however, all values in this column are null |
| 20 | home_club_name | Text | General Syntax: words separated by spaces | Name of the home club in the given game |
| 21 | away_club_name | Text | General Syntax: words separated by spaces | Name of the away club in the given game |
| 22 | aggregate | Text | General Syntax: home_club_goals:away_club_goals | Score of the game written as a ratio |
| 23 | competition_type | Text | Multiple words of text, with words separated by '_' | Text storing the general type of the given competition  |

#### Player Valuations Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 | player_id | Integer | Min: 10 Max: 1.24 million  | Integer tag for identifying players across tables  |
| 2 | date | Date | Special Date type with the syntax YYYY/MM/DD | Date that the valuation was calculated  |
| 3 | market_value_in_eur | Real | Min: 10000 Max: 180 million  | Real number storing the most recent market value of the player in Europe |
| 4 | current_club_id  | Int | Min: -1 Max: 837,000 | Integer tag for identifying a player's current club ID across tables 
| 5 | player_club_domestic_competition_id | Text | 2 to 4 letter abbreviation | Text storing the name of the domestic (local) competition that the given player (player_id) competes in 

#### Players Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 | player_id | Integer | Min: 10 Max: 1.24 million  | Integer tag for identifying players across tables  |
| 2 | player_code | Text | General Syntax: multiple words of text, with words separated by '-'  | Text storing the player's name, separated by '-' |
| 3 | name | Text | General Syntax: firstname lastname or lastname | Name of the player with the given player_id |
| 4 | position | Text | Categorical variables of text separated by spaces | General title of the position the given player (player_id) plays |
| 5 | date_of_birth | Date | Special Date type with the syntax YYYY/MM/DD | Date that the game stored in the game_id was played  |
| 6 | current_club_id | Integer | Min: 3 Max: 837,000 | Integer tag for identifying a player's current club ID across tables  |
| 7 | agent_name | Text | General Syntax: multiple words of text separated by spaces | Name of the agent company of the given player (player_id)  |
| 8 | image_url | Text | full website url required | Text storing a website where an image of the player is stored|
| 9 | url | Text | full website url required | Text storing the website where the data was scraped from |
| 10 | current_club_domestic_competition_id | Text | 2 to 4 letter abbreviation | Text storing the name of the domestic (local) competition that the given player's (player_id) most recent club competes in |
| 11 | current_club_name | Text | General Syntax: multiple words of text separated by spaces | Text storing the name of the given player's (player_id) most recent club |
| 12 | market_value_in_eur | Real | Min: 10000 Max: 180 million  | Real number storing the most recent market value of the club in Europe |
| 13 | highest_market_value_in_eur | Real | Min: 10000 Max: 200 million  | Real number storing the highest market value of the club in Europe |
| 14 | first_name | Text |  Single word string | Text value storing the first name of the current player (player_id) |
| 15 | last_name | Text | Single and multiple word string separated by spaces| Text value storing the last name of the current player (player_id) |
| 16 | last_season | Integer | Min: 2012 Max: 2023 | Integer value storing the last year that the given player (player_id) played in |
| 17 | country_of_birth | Text | Multiple word string separated by spaces | Text storing the country where the given player (player_id) was born |
| 18 | city_of_birth | Text | Multiple word string separated by spaces | Text storing the city where the given player (player_id) was born |
| 19 | country_of_citizenship | Text | Multiple word string separated by spaces | Text storing the country that the given player (player_id) is a citizen of |
| 20 | sub_position | Text | Categorical variables of text separated by spaces | Specific title of the position the the given player (player_id) plays |
| 21 | foot | Text |  Single word string | Text storing the dominant foot of the given player |
| 22 | height_in_cm | Integer | Min: 18 Max: 207 | Integer value storing the height of the given player (player_id) in cm |
| 23 | contract_expiration_date | Date | Special Date type with the syntax YYYY/MM/DD, majority of values null | Date value storing the contract expiration date of the given player (player_id)|
| 24 | rating | Real | Min: 0 Max: 1 | Calculated rating for the given player (player_id) as a decimal value between 0 and 1 |

#### Entity Relationship Diagram

![data_base](https://github.com/Riccardo-Maffei/Outsourced-Sport-Predictor/assets/174322968/758d405d-242d-43c1-9d19-660d76040117)



#### Data Quality
In general, this data was of very high quality as there were very few columns with a mixture of missing data and completed data, and the ones that were missing data were typically either entirely blank, allowing us to drop them, or had around 5% of the data missing, allowing us to easily fill in this values with means for numerical values or unknowns for categorical values. There were also very few static columns for us to drop.

## Processed Data
### Overview Processed Datasets
| Name | Quelle | Storage location |
|----------------|-----------------------------------------|--------------------------------------------------------------------------|
| data_modv6.csv | This set of data is a .csv file containing specific variables chosen and cleaned from our database | This data is obtainable by following the getting started section of the README|                                              

### Details Processed Dataset 1
- The data set includes home scores, away scores, player data for each player on the tea, and a little bit of data on the game itself
-Details about our processing steps can be found in the ReadMe
-This data is accessed through a.csv, which has been shortened to include only the points we deemed important for our model

#### Data Catalogue

| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 | home_club_goals | Integer | Min: 0 Max: 15| Integer value storing the number of goals scored by the home team |
| 2 | away_club_goals | Integer | Min: 0 Max: 15| Integer value storing the number of goals scored by the away team |
| 3 | referee | Text | Multiple Syntaxes: firstname lastname, lastname, title firstname lastname, firstname lastname1 lastname2  | Name of the referee during the given game (game_id) |
| 4 | competition_type | Text | Multiple words of text, with words separated by '_' | Text storing the general type of the given competition  |
| 5 | attendance | Integer | Min: 1 Max: 99,400 | Recorded attendance for the given game (game_id) |
| 6 | home_type_1 | Text |  Categorical variables of text separated by '_' | Stores if home player 1 is on the starting lineup or a substitute |
| 7 | home_position_1 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 1 plays |
| 8 | home_position.1_1 | Text | Categorical variables of text separated by spaces | General title of the position home player 1 plays |
| 9 | home__sub_position_1 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 1 plays |
| 10 | home_foot_1 | Text |  Single word string | Text storing the dominant foot of home player 1  |
| 11 | home_height_1 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 1 in cm |
| 12 | home_rating_1 | Real | Min: 0 Max: 1 | Calculated rating home player 1 as a decimal value between 0 and 1 |
| 13 | home_age_1 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 1 |
| 14 | home_type_2 | Text |  Categorical variables of text separated by '_' | Stores if home player 2 is on the starting lineup or a substitute |
| 15 | home_position_2 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 2 plays |
| 16 | home_position.1_2 | Text | Categorical variables of text separated by spaces | General title of the position home player 2 plays |
| 17 | home__sub_position_2 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 2 plays |
| 18 | home_foot_2 | Text |  Single word string | Text storing the dominant foot of home player 2  |
| 19 | home_height_2 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 2 in cm |
| 20 | home_rating_2 | Real | Min: 0 Max: 1 | Calculated rating home player 2 as a decimal value between 0 and 1 |
| 21 | home_age_2 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 2 |
| 22 | home_type_3 | Text |  Categorical variables of text separated by '_' | Stores if home player 3 is on the starting lineup or a substitute |
| 23 | home_position_3 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 3 plays |
| 24 | home_position.1_3 | Text | Categorical variables of text separated by spaces | General title of the position home player 3 plays |
| 25 | home__sub_position_3 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 3 plays |
| 26 | home_foot_3 | Text |  Single word string | Text storing the dominant foot of home player 3  |
| 27 | home_height_3 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 3 in cm |
| 28 | home_rating_3 | Real | Min: 0 Max: 1 | Calculated rating home player 3 as a decimal value between 0 and 1 |
| 29 | home_age_3 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 1 |
| 30 | home_type_4 | Text |  Categorical variables of text separated by '_' | Stores if home player 4 is on the starting lineup or a substitute |
| 31 | home_position_4 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 4 plays |
| 32 | home_position.1_4 | Text | Categorical variables of text separated by spaces | General title of the position home player 4 plays |
| 33 | home__sub_position_4 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 4 plays |
| 34 | home_foot_4 | Text |  Single word string | Text storing the dominant foot of home player 4  |
| 35 | home_height_4 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 4 in cm |
| 36 | home_rating_4 | Real | Min: 0 Max: 1 | Calculated rating home player 4 as a decimal value between 0 and 1 |
| 37 | home_age_4 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 4 |
| 38 | home_type_5 | Text |  Categorical variables of text separated by '_' | Stores if home player 5 is on the starting lineup or a substitute |
| 39 | home_position_5 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 5 plays |
| 40 | home_position.1_5 | Text | Categorical variables of text separated by spaces | General title of the position home player 5 plays |
| 41 | home__sub_position_5 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 5 plays |
| 42 | home_foot_5 | Text |  Single word string | Text storing the dominant foot of home player 5  |
| 43 | home_height_5 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 5 in cm |
| 44 | home_rating_5 | Real | Min: 0 Max: 1 | Calculated rating home player 5 as a decimal value between 0 and 1 |
| 45 | home_age_5 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 5 |
| 46 | home_type_6 | Text |  Categorical variables of text separated by '_' | Stores if home player 6 is on the starting lineup or a substitute |
| 47 | home_position_6 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 6 plays |
| 48 | home_position.1_6 | Text | Categorical variables of text separated by spaces | General title of the position home player 6 plays |
| 49 | home__sub_position_6 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 6 plays |
| 50 | home_foot_6 | Text |  Single word string | Text storing the dominant foot of home player 6  |
| 51 | home_height_6 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 6 in cm |
| 52 | home_rating_6 | Real | Min: 0 Max: 1 | Calculated rating home player 6 as a decimal value between 0 and 1 |
| 53 | home_age_6 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 6 |
| 54 | home_type_7 | Text |  Categorical variables of text separated by '_' | Stores if home player 7 is on the starting lineup or a substitute |
| 55 | home_position_7 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 7 plays |
| 56 | home_position.1_7 | Text | Categorical variables of text separated by spaces | General title of the position home player 7 plays |
| 57 | home__sub_position_7 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 7 plays |
| 58 | home_foot_7 | Text |  Single word string | Text storing the dominant foot of home player 7  |
| 59 | home_height_7 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 7 in cm |
| 60 | home_rating_7 | Real | Min: 0 Max: 1 | Calculated rating home player 7 as a decimal value between 0 and 1 |
| 61 | home_age_7 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 7 |
| 62 | home_type_8 | Text |  Categorical variables of text separated by '_' | Stores if home player 8 is on the starting lineup or a substitute |
| 63 | home_position_8 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 8 plays |
| 64 | home_position.1_8 | Text | Categorical variables of text separated by spaces | General title of the position home player 8 plays |
| 65 | home__sub_position_8 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 8 plays |
| 66 | home_foot_8 | Text |  Single word string | Text storing the dominant foot of home player 8  |
| 67 | home_height_8 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 8 in cm |
| 68 | home_rating_8 | Real | Min: 0 Max: 1 | Calculated rating home player 8 as a decimal value between 0 and 1 |
| 69 | home_age_8 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 8 |
| 70 | home_type_9 | Text |  Categorical variables of text separated by '_' | Stores if home player 9 is on the starting lineup or a substitute |
| 71 | home_position_9 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 9 plays |
| 72 | home_position.1_9 | Text | Categorical variables of text separated by spaces | General title of the position home player 9 plays |
| 73 | home__sub_position_9 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 9 plays |
| 74 | home_foot_9 | Text |  Single word string | Text storing the dominant foot of home player 9  |
| 75 | home_height_9 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 9 in cm |
| 76 | home_rating_9 | Real | Min: 0 Max: 1 | Calculated rating home player 9 as a decimal value between 0 and 1 |
| 77 | home_age_10 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 10 |
| 6 | home_type_10 | Text |  Categorical variables of text separated by '_' | Stores if home player 10 is on the starting lineup or a substitute |
| 7 | home_position_10 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 10 plays |
| 8 | home_position.1_10 | Text | Categorical variables of text separated by spaces | General title of the position home player 10 plays |
| 9 | home__sub_position_10 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 10 plays |
| 10 | home_foot_10 | Text |  Single word string | Text storing the dominant foot of home player 10  |
| 11 | home_height_10 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 10 in cm |
| 12 | home_rating_10 | Real | Min: 0 Max: 1 | Calculated rating home player 10 as a decimal value between 0 and 1 |
| 13 | home_age_10 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 10 |
| 6 | home_type_11 | Text |  Categorical variables of text separated by '_' | Stores if home player 11 is on the starting lineup or a substitute |
| 7 | home_position_11 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 11 plays |
| 8 | home_position.1_11 | Text | Categorical variables of text separated by spaces | General title of the position home player 11 plays |
| 9 | home__sub_position_11 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 11 plays |
| 10 | home_foot_11 | Text |  Single word string | Text storing the dominant foot of home player 11  |
| 11 | home_height_11 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 11 in cm |
| 12 | home_rating_11 | Real | Min: 0 Max: 1 | Calculated rating home player 11 as a decimal value between 0 and 1 |
| 13 | home_age_11 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 11 |
| 14 | home_type_12 | Text |  Categorical variables of text separated by '_' | Stores if home player 12 is on the starting lineup or a substitute |
| 15 | home_position_2 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 2 plays |
| 16 | home_position.1_12 | Text | Categorical variables of text separated by spaces | General title of the position home player 12 plays |
| 17 | home__sub_position_12 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 12 plays |
| 18 | home_foot_12 | Text |  Single word string | Text storing the dominant foot of home player 12  |
| 19 | home_height_12 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 12 in cm |
| 20 | home_rating_12 | Real | Min: 0 Max: 1 | Calculated rating home player 12 as a decimal value between 0 and 1 |
| 21 | home_age_12 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 12 |
| 22 | home_type_13 | Text |  Categorical variables of text separated by '_' | Stores if home player 13 is on the starting lineup or a substitute |
| 23 | home_position_13 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 13 plays |
| 24 | home_position.1_13 | Text | Categorical variables of text separated by spaces | General title of the position home player 13 plays |
| 25 | home__sub_position_13 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 13 plays |
| 26 | home_foot_13 | Text |  Single word string | Text storing the dominant foot of home player 13  |
| 27 | home_height_13 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 13 in cm |
| 28 | home_rating_13 | Real | Min: 0 Max: 1 | Calculated rating home player 13 as a decimal value between 0 and 1 |
| 29 | home_age_13 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 13 |
| 30 | home_type_14 | Text |  Categorical variables of text separated by '_' | Stores if home player 14 is on the starting lineup or a substitute |
| 31 | home_position_14 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 14 plays |
| 32 | home_position.1_14 | Text | Categorical variables of text separated by spaces | General title of the position home player 14 plays |
| 33 | home__sub_position_14 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 14 plays |
| 34 | home_foot_14 | Text |  Single word string | Text storing the dominant foot of home player 14  |
| 35 | home_height_14 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 14 in cm |
| 36 | home_rating_14 | Real | Min: 0 Max: 1 | Calculated rating home player 14 as a decimal value between 0 and 1 |
| 37 | home_age_14 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 14 |
| 38 | home_type_15 | Text |  Categorical variables of text separated by '_' | Stores if home player 15 is on the starting lineup or a substitute |
| 39 | home_position_15 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 15 plays |
| 40 | home_position.1_15 | Text | Categorical variables of text separated by spaces | General title of the position home player 15 plays |
| 41 | home__sub_position_15 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 15 plays |
| 42 | home_foot_15 | Text |  Single word string | Text storing the dominant foot of home player 15  |
| 43 | home_height_15 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 15 in cm |
| 44 | home_rating_15 | Real | Min: 0 Max: 1 | Calculated rating home player 15 as a decimal value between 0 and 1 |
| 45 | home_age_15 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 15 |
| 46 | home_type_16 | Text |  Categorical variables of text separated by '_' | Stores if home player 16 is on the starting lineup or a substitute |
| 47 | home_position_16 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 16 plays |
| 48 | home_position.1_16 | Text | Categorical variables of text separated by spaces | General title of the position home player 16 plays |
| 49 | home__sub_position_16 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 16 plays |
| 50 | home_foot_16 | Text |  Single word string | Text storing the dominant foot of home player 16  |
| 51 | home_height_16 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 16 in cm |
| 52 | home_rating_16 | Real | Min: 0 Max: 1 | Calculated rating home player 16 as a decimal value between 0 and 1 |
| 53 | home_age_16 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 16 |
| 54 | home_type_17 | Text |  Categorical variables of text separated by '_' | Stores if home player 17 is on the starting lineup or a substitute |
| 55 | home_position_17 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 17 plays |
| 56 | home_position.1_17 | Text | Categorical variables of text separated by spaces | General title of the position home player 17 plays |
| 57 | home__sub_position_17 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 17 plays |
| 58 | home_foot_17 | Text |  Single word string | Text storing the dominant foot of home player 17  |
| 59 | home_height_17 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 17 in cm |
| 60 | home_rating_17 | Real | Min: 0 Max: 1 | Calculated rating home player 17 as a decimal value between 0 and 1 |
| 61 | home_age_17 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of home player 17 |
| 62 | home_type_18 | Text |  Categorical variables of text separated by '_' | Stores if home player 18 is on the starting lineup or a substitute |
| 63 | home_position_18 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 18 plays |
| 64 | home_position.1_18 | Text | Categorical variables of text separated by spaces | General title of the position home player 18 plays |
| 65 | home__sub_position_18 | Text | Categorical variables of text separated by spaces | Specific title of the position home player 18 plays |
| 66 | home_foot_18 | Text |  Single word string | Text storing the dominant foot of home player 18  |
| 67 | home_height_18 | Integer | Min: 18 Max: 207 | Integer value storing the height of home player 18 in cm |
| 68 | home_rating_18 | Real | Min: 0 Max: 1 | Calculated rating home player 18 as a decimal value between 0 and 1 |
| 6 | away_type_1 | Text |  Categorical variables of text separated by '_' | Stores if away player 1 is on the starting lineup or a substitute |
| 7 | away_position_1 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 1 plays |
| 8 | away_position.1_1 | Text | Categorical variables of text separated by spaces | General title of the position away player 1 plays |
| 9 | away__sub_position_1 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 1 plays |
| 10 | away_foot_1 | Text |  Single word string | Text storing the dominant foot of away player 1  |
| 11 | away_height_1 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 1 in cm |
| 12 | away_rating_1 | Real | Min: 0 Max: 1 | Calculated rating away player 1 as a decimal value between 0 and 1 |
| 13 | away_age_1 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 1 |
| 14 | away_type_2 | Text |  Categorical variables of text separated by '_' | Stores if away player 2 is on the starting lineup or a substitute |
| 15 | away_position_2 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 2 plays |
| 16 | away_position.1_2 | Text | Categorical variables of text separated by spaces | General title of the position away player 2 plays |
| 17 | away__sub_position_2 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 2 plays |
| 18 | away_foot_2 | Text |  Single word string | Text storing the dominant foot of away player 2  |
| 19 | away_height_2 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 2 in cm |
| 20 | away_rating_2 | Real | Min: 0 Max: 1 | Calculated rating away player 2 as a decimal value between 0 and 1 |
| 21 | away_age_2 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 2 |
| 22 | away_type_3 | Text |  Categorical variables of text separated by '_' | Stores if away player 3 is on the starting lineup or a substitute |
| 23 | away_position_3 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 3 plays |
| 24 | away_position.1_3 | Text | Categorical variables of text separated by spaces | General title of the position away player 3 plays |
| 25 | away__sub_position_3 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 3 plays |
| 26 | away_foot_3 | Text |  Single word string | Text storing the dominant foot of away player 3  |
| 27 | away_height_3 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 3 in cm |
| 28 | away_rating_3 | Real | Min: 0 Max: 1 | Calculated rating away player 3 as a decimal value between 0 and 1 |
| 29 | away_age_3 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 1 |
| 30 | away_type_4 | Text |  Categorical variables of text separated by '_' | Stores if away player 4 is on the starting lineup or a substitute |
| 31 | away_position_4 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 4 plays |
| 32 | away_position.1_4 | Text | Categorical variables of text separated by spaces | General title of the position away player 4 plays |
| 33 | away__sub_position_4 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 4 plays |
| 34 | away_foot_4 | Text |  Single word string | Text storing the dominant foot of away player 4  |
| 35 | away_height_4 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 4 in cm |
| 36 | away_rating_4 | Real | Min: 0 Max: 1 | Calculated rating away player 4 as a decimal value between 0 and 1 |
| 37 | away_age_4 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 4 |
| 38 | away_type_5 | Text |  Categorical variables of text separated by '_' | Stores if away player 5 is on the starting lineup or a substitute |
| 39 | away_position_5 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 5 plays |
| 40 | away_position.1_5 | Text | Categorical variables of text separated by spaces | General title of the position away player 5 plays |
| 41 | away__sub_position_5 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 5 plays |
| 42 | away_foot_5 | Text |  Single word string | Text storing the dominant foot of away player 5  |
| 43 | away_height_5 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 5 in cm |
| 44 | away_rating_5 | Real | Min: 0 Max: 1 | Calculated rating away player 5 as a decimal value between 0 and 1 |
| 45 | away_age_5 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 5 |
| 46 | away_type_6 | Text |  Categorical variables of text separated by '_' | Stores if away player 6 is on the starting lineup or a substitute |
| 47 | away_position_6 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 6 plays |
| 48 | away_position.1_6 | Text | Categorical variables of text separated by spaces | General title of the position away player 6 plays |
| 49 | away__sub_position_6 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 6 plays |
| 50 | away_foot_6 | Text |  Single word string | Text storing the dominant foot of away player 6  |
| 51 | away_height_6 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 6 in cm |
| 52 | away_rating_6 | Real | Min: 0 Max: 1 | Calculated rating away player 6 as a decimal value between 0 and 1 |
| 53 | away_age_6 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 6 |
| 54 | away_type_7 | Text |  Categorical variables of text separated by '_' | Stores if away player 7 is on the starting lineup or a substitute |
| 55 | away_position_7 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 7 plays |
| 56 | away_position.1_7 | Text | Categorical variables of text separated by spaces | General title of the position away player 7 plays |
| 57 | away__sub_position_7 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 7 plays |
| 58 | away_foot_7 | Text |  Single word string | Text storing the dominant foot of away player 7  |
| 59 | away_height_7 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 7 in cm |
| 60 | away_rating_7 | Real | Min: 0 Max: 1 | Calculated rating away player 7 as a decimal value between 0 and 1 |
| 61 | away_age_7 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 7 |
| 62 | away_type_8 | Text |  Categorical variables of text separated by '_' | Stores if away player 8 is on the starting lineup or a substitute |
| 63 | away_position_8 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 8 plays |
| 64 | away_position.1_8 | Text | Categorical variables of text separated by spaces | General title of the position away player 8 plays |
| 65 | away__sub_position_8 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 8 plays |
| 66 | away_foot_8 | Text |  Single word string | Text storing the dominant foot of away player 8  |
| 67 | away_height_8 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 8 in cm |
| 68 | away_rating_8 | Real | Min: 0 Max: 1 | Calculated rating away player 8 as a decimal value between 0 and 1 |
| 69 | away_age_8 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 8 |
| 70 | away_type_9 | Text |  Categorical variables of text separated by '_' | Stores if away player 9 is on the starting lineup or a substitute |
| 71 | away_position_9 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 9 plays |
| 72 | away_position.1_9 | Text | Categorical variables of text separated by spaces | General title of the position away player 9 plays |
| 73 | away__sub_position_9 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 9 plays |
| 74 | away_foot_9 | Text |  Single word string | Text storing the dominant foot of away player 9  |
| 75 | away_height_9 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 9 in cm |
| 76 | away_rating_9 | Real | Min: 0 Max: 1 | Calculated rating away player 9 as a decimal value between 0 and 1 |
| 77 | away_age_10 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 10 |
| 6 | away_type_10 | Text |  Categorical variables of text separated by '_' | Stores if away player 10 is on the starting lineup or a substitute |
| 7 | away_position_10 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 10 plays |
| 8 | away_position.1_10 | Text | Categorical variables of text separated by spaces | General title of the position away player 10 plays |
| 9 | away__sub_position_10 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 10 plays |
| 10 | away_foot_10 | Text |  Single word string | Text storing the dominant foot of away player 10  |
| 11 | away_height_10 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 10 in cm |
| 12 | away_rating_10 | Real | Min: 0 Max: 1 | Calculated rating away player 10 as a decimal value between 0 and 1 |
| 13 | away_age_10 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 10 |
| 6 | away_type_11 | Text |  Categorical variables of text separated by '_' | Stores if away player 11 is on the starting lineup or a substitute |
| 7 | away_position_11 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 11 plays |
| 8 | away_position.1_11 | Text | Categorical variables of text separated by spaces | General title of the position away player 11 plays |
| 9 | away__sub_position_11 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 11 plays |
| 10 | away_foot_11 | Text |  Single word string | Text storing the dominant foot of away player 11  |
| 11 | away_height_11 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 11 in cm |
| 12 | away_rating_11 | Real | Min: 0 Max: 1 | Calculated rating away player 11 as a decimal value between 0 and 1 |
| 13 | away_age_11 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 11 |
| 14 | away_type_12 | Text |  Categorical variables of text separated by '_' | Stores if away player 12 is on the starting lineup or a substitute |
| 15 | away_position_2 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 2 plays |
| 16 | away_position.1_12 | Text | Categorical variables of text separated by spaces | General title of the position away player 12 plays |
| 17 | away__sub_position_12 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 12 plays |
| 18 | away_foot_12 | Text |  Single word string | Text storing the dominant foot of away player 12  |
| 19 | away_height_12 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 12 in cm |
| 20 | away_rating_12 | Real | Min: 0 Max: 1 | Calculated rating away player 12 as a decimal value between 0 and 1 |
| 21 | away_age_12 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 12 |
| 22 | away_type_13 | Text |  Categorical variables of text separated by '_' | Stores if away player 13 is on the starting lineup or a substitute |
| 23 | away_position_13 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 13 plays |
| 24 | away_position.1_13 | Text | Categorical variables of text separated by spaces | General title of the position away player 13 plays |
| 25 | away__sub_position_13 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 13 plays |
| 26 | away_foot_13 | Text |  Single word string | Text storing the dominant foot of away player 13  |
| 27 | away_height_13 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 13 in cm |
| 28 | away_rating_13 | Real | Min: 0 Max: 1 | Calculated rating away player 13 as a decimal value between 0 and 1 |
| 29 | away_age_13 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 13 |
| 30 | away_type_14 | Text |  Categorical variables of text separated by '_' | Stores if away player 14 is on the starting lineup or a substitute |
| 31 | away_position_14 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 14 plays |
| 32 | away_position.1_14 | Text | Categorical variables of text separated by spaces | General title of the position away player 14 plays |
| 33 | away__sub_position_14 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 14 plays |
| 34 | away_foot_14 | Text |  Single word string | Text storing the dominant foot of away player 14  |
| 35 | away_height_14 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 14 in cm |
| 36 | away_rating_14 | Real | Min: 0 Max: 1 | Calculated rating away player 14 as a decimal value between 0 and 1 |
| 37 | away_age_14 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 14 |
| 38 | away_type_15 | Text |  Categorical variables of text separated by '_' | Stores if away player 15 is on the starting lineup or a substitute |
| 39 | away_position_15 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 15 plays |
| 40 | away_position.1_15 | Text | Categorical variables of text separated by spaces | General title of the position away player 15 plays |
| 41 | away__sub_position_15 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 15 plays |
| 42 | away_foot_15 | Text |  Single word string | Text storing the dominant foot of away player 15  |
| 43 | away_height_15 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 15 in cm |
| 44 | away_rating_15 | Real | Min: 0 Max: 1 | Calculated rating away player 15 as a decimal value between 0 and 1 |
| 45 | away_age_15 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 15 |
| 46 | away_type_16 | Text |  Categorical variables of text separated by '_' | Stores if away player 16 is on the starting lineup or a substitute |
| 47 | away_position_16 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 16 plays |
| 48 | away_position.1_16 | Text | Categorical variables of text separated by spaces | General title of the position away player 16 plays |
| 49 | away__sub_position_16 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 16 plays |
| 50 | away_foot_16 | Text |  Single word string | Text storing the dominant foot of away player 16  |
| 51 | away_height_16 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 16 in cm |
| 52 | away_rating_16 | Real | Min: 0 Max: 1 | Calculated rating away player 16 as a decimal value between 0 and 1 |
| 53 | away_age_16 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 16 |
| 54 | away_type_17 | Text |  Categorical variables of text separated by '_' | Stores if away player 17 is on the starting lineup or a substitute |
| 55 | away_position_17 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 17 plays |
| 56 | away_position.1_17 | Text | Categorical variables of text separated by spaces | General title of the position away player 17 plays |
| 57 | away__sub_position_17 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 17 plays |
| 58 | away_foot_17 | Text |  Single word string | Text storing the dominant foot of away player 17  |
| 59 | away_height_17 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 17 in cm |
| 60 | away_rating_17 | Real | Min: 0 Max: 1 | Calculated rating away player 17 as a decimal value between 0 and 1 |
| 61 | away_age_17 | Integer | Min: 16 Max: 41 | Integer storing the calculated age of away player 17 |
| 62 | away_type_18 | Text |  Categorical variables of text separated by '_' | Stores if away player 18 is on the starting lineup or a substitute |
| 63 | away_position_18 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 18 plays |
| 64 | away_position.1_18 | Text | Categorical variables of text separated by spaces | General title of the position away player 18 plays |
| 65 | away__sub_position_18 | Text | Categorical variables of text separated by spaces | Specific title of the position away player 18 plays |
| 66 | away_foot_18 | Text |  Single word string | Text storing the dominant foot of away player 18  |
| 67 | away_height_18 | Integer | Min: 18 Max: 207 | Integer value storing the height of away player 18 in cm |
| 68 | away_rating_18 | Real | Min: 0 Max: 1 | Calculated rating away player 18 as a decimal value between 0 and 1 |
