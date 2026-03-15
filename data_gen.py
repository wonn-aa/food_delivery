import random

def generate_order():
    """Генерация данных: Рестораны, меню, клиенты, курьеры, заказы, отзывы"""
    restaurants = ["Вкусно и точка", "Додо Пицца", "Якитория", "Папа Джонс"]
    menu_items = ["Бургер Комбо", "Пицца Пепперони", "Набор Роллов", "Салат Цезарь"]
    couriers = ["Александр", "Дмитрий", "Елена", "макс"]
    
    return {
        "order_id": random.randint(1000, 9999),
        "restaurant": random.choice(restaurants),
        "item": random.choice(menu_items),
        "client": f"Client_{random.randint(1, 500)}",
        "courier": random.choice(couriers),
        "rating": random.randint(0, 5) # 0 специально для теста валидации
    }
