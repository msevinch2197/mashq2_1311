class Product:
    def __init__(self, nom, narx, zaxira_soni_maxfiy):
        self.nom = nom
        self.narx = narx
        self._zaxira_soni = zaxira_soni_maxfiy 
    def get_stock(self):
        if isinstance(self, InventoryManager):
            return "maxfiy"
        else:
            return self._zaxira_soni

    def purchase(self):
        """Mijozlar uchun: foydalanganingda zaxira kamayib borsin."""
        if self._zaxira_soni > 0:
            self._zaxira_soni -= 1
        else:
            raise ValueError("Mahsulot tugagan! Sotuvda yo'q.")

    def __str__(self):
        """Mahsulot tugasa, 'sotuvda yo'q' deb chiqsin."""
        if self._zaxira_soni <= 0:
            return f"{self.nom} - sotuvda yo'q"
        else:
            return f"{self.nom} - Narxi: {self.narx}, Zaxirada: {self._zaxira_soni}"


class InventoryManager(Product):
    pass  
product = Product("Laptop", 1200, 5)
inventory_manager = InventoryManager("Mouse", 25, 10)

print(product)              
print(inventory_manager)    


print(f"Zaxira soni (mijoz): {product.get_stock()}")          
print(f"Zaxira soni (manager): {inventory_manager.get_stock()}") 


product.purchase()
print(product)  


for _ in range(5):
    product.purchase()

print(product)  

try:
    product.purchase()  
except ValueError as e:
    print(e)  
