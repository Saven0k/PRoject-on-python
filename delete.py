import log
import view
import json


# Функция для удаления заметки

# Function to delete note


def delete():
    view.view()
    log.wr2("Пользователь выбрал удалить заметку")
    op2 = int(input("Выберете id заметки для ее удаления: "))
    with open('notex.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        minimal = 0
        for i in data['notes']:
            if i["id"] == op2:
                data['notes'].pop(minimal)
            else:
                None
            minimal += 1
        with open('notex.json', 'w', encoding='utf-8') as g:
            json.dump(data, g, ensure_ascii=False, indent=4)
    print("Заметка была удалена!")
    log.wr2("Пользователь удалил заметку")
