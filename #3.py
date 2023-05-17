# 
class Stationery:
    def __init__(self, title):
        self.title = title  
        
    @classmethod 

    def set_color(cls, color):
        cls.color = color
    

class Pen(Stationery):
    color = 'синий'  
    
    def draw(self):  
        print('Ручка пишет')
        
class Pencil(Stationery):
    
    def draw(self):  
        print('Карандаш рисует')
        

class Handle(Stationery):
    
    def draw(self):  
        print('Маркер рисует')

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
Stationery.set_color('желтый')

print(pen.color)      
print(pencil.color)   
print(handle.color)   