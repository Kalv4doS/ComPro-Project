class ShoeInventory:
    def __init__(self):
        self.inventory = {
            "Sneakers": [],
            "Formal Shoes": [],
            "Sandals": [],
            "Boots": []
        }

    def add_item(self, category, shoe_id, name, price, quantity):
        item = {
            "ID": shoe_id,
            "Name": name,
            "Price": price,
            "Quantity": quantity
        }
        self.inventory[category].append(item)

    def show_all(self):
        total_price = 0
        total_quantity = 0

        for category, items in self.inventory.items():
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

    def find_item(self, shoe_id):
        for category, items in self.inventory.items():
            for item in items:
                if item['ID'] == shoe_id:
                    return item
        return None

    def update_item(self, shoe_id, new_price=None, new_quantity=None):
        for category, items in self.inventory.items():
            for item in items:
                if item['ID'] == shoe_id:
                    if new_price is not None:
                        item['Price'] = new_price
                    if new_quantity is not None:
                        item['Quantity'] = new_quantity
                    return True
        return False

    def delete_item(self, shoe_id):
        for category, items in self.inventory.items():
            for item in items:
                if item['ID'] == shoe_id:
                    items.remove(item)
                    return True
        return False

# การใช้งาน
inventory = ShoeInventory()

# เพิ่มข้อมูล
inventory.add_item("Sneakers", 7, "Nike Air Max", 229.0, 2)
inventory.add_item("Sneakers", 8, "Adidas Ultraboost", 669.0, 2)
inventory.add_item("Formal Shoes", 5, "Oxford Shoes", 199.0, 1)
inventory.add_item("Formal Shoes", 6, "Derby Shoes", 369.0, 2)
inventory.add_item("Sandals", 3, "Flip Flops", 90.0, 12)
inventory.add_item("Sandals", 4, "Birkenstock Sandals", 160.0, 4)
inventory.add_item("Boots", 1, "Timberland Boots", 60.0, 2)
inventory.add_item("Boots", 2, "Dr. Martens", 60.0, 2)

# แสดงข้อมูลทั้งหมด
inventory.show_all()

# ค้นหารองเท้าตาม ID
found_item = inventory.find_item(7)
print("\nค้นหารองเท้า ID 7:", found_item)

# อัปเดตข้อมูล
inventory.update_item(8, new_price=700.0, new_quantity=1)

# ลบข้อมูล
inventory.delete_item(1)

# แสดงข้อมูลทั้งหมดหลังจากอัปเดตและลบ
inventory.show_all()
