# controller.py

import tkinter as tk
from view import CollectionApp, TabMovies, TabGames, TabBooks
from model import CollectionManager

class TabController:
    def __init__(self, category, model, view):
        self.category = category
        self.model = model
        self.view = view

    def search_items(self, query):
        results = self.model.search_items(self.category, query.lower())
        self.view.update_items_listbox(results)

    def add_item(self, entries):
        new_item = {key: entry.get() for key, entry in entries.items()}
        self.model.add_item(self.category, new_item)
        messagebox.showinfo("Success", f"New {self.category[:-1]} added successfully.")
        self.search_items("")  # Automatically run search after adding

    def save_item(self, item, entries):
        updated_item = {key: entry.get() for key, entry in entries.items()}
        index = self.model.get_items(self.category).index(item)
        self.model.update_item(self.category, index, updated_item)
        messagebox.showinfo("Success", f"{self.category[:-1].capitalize()} updated successfully.")
        self.search_items("")  # Automatically run search after updating

    def delete_item(self, selected_index):
        if selected_index:
            index = selected_index[0]
            item = self.model.get_items(self.category)[index]
            confirmed = messagebox.askyesno("Delete Confirmation", f"Are you sure you want to delete {item.get('title', 'Unknown')}?")
            if confirmed:
                self.model.delete_item(self.category, index)
                messagebox.showinfo("Success", f"{self.category[:-1].capitalize()} deleted successfully.")
                self.search_items("")  # Automatically run search after deletion
        else:
            messagebox.showwarning("Warning", f"Select a {self.category[:-1]} to delete.")

class CollectionController:
    def __init__(self):
        self.manager = CollectionManager("collections.json")
        self.app = CollectionApp()

        self.tab_movies = TabMovies(self.app.notebook, self)
        self.tab_games = TabGames(self.app.notebook, self)
        self.tab_books = TabBooks(self.app.notebook, self)

        self.movies_controller = TabController("movies", self.manager, self.tab_movies)
        self.games_controller = TabController("games", self.manager, self.tab_games)
        self.books_controller = TabController("books", self.manager, self.tab_books)

    def initialize_tabs(self):
        self.app.add_tab(TabMovies, "Movies", self.movies_controller)
        self.app.add_tab(TabGames, "Games", self.games_controller)
        self.app.add_tab(TabBooks, "Books", self.books_controller)

    def run(self):
        self.initialize_tabs()
        self.app.mainloop()

if __name__ == "__main__":
    controller = CollectionController()
    controller.run()
