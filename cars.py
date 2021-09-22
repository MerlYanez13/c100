class cars(object):
    def __init__(self,model,color, company ,speed): 
        self.company=company
        self.model=model
        self.color=color
        self.speed=speed
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def change(self,level):
        print("gear changed")

audi=cars("a6","purple","audi",120)
audi.start()
audi.stop()
audi.change(5)