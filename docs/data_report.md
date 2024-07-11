# Outsourced Sport Predictor - Data Report


## Raw data
### Overview Raw Datasets
| Name | Quelle | Storage location |
|----------------|-----------------------------------------|--------------------------------------------------------------------------|
| Main Dataset | A collection of club football games and player data scraped off [transfermarkt](https://www.transfermarkt.com/) by David Cariboo. | [This Dataset is stored here on kaggle](https://www.kaggle.com/datasets/davidcariboo/player-scores?resource=download) |

### Main Dataset Details
This dataset contains multiple .csv files, including the scores, venues, referees, players, and player positions played for over 60,000 club games and over 30,000 players' heights, dominant feet, birth dates, red card records, and yellow card records. The data set was scraped off the website transfermarkt weekly by David Cariboo and posted on the website Kaggle. Transfermarkt is a website dedicated to compiling data on football games and football players. Kaggle is a website dedicated to providing computer scientists with tools and data sets to work with. To download this data, head to [this website](https://www.kaggle.com/datasets/davidcariboo/player-scores?resource=download), and click on the download button at the top of the page. On Kaggle, the dataset is listed with a CC0 license, making it available for public use. 

#### Data Catalog

#### Appearances Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 | appearance_id | Text | Two groups of numbers separated by an underscore, non-repeating | Numerical tag for identifying a unique appearance of a player  |
| 2 |  player_id | Integer | Min: 10, Max: 1.24 million  | Integer tag for identifying players across tables  |
| 3  | game_id  | Integer  | Min: 2.21 million, Max: 4.35 million  | Integer tag for identifying games across tables  |
| 4  | player_club_id  | Integer  | Min: 1, Max: 102,000  | Integer tag for identifying a player's club ID in a given games across tables  |
| 5  | player_current_club_id  | Int | Min: -1, Max: 837,000 | Integer tag for identifying a player's current club ID across tables  |
| 6  | date  | Date  | Special Date type with the syntax YYYY/MM/DD | Date that the game stored in the game_id was played  |
| 7  | player_name  | Text |  In syntax firstname lastname or lastname |  first and last name of the given player (player_id) if both names are available|
| 8  | competition_id  | Text |  3 to 4 letter abbreviation |  Abbrevitation storing the type of competition of the given game (game_id) |
| 9  | yellow_cards  | Integer | Min: 0, Max: 2  |  The amount of yellow cards the given player (player_id) recived in the given game (game_id) |
| 10 | red_cards  | Integer | Min: 0, Max: 1 |  The amount of yellow cards the given player (player_id) recived in the given game (game_id) |
| 11 | goals  | Integer | Min: 0, Max: 6  | The number of goals scored by the given player (player_id) in the given game (game_id)  |
| 12 | asissts  | Integer | Min: 0, Max: 6  | The number of asissts from the given player (player_id) in the given game (game_id) |
| 13 | minutes_played  | Integer  | Min: 1 Max: 135  | The amount of time the given player (player_id) played in the given game (game_id) |

#### Club Games Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 |   |   |   |   |
| 2 |   |   |   |   |
|   |   |   |   |   |

#### Clubs Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 |   |   |   |   |
| 2 |   |   |   |   |
|   |   |   |   |   |

#### Competitions Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 |   |   |   |   |
| 2 |   |   |   |   |
|   |   |   |   |   |

#### Game Events Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 |   |   |   |   |
| 2 |   |   |   |   |
|   |   |   |   |   |

#### Game Lineups Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 |   |   |   |   |
| 2 |   |   |   |   |
|   |   |   |   |   |

#### Games Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 |   |   |   |   |
| 2 |   |   |   |   |
|   |   |   |   |   |

#### Player Valuations Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 |   |   |   |   |
| 2 |   |   |   |   |
|   |   |   |   |   |

#### Players Table
| Column index | Column name |  Datatype | Values (Range, validation rules) | Short description |
|---|---|---|---|---|
| 1 |   |   |   |   |
| 2 |   |   |   |   |
|   |   |   |   |   |

#### Entity Relationship Diagram

![Screenshot 2024-07-09 130855](https://github.com/Riccardo-Maffei/Outsourced-Sport-Predictor/assets/174322968/b892c82b-9022-4ae9-b883-ceaa2a08f7b0)


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
