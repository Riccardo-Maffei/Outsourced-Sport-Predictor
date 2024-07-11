import tkinter as tk
from tkinter import ttk


# Dummy model function for prediction
def predict_match(team1, team2):
    # Replace this with your actual model's prediction logic
    # For now, it's a dummy prediction
    return f"{team1} vs {team2}: 1-0"


def predict_result(self, team_1_label_name, team_2_label_name, result_label_name):
    team_1_input_field = getattr(self, team_1_label_name)
    team_2_input_field = getattr(self, team_2_label_name)
    result_label = getattr(self, result_label_name)

    team1 = team_1_input_field.get()
    team2 = team_2_input_field.get()

    print("Predict Result was called")
    print(team1)
    print(team2)

    if team1 and team2:
        result = predict_match(team1, team2)
        result_label.config(text=result)
    else:
        result_label.config(text="Please enter both team names.")


class App(tk.Tk):
    def create_text_element(self, label_name, text, padding):
        label = ttk.Label(self, text=text)
        label.pack(pady=padding)
        setattr(self, label_name, label)

    def create_input_field(self, label_name, padding):
        entry = ttk.Entry(self)
        entry.pack(pady=padding)
        setattr(self, label_name, entry)

    def create_button(self, label_name, text, command, padding):
        button = ttk.Button(self, text=text, command=command)
        button.pack(pady=padding)
        setattr(self, label_name, button)


if __name__ == "__main__":
    app = App()

    app.title("Soccer Match Predictor")
    app.geometry("1000x500")

    app.create_text_element("page_title", "Soccer Match Predictor", 10)

    app.create_text_element("team_1_label", "Team 1:", 5)
    app.create_input_field("input_field_team_1", 5)

    app.create_text_element("team_2_label", "Team 2:", 5)
    app.create_input_field("input_field_team_2", 5)

    app.create_text_element("result_label", "Output:", 5)
    app.create_text_element("result_text", "", 5)

    app.create_button("predict_button", "Predict Result", lambda: predict_result(app,
                                                                                 "input_field_team_1",
                                                                                 "input_field_team_2",
                                                                                 "result_text"), 10)

    app.mainloop()
