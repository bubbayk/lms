def load_list_from_file(file_path):
    items = {}
    with open(file_path, 'r') as file:
        for line in file:
            name, amount = line.strip().split(',')
            items[name] = int(amount)
    return items


def save_list_to_file(file_path, items):
    with open(file_path, 'w') as file:
        for name, amount in items.items():
            file.write(f"{name},{amount}\n")

def add_item(items, file_path):
    name = input("Введіть назву продукту: ")
    amount = int(input("Введіть кількість: "))
    items[name] = amount
    print("Продукт успішно додано до списку.")


    save_list_to_file(file_path, items)

def display_items(items):
    print("Ваш список покупок:")
    for name, amount in items.items():
        print(f"{name}: {amount}")

def remove_item(items, file_path):
    name = input("Введіть назву продукту, який бажаєте видалити: ")
    if name in items:
        del items[name]
        print("Продукт видалено зі списку.")


        save_list_to_file(file_path, items)
    else:
        print("Продукт не знайдено у списку.")

def main():
    file_path = "shopping_list.txt"
    items = load_list_from_file(file_path)

    while True:
        choice = input("Що ви хочете зробити? (додати, переглянути, видалити, вийти): ")
        if choice == "додати":
            add_item(items, file_path)  
        elif choice == "переглянути":
            display_items(items)  
        elif choice == "видалити":
            remove_item(items, file_path)  
        elif choice == "вийти":
            print("Дякую за використання програми!")
            break
if __name__ == "__main__":
    main()
