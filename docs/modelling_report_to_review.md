# `Sample Project` - Modelling Report
The report should summarise the details of the modelling activities, e.g. machine learning experiments. 

## Initial situation
- Aim of the modelling
    *The primary aim of the modelling is to predict the outcome of a soccer game based on factors such as the location of the game, the referee, and the individual players on each team. This aligns with the Data Mining Goals specified in the project charter.
- Data set(s) and/or feature set used
    The dataset used in this project was acquired from the Kaggle website (https://www.kaggle.com/datasets/davidcariboo/player-scores?resource=download). This data was subsequently input into a database, from which we extracted the necessary information as described in the Data Report. The features include both numerical and categorical variables representing various aspects of soccer games. The target variables are 'home_club_goals' and 'away_club_goals'. For further information, please refer to the Data Report.
- Description of the independent variables and the target variable
    Independent Variables:
        Numerical Variables: Various continuous variables relevant to the soccer game (e.g., player rating, player age).
        Categorical Variables: Categorical features such as the position of players, name of referees, and stadiom name.
    Target Variables:
        home_club_goals: The number of goals scored by the home team.
        away_club_goals: The number of goals scored by the away team.
- Type of model used or developed
    A neural network model was developed using TensorFlow's Keras API. This model was configured to predict the goals scored by both the home and away teams.

## Model Descriptions
Overview of the models used and/or implemented and their configurations 

- Detailed description of the model used
    Software Libraries:
        pandas for data manipulation and analysis.
        numpy for numerical computations.
        scikit-learn for preprocessing and model selection.
        tensorflow.keras for building and training the neural network model.
    Model Architecture:
        A sequential neural network model with multiple dense layers.
        Layers include dropout for regularization and L2 regularizers.
        Different loss functions (Mean Absolute Error, Mean Squared Error, Huber) and optimizers (Adam, SGD, RMSprop) were experimented with.
- Graphical representation of the modelling pipeline ------------------------------------------------
- If applicable: link to the code of the modelling pipeline, version information in code repository, configuration files  ------------------------------------------------------
- If possible, links to the artefacts of the executed modelling pipeline (training experiment) -----------------
- Link to the literature in which the model/method is described
    https://www.tensorflow.org/guide/keras/sequential_model
    https://www.tensorflow.org/guide/migrate/early_stopping
    https://www.tensorflow.org/api_docs/python/tf/keras/regularizers/L2

- Hyperparameters
    Numerical Transformer:
        'StandardScaler' for scaling numerical features.
    Categorical Transformer:
        'OneHotEncoder' with "handle_unknown='ignore'".
    Neural Network:
        Number of Layers: Multiple dense layers.
        Activation Functions: ReLU for hidden layers, linear for output layer.
        Dropout Rate: Applied at various layers.
        Regularization: L2 regularizers.
        Optimizers: Adam, SGD, RMSprop.
        Loss Functions: Mean Absolute Error loss, Mean Squared Error loss, Huber loss.
        Early Stopping: Monitor validation loss with a patience of 5 epochs.

## Results
Key figures dependent on the model and modelling objective
    - Results of multiple Loss Optimizer combinations:
        With rounding:
            https://github.com/Riccardo-Maffei/Outsourced-Sport-Predictor/blob/dev/evaluation/Model_Results_With_Rounding.csv
        With out Rounding:
            https://github.com/Riccardo-Maffei/Outsourced-Sport-Predictor/blob/dev/evaluation/Model_Results_Without_Rounding.csv

## Model Interpretation
- Were the modelling objectives achieved?
    The primary objectives were to minimize error metrics such as MAE, MSE, and Huber Loss. The results indicate that different optimizers perform variably across these metrics.
    The objectives were partly achieved with a Overall Accuracy of predictions at around 50%, with the best performance seen using the SGD optimizer for MAE with rounding.
- Project Objectives
    The results from the modeling phase indicate that the project objectives can be achieved with further refinement. The error metrics suggest that there is room for optimization and potentially better performance.
- Findings Utilization and Limitations
    The findings indicate the strengths and weaknesses of different optimizers. These can guide the selection of optimizers in future iterations or similar projects.
    Limitations include the potential overfitting or underfitting of the models, the need for more robust evaluation metrics, and the variability in performance across different datasets.

## Conclusions and next steps
- Key Findings
    The SGD optimizer with rounding provided the best performance for MAE.
    Variability in performance across different optimizers suggests the need for tailored optimization strategies.

- Discussion of Limitations
    The models may require further tuning and validation on diverse datasets.
    Metrics such as ROC, AUC, and confusion matrices were not provided but are essential for a comprehensive evaluation.

- Proposal for Extensions and Further Work
    Conduct extensive hyperparameter tuning and cross-validation.
    Incorporate additional evaluation metrics and visualizations for a holistic assessment.
    Explore different model architectures and feature engineering techniques.

- Proposal for Deployment
    Develop a user-friendly UI for deploying the model, allowing users to input data and receive predictions directly.
    Ensure the deployment pipeline includes model monitoring and periodic retraining to maintain performance.
