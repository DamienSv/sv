#Создайте родительский класс Animal, у которого есть 3 атрибута:
#color - цвет
#name - кличка
#age - возраст
#и абстрактный метод:
#say - издать звук.
#Создайте два класса потомка - Cat и Dog, в которых будет переопределен метод say: для класса Cat - Meow!, для Dog - Woof!

class Animal:
    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age
    
    def say(self):
        pass       
class Cat(Animal):
    def say(self):
        return "Meow!"
        
class Dog(Animal):
    def say(self):
        return "Woof!"
        
marsik = Cat('серо-черный', 'Марсик', 6)
sobaka = Dog('белый', 'Sobaka', 5)

print(f'{marsik.name} ({marsik.color}), {marsik.age} года, говорит {marsik.say()}')
print(f'{sobaka.name} ({sobaka.color}), {sobaka.age} лет, говорит {sobaka.say()}')