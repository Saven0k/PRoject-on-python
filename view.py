import log
import json


# Функция для просмотра всех заметок

# Function to view all notes

def view():
    log.wr2("Пользователь выбрал просмотр")
    with open('notex.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for i in data['notes']:
            print("id: " + str(i["id"]))
            print("date: " + i["date"])
            print("name: " + i["name"])
            print("text: " + i["text"])
            print(" ")
