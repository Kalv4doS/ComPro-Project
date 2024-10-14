inventory = {
    "Sneakers": [],
    "Formal Shoes": [],
    "Sandals": [],
    "Boots": []
}

def add_item(category, shoe_id, name, price, quantity):
    item = {
        "ID": shoe_id,
        "Name": name,
        "Price": price,
        "Quantity": quantity
    }
    inventory[category].append(item)

def show_all():
    total_price = 0
    total_quantity = 0

    for category, items in inventory.items():
        category_price = sum(item['Price'] * item['Quantity'] for item in items)
        category_quantity = sum(item['Quantity'] for item in items)
        total_price += category_price
        total_quantity += category_quantity
        
        print(f"หมวดหมู่: {category}")
        print("-" * 60)
        print(f"{'ID':<5} {'Name':<30} {'Price':<10} {'Quantity':<10}")
        print("-" * 60)
        for item in items:
            print(f"{item['ID']:<5} {item['Name']:<30} {item['Price']:<10} {item['Quantity']:<10}")
        print(f"รวมหมวดหมู่ {category} -> ราคารวม: {category_price:.2f}, จำนวนรวม: {category_quantity}")
        print("=" * 60)

    print("สรุปรวมทั้งหมด")
    print("-" * 60)
    print(f"ราคารวมทั้งหมด: {total_price:.2f}")
    print(f"จำนวนรวมทั้งหมด: {total_quantity}")
    print("-" * 60)

def find_item(shoe_id):
    for category, items in inventory.items():
        for item in items:
            if item['ID'] == shoe_id:
                return item
    return None

def update_item(shoe_id, new_price=None, new_quantity=None):
    for category, items in inventory.items():
        for item in items:
            if item['ID'] == shoe_id:
                if new_price is not None:
                    item['Price'] = new_price
                if new_quantity is not None:
                    item['Quantity'] = new_quantity
                return True
    return False

def delete_item(shoe_id):
    for category, items in inventory.items():
        for item in items:
            if item['ID'] == shoe_id:
                items.remove(item)
                return True
    return False

def add_data():
    category = input("Enter category: ")
    shoe_id = int(input("Enter shoe ID: "))
    name = input("Enter shoe name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    add_item(category, shoe_id, name, price, quantity)
    print("Item added successfully.")

def search_data():
    shoe_id = int(input("Enter shoe ID to find: "))
    item = find_item(shoe_id)
    if item:
        print("Found item:", item)
    else:
        print("Item not found.")

def update_data():
    shoe_id = int(input("Enter shoe ID to update: "))
    new_price = input("Enter new price (leave blank to skip): ")
    new_quantity = input("Enter new quantity (leave blank to skip): ")
    new_price = float(new_price) if new_price else None
    new_quantity = int(new_quantity) if new_quantity else None
    if update_item(shoe_id, new_price, new_quantity):
        print("Item updated successfully.")
    else:
        print("Item not found.")

def delete_data():
    shoe_id = int(input("Enter shoe ID to delete: "))
    if delete_item(shoe_id):
        print("Item deleted successfully.")
    else:
        print("Item not found.")

def exit_program():
    print("Exiting program...")
    exit()

def main():
    while True:
        print("\n1. Add new data")
        print("2. Show all data")
        print("3. Search specific data")
        print("4. Update data")
        print("5. Delete data")
        print("6. Exit program")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_data()
        elif choice == '2':
            show_all()
        elif choice == '3':
            search_data()
        elif choice == '4':
            update_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
