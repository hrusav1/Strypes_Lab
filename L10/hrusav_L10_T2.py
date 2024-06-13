import tkinter as tk
from tkinter import messagebox

class HangmanModel:
    def __init__(self):
        self.word = "PYTHON"
        self.max_guesses = 7
        self.guesses_left = self.max_guesses
        self.guessed_letters = set()
        self.hangman_stages = [
            r"""
                _______
               |       |
                       |
                       |
                       |
                       |
                _________|_______
            """,
            r"""
                _______
               |       |
               O       |
                       |
                       |
                       |
                _________|_______
            """,
            r"""
                _______
               |       |
               O       |
               |       |
                       |
                       |
                _________|_______
            """,
            r"""
                _______
               |       |
               O       |
              /|       |
                       |
                       |
                _________|_______
            """,
            r"""
                _______
               |       |
               O       |
              /|\      |
                       |
                       |
                _________|_______
            """,
            r"""
                _______
               |       |
               O       |
              /|\      |
              /        |
                       |
                _________|_______
            """,
            r"""
                _______
               |       |
               O       |
              /|\      |
              / \      |
                       |
                _________|_______
            """
        ]

    def get_display_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])

    def make_guess(self, guess):
        if guess in self.guessed_letters:
            return False, "Already Guessed"
        
        self.guessed_letters.add(guess)
        if guess not in self.word:
            self.guesses_left -= 1
        
        return True, "Correct" if guess in self.word else "Incorrect"

    def is_game_over(self):
        if "_" not in self.get_display_word():
            return True, "Win"
        if self.guesses_left <= 0:
            return True, "Lose"
        return False, None

class HangmanView:
    def __init__(self, root):
        self.controller = None
        self.root = root
        self.root.title("Hangman")

        self.hangman_ascii = tk.Label(self.root, text="", font=("Courier", 12))
        self.hangman_ascii.pack()

        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.word_label.pack(pady=10)

        self.guess_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.guess_label.pack(pady=5)

        self.letter_buttons_frame = tk.Frame(self.root)
        self.letter_buttons_frame.pack()

        self.letter_buttons = {}
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            button = tk.Button(self.letter_buttons_frame, text=letter, font=("Helvetica", 16), command=lambda l=letter: self.controller.handle_guess(l))
            button.grid(row=(ord(letter) - ord('A')) // 9, column=(ord(letter) - ord('A')) % 9, padx=5, pady=5)
            self.letter_buttons[letter] = button

        self.restart_button = tk.Button(self.root, text="Restart Game", font=("Helvetica", 16), command=self.restart_game)
        self.restart_button.pack(pady=20)
        self.restart_button.pack_forget()  # Hide the button initially

    def update_view(self, display_word, guesses_left, hangman_stage):
        self.word_label.config(text=display_word)
        self.guess_label.config(text=f"Guesses left: {guesses_left}")
        self.hangman_ascii.config(text=hangman_stage)

    def disable_buttons(self):
        for button in self.letter_buttons.values():
            button.config(state=tk.DISABLED)
        self.restart_button.pack()  # Show the restart button when the game is over

    def reset_buttons(self):
        for button in self.letter_buttons.values():
            button.config(state=tk.NORMAL)
        self.restart_button.pack_forget()  # Hide the restart button when the game restarts

    def restart_game(self):
        self.controller.restart_game()

class HangmanController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.update_view()

    def handle_guess(self, guess):
        valid, message = self.model.make_guess(guess)
        if not valid:
            messagebox.showinfo("Error", message)
        self.view.letter_buttons[guess].config(state=tk.DISABLED)
        self.update_view()

        game_over, result = self.model.is_game_over()
        if game_over:
            if result == "Win":
                messagebox.showinfo("Congratulations!", f"You guessed the word: {self.model.word}")
            elif result == "Lose":
                messagebox.showinfo("Game Over", "You have been hanged. Better luck next time!")
            self.view.disable_buttons()

    def update_view(self):
        display_word = self.model.get_display_word()
        guesses_left = max(0, self.model.guesses_left)
        hangman_stage = self.model.hangman_stages[min(self.model.max_guesses - guesses_left, len(self.model.hangman_stages) - 1)]
        self.view.update_view(display_word, guesses_left, hangman_stage)

    def restart_game(self):
        self.model.__init__()  # Reset the model
        self.view.reset_buttons()
        self.update_view()

if __name__ == "__main__":
    root = tk.Tk()
    model = HangmanModel()
    view = HangmanView(root)  # Create the view without the controller
    controller = HangmanController(model, view)
    view.controller = controller  # Now assign the controller to the view
    root.mainloop()

