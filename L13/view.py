import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk

class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = None
        self.edit_genres_button = None
        self.genre_label = None
        self.title("Collection Manager")
        self.geometry("1200x700")
        self.configure(bg="#252525")

    def set_controller(self, controller):
        self.controller = controller
        self.create_widgets()
        self.hide_right_side()

    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self, bg="#252525")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left side
        left_frame = tk.Frame(main_frame, bg="#252525", width=200)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        self.search_entry = tk.Entry(left_frame, bg="#D9D9D9", fg="#000716")
        self.search_entry.pack(fill=tk.X, pady=(0, 5))

        self.search_button = tk.Button(left_frame, text="Search", command=self.on_search)
        self.search_button.pack(fill=tk.X, pady=(0, 10))

        collection_frame = tk.Frame(left_frame, bg="#252525")
        collection_frame.pack(fill=tk.X)

        self.movies_button = tk.Button(collection_frame, text="Movies", command=lambda: self.controller.select_collection("Movies"))
        self.movies_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.games_button = tk.Button(collection_frame, text="Games", command=lambda: self.controller.select_collection("Games"))
        self.games_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.books_button = tk.Button(collection_frame, text="Books", command=lambda: self.controller.select_collection("Books"))
        self.books_button.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.item_listbox = tk.Listbox(left_frame, bg="#464646", fg="#FFFFFF")
        self.item_listbox.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        self.item_listbox.bind('<<ListboxSelect>>', self.controller.on_item_select)

        # Right side
        self.right_frame = tk.Frame(main_frame, bg="#252525")
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        top_buttons_frame = tk.Frame(self.right_frame, bg="#252525")
        top_buttons_frame.pack(fill=tk.X, pady=(0, 10))

        self.add_button = tk.Button(top_buttons_frame, text="Create New", command=self.controller.create_new_item)
        self.add_button.pack(side=tk.LEFT, padx=(0, 10))

        self.image_button = tk.Button(top_buttons_frame, text="Select Image", command=self.controller.select_image)
        self.image_button.pack(side=tk.LEFT, padx=(0, 10))

        self.save_button = tk.Button(top_buttons_frame, text="Save", command=self.controller.save_item, state="disabled")
        self.save_button.pack(side=tk.LEFT, padx=(0, 10))

        self.edit_genres_button = tk.Button(top_buttons_frame, text="Edit Genres", command=self.controller.open_genre_selection, state="disabled")
        self.edit_genres_button.pack(side=tk.LEFT, padx=(0, 10))

        self.delete_button = tk.Button(top_buttons_frame, text="Delete", command=self.controller.delete_item)
        self.delete_button.pack(side=tk.RIGHT)

        # Image and description frame
        image_desc_frame = tk.Frame(self.right_frame, bg="#464646")
        image_desc_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        self.image_label = tk.Label(image_desc_frame, bg="#464646")
        self.image_label.pack(side=tk.TOP, pady=(0, 10))

        description_label = tk.Label(image_desc_frame, text="Description", bg="#464646", fg="#FFFFFF")
        description_label.pack(side=tk.TOP, anchor="w")

        self.description_text = tk.Text(image_desc_frame, bg="#D9D9D9", fg="#000716", wrap=tk.WORD, height=10)
        self.description_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.description_text.bind("<KeyRelease>", self.controller.on_field_edit)

        # Information display area
        self.info_frame = tk.Frame(self.right_frame, bg="#464646")
        self.info_frame.pack(fill=tk.BOTH, expand=True)

        self.info_canvas = tk.Canvas(self.info_frame, bg="#464646")
        self.info_scrollbar = ttk.Scrollbar(self.info_frame, orient="vertical", command=self.info_canvas.yview)
        self.scrollable_frame = tk.Frame(self.info_canvas, bg="#464646")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.info_canvas.configure(
                scrollregion=self.info_canvas.bbox("all")
            )
        )

        self.info_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.info_canvas.configure(yscrollcommand=self.info_scrollbar.set)

        self.info_canvas.pack(side="left", fill="both", expand=True)
        self.info_scrollbar.pack(side="right", fill="y")

    def on_search(self):
        if self.controller:
            self.controller.search()

    def hide_right_side(self):
        self.right_frame.pack_forget()

    def show_right_side(self):
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def create_info_fields(self, fields):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.info_fields = {}
        row = 0
        for key, value in fields.items():
            if key in ["description", "image_path"]:
                continue

            label = tk.Label(self.scrollable_frame, text=key, bg="#464646", fg="#FFFFFF")
            label.grid(row=row, column=0, sticky="w", padx=5, pady=2)

            if key == "Genres":
                self.genre_label = tk.Label(self.scrollable_frame, text=", ".join(value) if value else "No genres selected", 
                                            bg="#D9D9D9", fg="#000716", wraplength=300, justify="left")
                self.genre_label.grid(row=row, column=1, sticky="ew", padx=5, pady=2)
                self.info_fields[key] = self.genre_label
            else:
                entry = tk.Entry(self.scrollable_frame, bg="#D9D9D9", fg="#000716")
                entry.insert(0, str(value))
                entry.bind("<KeyRelease>", self.controller.on_field_edit)
                entry.grid(row=row, column=1, sticky="ew", padx=5, pady=2)
                self.info_fields[key] = entry

            row += 1

        self.scrollable_frame.grid_columnconfigure(1, weight=1)

        #         entry = tk.Entry(self.scrollable_frame, bg="#D9D9D9", fg="#000716")
        #         entry.insert(0, value)
        #         entry.bind("<KeyRelease>", self.controller.on_field_edit)
        #     entry.grid(row=row, column=col+1, sticky="ew", padx=5, pady=2)

        #     self.info_fields[key] = entry

        #     col += 2
        #     if col >= 4:  # Adjust this value to change the number of columns
        #         col = 0
        #         row += 1

        # self.scrollable_frame.grid_columnconfigure(1, weight=1)
        # self.scrollable_frame.grid_columnconfigure(3, weight=1)

    def clear_info_fields(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

    def show_genres_popup(self, genres, selected_genres):
        popup = tk.Toplevel(self)
        popup.title("Select Genres")
        popup.geometry("800x800")

        canvas = tk.Canvas(popup, borderwidth=0)
        scrollbar = ttk.Scrollbar(popup, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        genre_vars = {genre: tk.BooleanVar(value=genre in selected_genres) for genre in genres}

        for i, (genre, var) in enumerate(genre_vars.items()):
            tk.Checkbutton(scrollable_frame, text=genre, variable=var).grid(row=i, column=0, sticky="w")

        save_button = tk.Button(popup, text="Save Genres", command=lambda: self.controller.update_genres(genre_vars, popup))
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        save_button.pack(side="bottom", pady=10)

        # Configure the canvas scrolling
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))


    def update_image(self, image_path):
        if image_path:
            image = Image.open(image_path)
            image.thumbnail((300, 300))  # Resize image while maintaining aspect ratio
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        else:
            self.image_label.config(image="")

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def show_info(self, message):
        messagebox.showinfo("Info", message)

    def ask_yes_no(self, message):
        return messagebox.askyesno("Confirm", message)

    def get_file_path(self):
        return filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])

    def update_genre_label(self, genres):
        if self.genre_label:
            self.genre_label.config(text=", ".join(genres) if genres else "No genres selected")

    def enable_edit_genres_button(self):
        self.edit_genres_button.config(state="normal")

    def disable_edit_genres_button(self):
        self.edit_genres_button.config(state="disabled")