print("let's cook")

#parent class
class storageRack:

    def __init__(self, rack_id, max_capacity):
        self.rack_id = rack_id
        self.max_capacity = max_capacity
        self.current_items = []
    
    def add_item(self, item_name):
        if len(self.current_items) < self.max_capacity:
            self.current_items.append(item_name)
            print (f"{item_name} added")
        else: print(f"Rack is full, {item_name} not added") 
    
class coldStorageRack(storageRack):
    def __init__(self, rack_id, max_capacity, temperature):

        super().__init__(rack_id, max_capacity)
        self.temperature = temperature
    
    def add_item(self, item_name):
        print(f"Verifying cold chain for {item_name}")
        return super().add_item(item_name) 
    
ice_rack = coldStorageRack("RACK-01", 2, -18)
ice_rack.add_item("Frozen Pizza")
ice_rack.add_item("Ice Cream")
ice_rack.add_item("Frozen Veggies")