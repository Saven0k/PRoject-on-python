import log
import json
import datetime
import make_file_json


# Функция для поиска и изменения заметок

# Function for searching and changing notes


def add():
    log.wr2("Пользователь выбрал создать новую заметку")
    name_n = input("Введите название заметки: ")
    text = input("Введите текст заметки: ")
    log.wr2(f"Пользователь добавил заметку с название {name_n}, text - {text}")
    make_file_json.go_note(name_n, text)
