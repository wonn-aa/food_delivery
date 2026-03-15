import json
from confluent_kafka import Consumer

# Настройка
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'delivery_consumer_group_v2', # Новое имя группы, чтобы прочитать всё с начала
    'auto.offset.reset': 'earliest'           # Читать старые сообщения, если они были
}
c = Consumer(conf)
c.subscribe(['food_delivery'])

def is_valid(data):
    # Валидация: заказ считается валидным, если рейтинг выше 0
    return data.get('rating', 0) > 0

print("--- CONSUMER ЗАПУЩЕН. ОЖИДАНИЕ ДАННЫХ... ---")
try:
    while True:
        msg = c.poll(1.0) # Ждем сообщение 1 секунду
        
        if msg is None:
            continue
        if msg.error():
            print(f"Ошибка Consumer: {msg.error()}")
            continue

        # Декодируем JSON
        order_data = json.loads(msg.value().decode('utf-8'))
        
        # Валидация и вывод
        if is_valid(order_data):
            print(f"ПОЛУЧЕНО: {order_data}")
        else:
            print(f"СООБЩЕНИЕ: {order_data} -> NOT VALID (Низкий рейтинг)")
            
except KeyboardInterrupt:
    print("Consumer остановлен")
finally:
    c.close()
