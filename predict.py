import pandas as pd
import pickle

# Загружаем модель
with open('mobile_model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_phone_price(features: dict) -> float:
    """
    Возвращает предсказанную цену телефона (в тенге)
    """
    df = pd.DataFrame([features])
    predicted_price = model.predict(df)[0]
    return round(predicted_price, 2)

# Пример использования
new_phone = {
    'battery_power': 200,
    'blue': 1,
    'clock_speed': 2.4,
    'dual_sim': 1,
    'fc': 8,
    'four_g': 1,
    'int_memory': 64,
    'm_dep': 0.7,
    'mobile_wt': 160,
    'n_cores': 8,
    'pc': 16,
    'px_height': 1080,
    'px_width': 2400,
    'ram': 6000,
    'sc_h': 15,
    'sc_w': 7,
    'talk_time': 24,
    'three_g': 1,
    'touch_screen': 1,
    'wifi': 1
}

print(f"Примерная цена телефона: {predict_phone_price(new_phone)} ₸")
