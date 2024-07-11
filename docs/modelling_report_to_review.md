
# `Soccer Predictor` - Modelling Report

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
            - The model was trained on a portion of the dataset, with early stopping to monitor performance and avoid overfitting.

- **Modeling Pipeline**
    This document describes the modeling pipeline based on the provided script. The pipeline consists of the following steps:
        
    1. **Data Loading**: Load the dataset from a specified path on Google Drive.
    2. **Data Preprocessing**:
        - Identify numerical and categorical columns.
        - Define preprocessing steps for numerical data (StandardScaler).
        - Define preprocessing steps for categorical data (OneHotEncoder).
        - Combine preprocessing steps using `ColumnTransformer`.
    3. **Data Splitting**: Split the data into training and testing sets.
    4. **Model Definition**: Define a Keras Sequential model.
    5. **Model Compilation**: Compile the model with specified loss functions and optimizers.
    6. **Model Training**: Train the model using the training data with early stopping.
    7. **Model Evaluation**: Evaluate the model on the test set and calculate various metrics.
    8. **Hyperparameter Tuning**: Experiment with different hyperparameters (regularizers, activation functions, dropout values, optimizers, loss functions).

- **Graphical Representation**

  Data Loading -> Data Preprocessing -> Data Splitting -> Model Definition -> Model Compilation -> Model Training -> Model Evaluation -> Hyperparameter Tuning

## Model Performance

- **Metrics Used to Evaluate Model Performance**
    - Accuracy: Measures how often the model correctly predicts the win, loss, draw rate.
    - Mean Squared Error (MSE): Measures the average squared difference between the predicted and actual number of goals.

- **Performance Results**
    - The best model achieved an accuracy of 46% on the test set.
    - The Mean Squared Error on the test set was 0.47.

## Conclusion

- **Summary of Key Findings**
    - The neural network model demonstrated a ability to predict the outcomes of soccer games based on the provided features.
    - The performance metrics indicate that the model is reasonably accurate for the topic but could be improved with further input data, tuning and feature engineering.

- **Potential Improvements**
    - Experimenting with different model architectures and hyperparameters.
    - Incorporating additional features, such as team form and player injuries.
    - Using more sophisticated techniques for handling categorical variables.

## Literature
- **Links to model/methods described**
    - [Sequential Model](https://www.tensorflow.org/guide/keras/sequential_model)
    - [Early Stopping](https://www.tensorflow.org/guide/migrate/early_stopping)
    - [L2 Regularizer](https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L2)

## Appendices

- **Appendix A: Data Preprocessing Steps**
    - Data cleaning, handling missing values, and encoding categorical variables.
    - Normalization and scaling of numerical features.

- **Appendix B: Model Training Details**
    - Training and validation split, batch processing, and optimization techniques used.

- **Appendix C: Code Snippets**
    ```python
    # Model example definition in Keras that was traind
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Dropout
    from tensorflow.keras.regularizers import l2
    from tensorflow.keras.optimizers import Adam

    activation = 'relu'
    kernel_regularizer = l2(0.001)
    loss = 'mean_squared_error'
    optimizer = Adam(learning_rate=0.0001)
    dropout = 0.3
    
    model = Sequential()
    model.add(Dense(512, input_dim=X_train.shape[1], activation=activation, kernel_regularizer=kernel_regularizer))
    model.add(Dropout(dropout))
    model.add(Dense(256, activation=activation, kernel_regularizer=kernel_regularizer))
    model.add(Dropout(dropout))
    model.add(Dense(128, activation=activation, kernel_regularizer=kernel_regularizer))
    model.add(Dropout(dropout))
    model.add(Dense(64, activation=activation, kernel_regularizer=kernel_regularizer))
    model.add(Dropout(dropout))
    model.add(Dense(32, activation=activation, kernel_regularizer=kernel_regularizer))
    model.add(Dense(2, dtype='float32'))  # Output layer for home and away goals

    # Compile the model with a different learning rate
    model.compile(optimizer=optimizer, loss=loss, metrics=['mae'])
    ```

- **Appendix D: References**
    - Data source: [Kaggle Dataset](https://www.kaggle.com/datasets/davidcariboo/player-scores?resource=download)
    - Libraries and frameworks: pandas, numpy, scikit-learn, TensorFlow, Keras

