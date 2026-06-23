import tkinter as tk
from tkinter import messagebox
import random


class RPSGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Rock-Paper-Scissors")
        self.window.geometry("500x400")
        self.player_wins = 0
        self.computer_wins = 0
        self.ties = 0

        # Title
        title = tk.Label(window, text="Rock-Paper-Scissors", font=("Arial", 24, "bold"))
        title.pack(pady=20)

        # Display area for choices
        self.choice_label = tk.Label(window, text="Make your choice!", font=("Arial", 16))
        self.choice_label.pack(pady=10)

        # Buttons frame
        button_frame = tk.Frame(window)
        button_frame.pack(pady=20)

        rock_btn = tk.Button(button_frame, text="🪨 Rock", font=("Arial", 12),
                             command=lambda: self.play("rock"), width=10)
        rock_btn.grid(row=0, column=0, padx=10)

        paper_btn = tk.Button(button_frame, text="📄 Paper", font=("Arial", 12),
                              command=lambda: self.play("paper"), width=10)
        paper_btn.grid(row=0, column=1, padx=10)

        scissors_btn = tk.Button(button_frame, text="✂️ Scissors", font=("Arial", 12),
                                 command=lambda: self.play("scissors"), width=10)
        scissors_btn.grid(row=0, column=2, padx=10)

        # Result display
        self.result_label = tk.Label(window, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Score display
        self.score_label = tk.Label(window, text="", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.update_score_display()

    def play(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        # Determine winner
        if player_choice == computer_choice:
            result = "TIE!"
            self.ties += 1
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "scissors" and computer_choice == "paper") or \
                (player_choice == "paper" and computer_choice == "rock"):
            result = "YOU WIN!"
            self.player_wins += 1
        else:
            result = "COMPUTER WINS!"
            self.computer_wins += 1

        # Update display
        self.choice_label.config(text=f"You: {player_choice.upper()} | Computer: {computer_choice.upper()}")
        self.result_label.config(text=result, font=("Arial", 16, "bold"))
        self.update_score_display()

    def update_score_display(self):
        score_text = f"Score - You: {self.player_wins} | Computer: {self.computer_wins} | Ties: {self.ties}"
        self.score_label.config(text=score_text)


# Create window and run game
window = tk.Tk()
game = RPSGame(window)
window.mainloop()


