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
| 1 | appearance_id | Text | Two groups of numbers seperated by an underscore, non-repeating | Numerical tag for identifying a unique appearance of a player  |
| 2 |  player_id | Int | Min: 10 Max: 1.24 million  | Integer tag for identifying players across files  |
| 3  | game_id  | Int  | Min: 10 Max: 1.24 million  |   |
| 3  | game_id  |   |   |   |
| 3  | game_id  |   |   |   |
| 3  | game_id  |   |   |   |
| 3  | game_id  |   |   |   |

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
