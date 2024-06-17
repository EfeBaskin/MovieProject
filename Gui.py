import customtkinter as ctk
from tkinter import messagebox
from MovieRecomendation import recommend_movie


def on_recommend():
    movie_title = movie_entry.get()
    recommendations = recommend_movie(movie_title)
    if recommendations:
        result_var.set("\n".join(recommendations))
    else:
        messagebox.showerror("Error", "Movie not found!")


ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()
root.title("Movie Recommendation System")

ctk.CTkLabel(root, text="Enter Movie Title:").pack(pady=10)
movie_entry = ctk.CTkEntry(root, width=300)
movie_entry.pack(pady=10)

recommend_button = ctk.CTkButton(root, text="Recommend", command=on_recommend)
recommend_button.pack(pady=10)

result_var = ctk.StringVar()
ctk.CTkLabel(root, textvariable=result_var, justify="left").pack(pady=10)

root.mainloop()
