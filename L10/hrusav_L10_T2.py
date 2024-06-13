import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")
        self.word = "PYTHON"  # Hardcoded word to guess
        self.guesses_left = 7
        self.guessed_letters = set()

        self.create_widgets()

    def create_widgets(self):
        self.word_label = tk.Label(self.root, text=self.get_display_word(), font=("Helvetica", 24))
        self.word_label.pack(pady=10)

        self.guess_label = tk.Label(self.root, text=f"Guesses left: {self.guesses_left}", font=("Helvetica", 16))
        self.guess_label.pack(pady=5)

        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(self.root, text="Guess", command=self.handle_guess, font=("Helvetica", 16))
        self.guess_button.pack(pady=10)

    def get_display_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])

    def handle_guess(self):
        guess = self.guess_entry.get().upper()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You already guessed that letter.")
            return

        self.guessed_letters.add(guess)

        if guess not in self.word:
            self.guesses_left -= 1

        self.update_game_status()

    def update_game_status(self):
        self.word_label.config(text=self.get_display_word())
        self.guess_label.config(text=f"Guesses left: {self.guesses_left}")

        if "_" not in self.get_display_word():
            messagebox.showinfo("Congratulations!", f"You guessed the word: {self.word}")
            self.restart_game()

        if self.guesses_left == 0:
            messagebox.showinfo("Game Over", f"The word was: {self.word}")
            self.restart_game()

    def restart_game(self):
        self.guesses_left = 7
        self.guessed_letters = set()
        self.word_label.config(text=self.get_display_word())
        self.guess_label.config(text=f"Guesses left: {self.guesses_left}")


if __name__ == "__main__":
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()

