class ShoppingCart:
    def __init__(self,employee_discount=None):
        self.total=0
        self.items=[]
        self.employee_discount=employee_discount
                   
    def add_item(self,item,price,quantity=1):
        self.quantity=quantity
        self.total+=price*quantity
        adding=list(range(0,quantity))
        for i in adding:
            self.items.append({'item':item,'price':price})
        return round(self.total,2)
    
    def mean_item_price(self):
        num_items = len(self.items)
        total=self.total
        mean=round(total/num_items,2)
        return mean
        
    def median_item_price(self):
        prices=[i['price'] for i in self.items]
        if len(prices)%2==0:
            median = (prices[int(len(prices)/2)-1] + prices[int(len(prices)/2)])/2
        else:
            median = prices[int(len(prices)/2)]
        return median
    
    def apply_discount(self):
        if self.employee_discount:
            discount = self.employee_discount/100
            disc_total = self.total * (1 - discount)
            return disc_total
        else:
            return "Sorry, there is no discount to apply to your cart :("
        
    def item_names(self):
        return self.items

    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= removed_item['price']