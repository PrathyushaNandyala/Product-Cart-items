class Product:
    
    def __init__(self,Name,Price,deal_price,ratings):
        self.Name=Name
        self.Price=Price
        self.deal_price=deal_price
        self.ratings=ratings
        self.you_saved=Price-deal_price
        
    def display_product_details(self):
        print('Product Name:{}'.format(self.Name))
        print('Price: {}'.format(self.Price))
        print('deal_price:{}'.format(self.deal_price))
        print('ratings:{}'.format(self.ratings))
        print('You_saved:{}'.format(self.you_saved))
        
        
        
        
class Electronic_item(Product):
    
    def set_warranty(self,warranty_in_months):
        self.waranty_in_months=warranty_in_months
        
    def get_warranty(self):
        print('warranty in months:{}'.format(self.waranty_in_months))
        print("--------------***-----------------")


class Grocery_item(Product):
    def set_expiry_date(self,expiry_date):
        self.expiry_date=expiry_date
        
    def get_expiry_date(self):
        print('expiry_date:{}'.format(self.expiry_date))
        print("--------------***-----------------")
        
        
        
e_item=Electronic_item('Camara',30000,25000,4)
e_item.set_warranty(24)
e_item.display_product_details()   
e_item.get_warranty()
        
        
g_item=Grocery_item('biscuites',30,25,4.5)
g_item.set_expiry_date('best before 12 months from mfg')
g_item.display_product_details()   
g_item.get_expiry_date()