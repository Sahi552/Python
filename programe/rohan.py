class laptop():
    def __init__(self):
        self.price = 0
        self.ram = ""
        self.proces = ""
    def display(self):
        print("Display")
        
hp=laptop()
hp.ram=" 8GB "
hp.price = 20000
hp.proces = "intel i5"
dell=laptop()
dell.ram=" 16GB "
dell.price = 30000
dell.proces = "amd 5500"
print(hp.ram)
print(hp.price)
print(hp.proces)
print(dell.ram)
print(dell.price)
print(dell.proces)