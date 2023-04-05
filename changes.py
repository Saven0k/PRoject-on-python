import log
import view
import datetime
import json
import make_file_json


# Функция для изменения заметок

# Function to change notes



def find_and_change():
    view.view()
    log.wr2("Пользователь выбрал изменить заметку")
    op3 = int(input("Выберете id заметки для ее измнения\n :"))
    with open('notex.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        minimal = 0
        for i in data['notes']:
            if i["id"] == op3:
                doing = int(input("Что хотите сделать:\n1 - изменить текст \n2 - изменить название\n : "))

                if doing == 1:
                    text_sc = str(input("Введите текст, который хотите поменять\n :"))
                    i["text"] = str(text_sc)

                else:
                    name_sc = str(input("Введите название, который хотите поменять\n :"))
                    i["name"] = str(name_sc)


            else:
                None
            minimal += 1
        with open('notex.json', 'w', encoding='utf-8') as g:
            json.dump(data, g, ensure_ascii=False, indent=4)
    print("Заметка была изменена")
    log.wr2("Пользователь изменил заметку")
