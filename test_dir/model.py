# model.py

import json
import os

class CollectionManager:
    def __init__(self, filename):
        self.filename = filename
        self.collections = {"movies": [], "games": [], "books": []}
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.collections = json.load(file)

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.collections, file, indent=4)

    def add_item(self, category, item):
        self.collections[category].append(item)
        self.save_data()

    def update_item(self, category, index, new_item):
        self.collections[category][index] = new_item
        self.save_data()

    def delete_item(self, category, index):
        del self.collections[category][index]
        self.save_data()

    def search_items(self, category, query):
        return [item for item in self.collections[category] if query.lower() in json.dumps(item).lower()]

    def get_items(self, category):
        return sorted(self.collections[category], key=lambda x: x.get('title', x.get('Title', x.get('name', ''))))
