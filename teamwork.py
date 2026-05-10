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









я ебал эито все

    
  
  
