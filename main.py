import log
import add_new_note
import changes
import delete
import view

#   Промежуточная аттестация

#  Приложение заметки


# Фаил main  в котором прописан все возможности


print("                     Заметки(notes)                         ")

log.wr("start")


# make_file_json.start()


def main():
    print(
        "Выберете что хотите сделать\n1 - Посмотреть заметки \n2 - Сделать новоую заметку \n3 - Удалить заметку \n4 - Изменить заметку\n0 - Выйти ")

    operation = int(input(": "))
    print("\n\n")
    while operation != 0:
        if operation == 1:
            view.view()  # Решил попробывать сделать так, вроде все по правилам solid, если есть какие то недочеты прошу сообщить о них
            main()
        elif operation == 2:
            add_new_note.add()
            main()

        elif operation == 3:
            delete.delete()
            main()

        elif operation == 4:
            changes.find_and_change()
            main()
        else:
            print("Eror\n\n")
            main()

    print("Пока! Bye!!")
    log.wr2("close programm")
    exit()


main()
