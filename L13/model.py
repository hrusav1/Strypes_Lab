import json
from pathlib import Path

class Item:
    def __init__(self, title, description="", image_path=""):
        self.title = title
        self.description = description
        self.image_path = image_path

class Movie(Item):
    def __init__(self, title, description="", image_path="", release_date="", runtime="", imdb_rating="", 
                 metascore="", rotten_tomatoes="", director="", writer="", main_cast="", supporting_cast="",
                 Genres=None, tagline="", budget="", box_office="", production_companies="", 
                 filming_locations="", language="", country="", awards=""):
        super().__init__(title, description, image_path)
        self.release_date = release_date
        self.runtime = runtime
        self.imdb_rating = imdb_rating
        self.metascore = metascore
        self.rotten_tomatoes = rotten_tomatoes
        self.director = director
        self.writer = writer
        self.main_cast = main_cast
        self.supporting_cast = supporting_cast
        self.Genres = Genres or []
        self.tagline = tagline
        self.budget = budget
        self.box_office = box_office
        self.production_companies = production_companies
        self.filming_locations = filming_locations
        self.language = language
        self.country = country
        self.awards = awards

class Game(Item):
    def __init__(self, title, description="", image_path="", release_date="", developer="", publisher="",
                 user_reviews="", metascore="", number_of_reviews="", Genres=None, game_modes="",
                 tags="", features="", min_requirements="", rec_requirements=""):
        super().__init__(title, description, image_path)
        self.release_date = release_date
        self.developer = developer
        self.publisher = publisher
        self.user_reviews = user_reviews
        self.metascore = metascore
        self.number_of_reviews = number_of_reviews
        self.Genres = Genres or []
        self.game_modes = game_modes
        self.tags = tags
        self.features = features
        self.min_requirements = min_requirements
        self.rec_requirements = rec_requirements

class Book(Item):
    def __init__(self, title, description="", image_path="", author="", publisher="", publication_date="",
                 isbn="", language="", Genres=None, tags="", series_info=""):
        super().__init__(title, description, image_path)
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
        self.isbn = isbn
        self.language = language
        self.Genres = Genres or []
        self.tags = tags
        self.series_info = series_info

class Model:
    def __init__(self):
        self.collections = {
            "Movies": [],
            "Games": [],
            "Books": []
        }
        self.load_data()

    def add_item(self, collection_name, item):
        self.collections[collection_name].append(item)
        self.save_data()

    def remove_item(self, collection_name, item):
        self.collections[collection_name].remove(item)
        self.save_data()

    def get_items(self, collection_name):
        return self.collections[collection_name]

    def search_items(self, query, collection_name):
        results = []
        for item in self.collections[collection_name]:
            if any(query.lower() in str(value).lower() for value in vars(item).values()):
                results.append(item)
        return results

    def save_data(self):
        data = {}
        for name, collection in self.collections.items():
            data[name] = [vars(item) for item in collection]
        
        with open("collections.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open("collections.json", "r") as f:
                data = json.load(f)
            
            for name, items in data.items():
                for item_data in items:
                    if name == "Movies":
                        item = Movie(**item_data)
                    elif name == "Games":
                        item = Game(**item_data)
                    elif name == "Books":
                        item = Book(**item_data)
                    self.collections[name].append(item)
        except FileNotFoundError:
            pass

    def create_new_item(self, collection_name):
        if collection_name == "Movies":
            new_item = Movie("New Movie")
        elif collection_name == "Games":
            new_item = Game("New Game")
        elif collection_name == "Books":
            new_item = Book("New Book")
        else:
            raise ValueError("Invalid collection name")
        
        self.add_item(collection_name, new_item)
        return new_item

    def get_genres(self, collection_name):
        if collection_name == "Movies":
            return [
                "Action", "Adventure", "Comedy", "Drama", "Fantasy", "Horror", "Mystery",
                "Romance", "Sci-Fi", "Thriller", "Western", "Animation", "Crime", "Documentary",
                "Family", "Musical", "War", "Historical", "Biographical", "Sports", "Superhero",
                "Noir", "Suspense", "Martial Arts", "Post-Apocalyptic", "Disaster", "Epic",
                "Teen", "Dance", "Silent"
            ]
        elif collection_name == "Games":
            return [
                "Action", "Adventure", "Role-Playing (RPG)", "Simulation", "Strategy", "Sports",
                "Puzzle", "Idle", "Sandbox", "Survival", "Horror", "Stealth", "Fighting",
                "Beat 'em Up", "Platformer", "Shooter", "Racing", "Rhythm", "Turn-Based Strategy (TBS)",
                "Real-Time Strategy (RTS)", "Massive Multiplayer Online (MMO)",
                "Multiplayer Online Battle Arena (MOBA)", "Card Game", "Roguelike", "Metroidvania",
                "Visual Novel", "Text-Based", "Interactive Fiction", "Tactical RPG", "Battle Royale",
                "Party Games", "Educational", "Casual", "Fitness", "Trivia", "Escape Room",
                "Tycoon/Management"
            ]
        elif collection_name == "Books":
            return [
                "Fiction", "Literary", "Mystery", "Thriller", "Horror", "Science Fiction",
                "Fantasy", "Romance", "Historical Fiction", "Adventure", "Dystopian",
                "Magical Realism", "Satire", "Speculative Fiction", "Crime", "Gothic",
                "Coming-of-Age", "Urban Fantasy", "Paranormal", "Political Fiction",
                "Non-Fiction", "Biography", "Memoir", "Self-Help", "History", "True Crime",
                "Essay", "Travel", "Science", "Philosophy", "Psychology", "Business",
                "Spirituality", "Health and Wellness", "Cooking", "Art", "Music",
                "Political Science", "Sociology", "Technology", "Poetry", "Graphic Novels",
                "Anthologies", "Short Stories", "Drama", "Children's", "Young Adult", "New Adult"
            ]
        else:
            return []