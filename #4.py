# Создаем базовый класс User
class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    # Метод view для просмотра содержимого
    def view(self):
        print("Я - User. Могу просматривать содержимое")

# Создаем дочерний класс Moderator
class Moderator(User):
    def __init__(self, login, password, group_id):
        # Вызываем конструктор родительского класса
        super().__init__(login, password)
        self.group_id = group_id

    # Переопределяем метод view
    def view(self):
        # Вызываем метод view родительского класса
        super().view()
        print("Я - Moderator. Могу просматривать содержимое")

    # Метод redact для редактирования содержимого
    def redact(self):
        print("Я - Moderator. Могу редактировать содержимое")

# Создаем объекты классов
user = User("user_login", "user_password")
moderator = Moderator("moderator_login", "moderator_password", "123")

# Вызываем методы объектов
user.view() # Выводит "Я - User. Могу просматривать содержимое"
moderator.view() # Выводит "Я - User. Могу просматривать содержимое" и "Я - Moderator. Могу просматривать содержимое"
moderator.redact() # Выводит "Я - Moderator. Могу редактировать содержимое"