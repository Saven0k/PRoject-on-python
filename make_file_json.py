import json
import datetime
from random import randint
import datetime
import log




def go_note(name, text):
    new_data = {'name': name, 'id': randint(0, 123123123), 'text': text, 'date': str(datetime.datetime.now())}
    with open('notex.json', encoding='utf-8') as g:
        data = json.load(g)
        data['notes'].append(new_data)
        with open('notex.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    print("Заметка успешно добавлена\n\n\n")
    log.wr2("Заметка была  успешно добавленна!")


