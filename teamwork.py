# Простой To-Do List
tasks = []

while True:
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Удалить задачу")
    print("4. Выйти")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        task = input("Введите задачу: ")
        tasks.append(task)
        print("Задача добавлена!")
    
    elif choice == "2":
        if not tasks:
            print("Список задач пуст!")
        else:
            print("\nВаши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    
    elif choice == "3":
        if not tasks:
            print("Нет задач для удаления!")
        else:
            print("\nВаши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                num = int(input("Номер задачи для удаления: "))
                if 1 <= num <= len(tasks):
                    deleted = tasks.pop(num-1)
                    print(f"Задача '{deleted}' удалена!")
                else:
                    print("Неверный номер!")
            except:
                print("Введите число!")
    
    elif choice == "4":
        print("До свидания!")
        break
    
    else:
        print("Неверный выбор!")