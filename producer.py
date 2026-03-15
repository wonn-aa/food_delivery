import json
import time
from confluent_kafka import Producer
from data_gen import generate_order

# Настройка
conf = {'bootstrap.servers': 'localhost:9092'}
p = Producer(conf)

def delivery_report(err, msg):
    if err:
        print(f"Ошибка доставки: {err}")
    else:
        print(f"Успешно отправлено в топик '{msg.topic()}': {msg.value().decode('utf-8')}")

print("--- PRODUCER ЗАПУЩЕН ---")
try:
    while True:
        # Генерируем данные
        order = generate_order()
        
        # Выводим в консоль
        print(f"Генерация: {order}")
        
        # Отправляем (кодируем в JSON с поддержкой кириллицы)
        json_data = json.dumps(order, ensure_ascii=False).encode('utf-8')
        p.produce('food_delivery', value=json_data, callback=delivery_report)
        
        # ОЧЕНЬ ВАЖНО: Очищаем буфер, чтобы данные ушли сразу
        p.flush()
        
        time.sleep(3) # Пауза 3 секунды
except KeyboardInterrupt:
    print("Producer остановлен")
