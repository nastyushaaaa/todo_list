# Консольное приложение
tasks = []

def add_task(title):
    if not title.strip():
        print("Название задачи не может быть пустым!")
        return False

    tasks.append({"title": title, "completed": False})
    print("Задача добавлена!")
    return True

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Задача удалена!")
    else:
        print("Задача не найдена!")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Задача выполнена!")
    else:
        print("Задача не найдена!")

def show_tasks():
    if not tasks:
        print("Список задач пуст.")
        return

    for i, task in enumerate(tasks):
        status = "Выполнена" if task["completed"] else "Не выполнена"
        print(f"{i}. {task['title']} — {status}")

def main():
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Выполнить задачу")
        print("4. Показать задачи")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите задачу: ")
            add_task(title)

        elif choice == "2":
            index = int(input("Введите номер задачи: "))
            delete_task(index)

        elif choice == "3":
            index = int(input("Введите номер задачи: "))
            complete_task(index)

        elif choice == "4":
            show_tasks()

        elif choice == "5":
            print("Завершение программы.")
            break

        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
