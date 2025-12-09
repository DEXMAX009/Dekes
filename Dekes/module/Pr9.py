from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
c = Circle(5)
r = Rectangle(3, 4)

print("Площадь круга:", c.area())
print("Периметр круга:", c.perimeter())

print("Площадь прямоугольника:", r.area())
print("Периметр прямоугольника:", r.perimeter())

# Ошибка — нельзя создать абстрактный класс:
# s = Shape()  # TypeError




class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Woof!")

    def eat(self):
        print("Dog eating...")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")

    def eat(self):
        print("Cat eating...")


class Bird(Animal):
    def make_sound(self):
        print("Chirp!")

    def eat(self):
        print("Bird eating...")
d = Dog()
c = Cat()
b = Bird()

d.make_sound()
d.eat()

c.make_sound()
c.eat()

b.make_sound()
b.eat()



class PaymentSystem(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund_payment(self, payment_id, amount):
        pass


class PayPalPayment(PaymentSystem):
    def __init__(self, api_key):
        self.api_key = api_key

    def process_payment(self, amount):
        print(f"PayPal: Processing payment {amount}...")

    def refund_payment(self, payment_id, amount):
        print(f"PayPal: Refunding payment {payment_id} for {amount}...")


class StripePayment(PaymentSystem):
    def __init__(self, api_key):
        self.api_key = api_key

    def process_payment(self, amount):
        print(f"Stripe: Processing payment {amount}...")

    def refund_payment(self, payment_id, amount):
        print(f"Stripe: Refunding payment {payment_id} for {amount}...")
paypal = PayPalPayment("key123")
stripe = StripePayment("abc999")

paypal.process_payment(150)
paypal.refund_payment("TXN100", 150)

stripe.process_payment(200)
stripe.refund_payment("TXN555", 200)





class OrderProcessor(ABC):

    @abstractmethod
    def validate_order(self, order):
        pass

    @abstractmethod
    def calculate_total(self, order):
        pass

    @abstractmethod
    def process_payment(self, order):
        pass

    @abstractmethod
    def ship_order(self, order):
        pass


class StandardOrderProcessor(OrderProcessor):

    def validate_order(self, order):
        required = ["customer", "items"]
        if all(field in order for field in required):
            print("Стандартная проверка пройдена.")
            return True
        print("Ошибка: в заказе не хватает данных.")
        return False

    def calculate_total(self, order):
        total = sum(item["price"] * item["qty"] for item in order["items"])
        print(f"Стандартная сумма: {total}")
        return total

    def process_payment(self, order):
        print("Оплата обрабатывается (стандарт)...")

    def ship_order(self, order):
        print("Заказ отправлен обычной доставкой.")


class PremiumOrderProcessor(OrderProcessor):

    def validate_order(self, order):
        if order.get("vip", False) is True:
            print("VIP-проверка успешна!")
            return True
        print("Ошибка: заказ не VIP.")
        return False

    def calculate_total(self, order):
        total = sum(item["price"] * item["qty"] for item in order["items"])
        total *= 0.9  # скидка 10%
        print(f"Премиум сумма со скидкой: {total}")
        return total

    def process_payment(self, order):
        print("Оплата обработана супербыстрой системой!")

    def ship_order(self, order):
        print("Заказ отправлен ускоренной Premium-доставкой!")
order1 = {
    "customer": "Иван",
    "items": [
        {"price": 100, "qty": 2},
        {"price": 50, "qty": 1}
    ]
}

order2 = {
    "customer": "Анна",
    "items": [{"price": 200, "qty": 1}],
    "vip": True
}

standard = StandardOrderProcessor()
premium = PremiumOrderProcessor()

print("--- Стандартный заказ ---")
if standard.validate_order(order1):
    standard.calculate_total(order1)
    standard.process_payment(order1)
    standard.ship_order(order1)

print("\n--- VIP заказ ---")
if premium.validate_order(order2):
    premium.calculate_total(order2)
    premium.process_payment(order2)
    premium.ship_order(order2)
