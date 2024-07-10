import tkinter as tk
from tkinter import ttk


# Dummy model function for prediction
def predict_match(team1, team2):
    # Replace this with your actual model's prediction logic
    # For now, it's a dummy prediction
    return f"{team1} vs {team2}: 1-0"


class SoccerPredictorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Soccer Match Predictor")
        self.geometry("300x200")

        # Team 1
        self.label_team1 = ttk.Label(self, text="Team 1:")
        self.label_team1.pack(pady=5)
        self.entry_team1 = ttk.Entry(self)
        self.entry_team1.pack(pady=5)

        # Team 2
        self.label_team2 = ttk.Label(self, text="Team 2:")
        self.label_team2.pack(pady=5)
        self.entry_team2 = ttk.Entry(self)
        self.entry_team2.pack(pady=5)

        # Predict Button
        self.predict_button = ttk.Button(self, text="Predict Result", command=self.predict_result)
        self.predict_button.pack(pady=10)

        # Result Label
        self.label_result = ttk.Label(self, text="")
        self.label_result.pack(pady=5)

    def predict_result(self):
        team1 = self.entry_team1.get()
        team2 = self.entry_team2.get()
        if team1 and team2:
            result = predict_match(team1, team2)
            self.label_result.config(text=result)
        else:
            self.label_result.config(text="Please enter both team names.")


if __name__ == "__main__":
    app = SoccerPredictorApp()
    app.mainloop()