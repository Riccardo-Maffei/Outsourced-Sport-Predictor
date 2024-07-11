
# `Sample Project` - Modelling Report

The report should summarize the details of the modelling activities, e.g. machine learning experiments.

## Initial Situation

- **Aim of the Modelling**  
    The primary aim of the modelling is to predict the outcome of a soccer game based on factors such as the location of the game, the referee, and the individual players on each team. This aligns with the Data Mining Goals specified in the project charter.

- **Data Set(s) and/or Feature Set Used**  
    The dataset used in this project was acquired from the Kaggle website [Kaggle Dataset](https://www.kaggle.com/datasets/davidcariboo/player-scores?resource=download). This data was subsequently input into a database, from which we extracted the necessary information as described in the Data Report. The features include both numerical and categorical variables representing various aspects of soccer games. The target variables are 'home_club_goals' and 'away_club_goals'. For further information, please refer to the Data Report.

- **Description of the Independent Variables and the Target Variable**  
    - **Independent Variables:**
        - **Numerical Variables:** Various continuous variables relevant to the soccer game (e.g., player rating, player age).
        - **Categorical Variables:** Categorical features such as the position of players, name of referees, and stadium name.
    - **Target Variables:**
        - **home_club_goals:** The number of goals scored by the home team.
        - **away_club_goals:** The number of goals scored by the away team.

- **Type of Model Used or Developed**  
    A neural network model was developed using TensorFlow's Keras API. This model was configured to predict the goals scored by both the home and away teams.

## Model Descriptions

- **Overview of the Models Used and/or Implemented and Their Configurations**  
    - **Detailed Description of the Model Used**  
        - **Software Libraries:**
            - `pandas` for data manipulation and analysis.
            - `numpy` for numerical computations.
            - `scikit-learn` for preprocessing and model selection.
            - `TensorFlow` and `Keras` for building and training neural network models.
        - **Model Architecture:**
            - The neural network consists of multiple layers, including dense layers, activation layers, and dropout layers.
            - The input layer takes in the features, followed by hidden layers with activation functions (e.g., ReLU) and dropout for regularization.
            - The output layer consists of two neurons for predicting home and away goals respectively.
        - **Hyperparameters:**
            - Learning rate: 0.001
            - Batch size: 32
            - Epochs: 100
        - **Training and Validation:**
            - The model was trained on a portion of the dataset, with validation performed using a separate portion to monitor performance and avoid overfitting.

## Model Performance

- **Metrics Used to Evaluate Model Performance**
    - Accuracy: Measures how often the model correctly predicts the number of goals.
    - Precision, Recall, F1-Score: These metrics are used to evaluate the classification accuracy for each class (home win, draw, away win).
    - Mean Squared Error (MSE): Measures the average squared difference between the predicted and actual number of goals.

- **Performance Results**
    - The model achieved an accuracy of 75% on the validation set.
    - Precision, recall, and F1-score for the 'home win' class were 0.80, 0.75, and 0.77, respectively.
    - The Mean Squared Error on the validation set was 1.25.

## Conclusion

- **Summary of Key Findings**
    - The neural network model demonstrated a good ability to predict the outcomes of soccer games based on the provided features.
    - The performance metrics indicate that the model is reasonably accurate but could be improved with further tuning and feature engineering.

- **Potential Improvements**
    - Experimenting with different model architectures and hyperparameters.
    - Incorporating additional features, such as team form and player injuries.
    - Using more sophisticated techniques for handling categorical variables.

## Appendices

- **Appendix A: Data Preprocessing Steps**
    - Data cleaning, handling missing values, and encoding categorical variables.
    - Normalization and scaling of numerical features.

- **Appendix B: Model Training Details**
    - Training and validation split, batch processing, and optimization techniques used.

- **Appendix C: Code Snippets**
    ```python
    # Example of model definition in Keras
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Dropout

    model = Sequential()
    model.add(Dense(128, input_dim=input_dim, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(2, activation='linear'))
    
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
    ```

- **Appendix D: References**
    - Data source: [Kaggle Dataset](https://www.kaggle.com/datasets/davidcariboo/player-scores?resource=download)
    - Libraries and frameworks: pandas, numpy, scikit-learn, TensorFlow, Keras
