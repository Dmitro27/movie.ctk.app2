from customtkinter import *
import requests
from PIL import Image
from io import BytesIO
import random

set_appearance_mode("dark")
set_default_color_theme("blue")

window = CTk()
window.title("Фільми")
window.geometry("450x650")

def get_random_movie():
    try:
        # Отримуємо список шоу "https://api.tvmaze.com/shows"
        response = requests.get("https://api.tvmaze.com/shows")
        data = response.json()
        

        # Вибираємо випадкове шоу
        movie = random.choice(data)

        # Отримуємо дані
        title = movie.get("name", "без назви")
        rating = movie.get("rating", {}).get("average", "??")
        genres = ", ".join(movie.get("genres", ["Невідомо"]))
        img_url = movie.get("image", {}).get("medium")


        # Оновлюємо текст назва шоу
        label_title.configure(text=title.upper())
        # Оновлюємо текст Жанр та Рейтинг: ⭐
        label_info.configure(text=f"Жанр: {genres}\nРейтинг: ⭐ {rating}")

        # ЗАВАНТАЖЕННЯ КАРТИНКИ
        if img_url:
            img_response = requests.get(img_url)
            img_data = BytesIO(img_response.content)
            
            # Перетворюємо байти в об'єкт
             

            # Створюємо CTkImage для коректного відображення
            my_image = CTkImage(light_image=Image.open(img_data), size=(250, 350))
            label_poster.configure(image=my_image, text="")
            
            
             # Прибираємо текст, ставимо фото
            
        else:
            label_poster.configure(image=None, text="Постер відсутній")

    except Exception as e:
        label_title.configure(text="Помилка мережі")
        print(f"Error: {e}")



# Заголовок. Колір #3b8ed0
header = CTkLabel(window, text="КАТАЛОГ ФІЛЬМІВ",
                  font=("Arial", 24, "bold"),
                  )
header.pack(pady=20)

# Фрейм для постера
poster_frame = CTkFrame(window, width=260, height=360, corner_radius=15)
poster_frame.pack_propagate(False)
poster_frame.pack(pady=16)


# Підпис (картинка)
label_poster = CTkLabel(poster_frame,
                        text="Тисни кнопку швідко, /nщоб завантажити",
                        font=("Arial", 14)
                        )
label_poster.pack(expand = True, fill="both")

# Назва шоу
label_title = CTkLabel(window,
                        text="Please, wait. . .",
                        font=("Arial", 20, "bold"),
                        wraplength=400
                        )
label_title.pack(pady=(20, 5))


# Жанр шоу
label_info = CTkLabel(window,
                        text="",
                        font=("Arial", 14),
                        text_color="gold"
                        )
label_info.pack(pady=(20, 5))


# Кнопка пошуку
btn_get = CTkButton(window,
                    text="Шкереберть",
                    height=50,
                    width=300,
                    font=("Arial", 16, "bold"),
                    command=get_random_movie
                    )
btn_get.pack(pady = 33)

# Запуск
window.mainloop()