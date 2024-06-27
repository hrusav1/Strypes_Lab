from data_layer import CollectionManager

class CollectionService:
    def __init__(self, manager):
        self.manager = manager

    def add_item(self, category, item):
        self.manager.add_item(category, item)

    def update_item(self, category, index, new_item):
        self.manager.update_item(category, index, new_item)

    def delete_item(self, category, index):
        self.manager.delete_item(category, index)

    def search_items(self, category, query):
        return self.manager.search_items(category, query)

    def get_items(self, category):
        return self.manager.get_items(category)
