"""
Напишите программу с классом Math. Создайте два атрибута — a и b.
Напишите методы addition — сложение, multiplication — умножение, division — деление, subtraction — вычитание.
При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.
"""

# class Math:
#     def addition(self, a, b):
#         return a + b
#     # def __repr__(self):
#
#
#     def multiplication(self, a, b):
#         return a - b
#
#     def division(self, a, b):
#         return a * b
#
#     def subtraction(self, a, b):
#         return a / b
#
#
# math_1 = Math()
# print(math_1.addition(4, 6))
# print(math_1.multiplication(7, 5))
# print(math_1.division(3, 5))
# print(math_1.subtraction(6, 2))


"""
# Ресторан: создайте класс с именем Restaurant. Метод __init__() класса Restaurant должен содержать два
# атрибута: restaurant_name и cuisine_type. Создайте метод describe_ restaurant(), который выводит два атрибута,
# и метод open_restaurant(), который выводит сообщение о том, что ресторан открыт.
# Создайте на основе своего класса экземпляр с именем restaurant. Выведите два атрибута по отдельности, затем
# вызовите оба метода.
"""

class Restaurant:
    def __init__(self, retaurant_name, cuisine_type,):
        self.name = retaurant_name
        self.type = cuisine_type
        self.number_served = 0


    def __str__(self):
        return f"{self.name}, {self.type}"



    def describe_restaurant(self, menu, price):
        # menu = menu
        # cost = price
        return menu, price


    def open_restaurant(self, open):
         return f"{self.name} is open"




    def set_number_served(self, number):
        self.number_served = number
        return self.number_served


    def increment_number_served(self, number):
        self.number_served += number
        return self.number_served



restaurant = Restaurant("Alpachino", "Italian")
print(restaurant.number_served)
print(restaurant.set_number_served(100))
print(restaurant.increment_number_served(50))

# print(restaurant.describe_restaurant("Chicken Alfredo", 467))
#
# print(restaurant.open_restaurant("open"))


"""
Пользователи: создайте класс с именем User. Создайте два атрибута first_name и last_name, 
а затем еще несколько атрибутов, которые обычно хранятся в профиле пользователя. 
Напишите метод describe_user(), который выводит сводку с информацией о пользователе. 
Создайте еще один метод greet_user() для вывода персонального приветствия для пользователя.
Создайте несколько экземпляров, представляющих разных пользователей. Вызовите оба метода для каждого пользователя

"""

# class User:
#     def __init__(self, first_name, last_name, age, married):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.married = married
#         self.followers = []
#
#     def add_follower(self, follower):
#         self.followers.append(follower)
#
#     def __repr__(self):
#         return f"{self.first_name}" \
#                f"{self.last_name}" \
#                f"{self.age}" \
#                f"{self.married}"

#     def describe_user(self, work, drive):
#         return work, drive
#
#     def greet_user(self):
#         return "Welcome to Codify"
#
# user = User("Matt ", "Boss ", "31 ", True,)
# print(user)
# print(user.describe_user("Power Engeenering", "Honda Accord"))
# print(user.greet_user())
#
# user_1 = User("Nick ", "Steve ", "30 ", False)
# user_2 = User("Bakyt ", "Omorov ", "21 ", True)
# user_3 = User("Ulan ", "Bekov ", "25 ", True)
#
# user.add_follower(user_1)
# user.add_follower(user_2)
# user.add_follower(user_3)
#
# print(user.followers, end=",")


"""

Создайте класс Soda (для определения типа газированной воды), 
принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). 
В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, 
а иначе отобразится следующая фраза: «Обычная газировка».

"""

# class Soda:
#     def __init__(self, additive=None):
#         self.additive = additive
#
#     def show_my_drink(self):
#         if self.additive is None:
#             return "Обычная газировка"
#
#         else:
#             return f"Газировка и {self.additive}"
#
#
#
# soda = Soda()
# print(soda.show_my_drink())
# soda2 = Soda("lemon")
# print(soda.show_my_drink())


"""
Посетители: начните с программы из упражнения 9.1 (с. 175). Добавьте атрибут number_served со значением по умолчанию 0;
 он представляет количество обслуженных посетителей. Создайте экземпляр с именем restaurant. 
 Выведите значение number_served, потом измените и выведите снова.
Добавьте метод с именем set_number_served(), позволяющий задать количество обслуженных посетителей. 
Вызовите метод с новым числом, снова выведите значение.
Добавьте метод с именем increment_number_served(), 
который увеличивает количество обслуженных посетителей на заданную величину. 
Вызовите этот метод с любым числом, которое могло бы представлять количество обслуженных клиентов, — скажем, за один день.
"""













