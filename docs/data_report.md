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
| 1 |   |   |   |   |
| 2 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |

#### Game Lineups Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 |   |   |   |   |
| 2 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |

#### Games Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 | game_id | Integer | Min: 2.21 million Max: 4.35 million  | Integer tag for identifying games across tables  |
| 2 | date | Date | Special Date type with the syntax YYYY/MM/DD | Date that the game stored in the game_id was played  |
| 3 | competition_id | Text | 3 to 4 letter abbreviation | Abbreviation tags storing the type of competition of the given game (game_id) to be used across tables |
| 4 | season | Text | Years between 2012 and 2023 | Season the competition took place in by year |
| 5 | round | Text | Categorical variables, text seperated by spaces | Name of the round that the given game (game_id) took place in |
| 6 | attendance | Integer | Min: 1 Max: 99,400 | Recorded attendance for the given game (game_id) |
| 7 | referee | Text | Multiple Syntaxes: firstname lastname, lastname, title firstname lastname, firstname lastname1 lastname2  | Name of the referee during the given game (game_id) |
| 8 | home_club_id | Integer | Min: 1 Max: 113,000 | Integer tag for identifying clubs across tables, in this case, specifically the home team |
| 9 | away_club_id | Integer | Min: 2 Max: 113,000 | Integer tag for identifying clubs across tables, in this case, specifically the away team |
| 10 |   |   |   |   |
| 11 |   |   |   |   |
| 12 |   |   |   |   |
| 13 |   |   |   |   |
| 14 |   |   |   |   |
| 15 |   |   |   |   |
| 16 |   |   |   |   |
| 17 |   |   |   |   |
| 18 |   |   |   |   |
| 19 |   |   |   |   |
| 20 |   |   |   |   |
| 21 |   |   |   |   |
| 22 |   |   |   |   |
| 23 |   |   |   |   |

#### Player Valuations Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 |   |   |   |   |
| 2 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |

#### Players Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 |   |   |   |   |
| 2 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |
| 3 |   |   |   |   |

#### Entity Relationship Diagram

![data_base](https://github.com/Riccardo-Maffei/Outsourced-Sport-Predictor/assets/174322968/758d405d-242d-43c1-9d19-660d76040117)



#### Data Quality
In generak with this data, there were specific values that were missing 5% top 1% outliers, most cases drop or process it to include a mean or unknown

## Processed Data
### Overview Processed Datasets
| Name | Quelle | Storage location |
|----------------|-----------------------------------------|--------------------------------------------------------------------------|
| Processed Dataset 1      | Name/short description of the data source | Link and/or short description of the location where the data is stored, e.g. accessible to the team |
| Processed Dataset 2      | …                                       | …                                                                        |

### Details Processed Dataset 1
- Description of what information the dataset contains
- Details and reasons for the processing steps -> Traceability and ensuring reproducibility
- How can the data be accessed? Description, scripts, tools, ...
- ...

#### Data Catalogue


#### If applicable: Entity Relationship Diagram


### Details Processed Dataset 2
...
