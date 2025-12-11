import random
import pandas as pd
from datetime import datetime

def generate_phone_dataset(num_records=500):
    """
    Генерирует датасет характеристик мобильных телефонов.
    
    Args:
        num_records: количество записей для генерации (по умолчанию 500)
    
    Returns:
        DataFrame с характеристиками телефонов
    """
    # Инициализация списков для каждого столбца
    battery_power = []
    blue = []
    clock_speed = []
    dual_sim = []
    fc = []
    four_g = []
    int_memory = []
    m_dep = []
    mobile_wt = []
    n_cores = []
    pc = []
    px_height = []
    px_width = []
    ram = []
    sc_h = []
    sc_w = []
    talk_time = []
    three_g = []
    touch_screen = []
    wifi = []
    price_range_tenge = []
    
    for _ in range(num_records):
        # Генерация базовых характеристик
        # Определяем случайный класс телефона для сохранения логики
        phone_class = random.choice(['budget', 'mid', 'high', 'flagship'])
        
        if phone_class == 'budget':
            # Бюджетные телефоны
            battery = random.randint(600, 1200)
            ram_val = random.randint(512, 3072)
            px_h = random.randint(480, 1280)
            px_w = random.randint(640, 1920)
            price = random.randint(40000, 150000)
            memory = random.choice([4, 8, 16, 32])
            cores = random.choice([2, 4])
            pc_val = random.randint(0, 8)
            fc_val = random.randint(0, 5)
            weight = random.randint(180, 230)
            thickness = round(random.uniform(0.5, 0.9), 2)
            screen_h = random.randint(8, 12)
            screen_w = random.randint(4, 7)
            talk = random.randint(8, 18)
            
        elif phone_class == 'mid':
            # Средний класс
            battery = random.randint(1000, 1800)
            ram_val = random.randint(2048, 6144)
            px_h = random.randint(720, 1920)
            px_w = random.randint(1280, 2560)
            price = random.randint(120000, 300000)
            memory = random.choice([32, 64, 128])
            cores = random.choice([4, 6])
            pc_val = random.randint(5, 16)
            fc_val = random.randint(5, 12)
            weight = random.randint(150, 190)
            thickness = round(random.uniform(0.6, 0.9), 2)
            screen_h = random.randint(12, 15)
            screen_w = random.randint(6, 8)
            talk = random.randint(12, 22)
            
        elif phone_class == 'high':
            # Высокий класс
            battery = random.randint(1600, 2500)
            ram_val = random.randint(4096, 9216)
            px_h = random.randint(1080, 2160)
            px_w = random.randint(1920, 3840)
            price = random.randint(250000, 500000)
            memory = random.choice([128, 256])
            cores = 8
            pc_val = random.randint(12, 25)
            fc_val = random.randint(10, 25)
            weight = random.randint(140, 170)
            thickness = round(random.uniform(0.7, 1.0), 2)
            screen_h = random.randint(15, 17)
            screen_w = random.randint(8, 9)
            talk = random.randint(18, 28)
            
        else:  # flagship
            # Флагманы
            battery = random.randint(2000, 3500)
            ram_val = random.randint(8192, 16384)
            px_h = random.randint(1440, 4000)
            px_w = random.randint(2560, 5120)
            price = random.randint(450000, 800000)
            memory = random.choice([256, 512])
            cores = 8
            pc_val = random.randint(20, 40)
            fc_val = random.randint(20, 40)
            weight = random.randint(130, 160)
            thickness = round(random.uniform(0.8, 1.2), 2)
            screen_h = random.randint(16, 19)
            screen_w = random.randint(9, 11)
            talk = random.randint(20, 35)
        
        # Добавляем небольшую случайность к некоторым параметрам
        battery += random.randint(-50, 50)
        price += random.randint(-10000, 10000)
        
        # Генерация бинарных признаков с логикой
        bluetooth = random.randint(0, 1)
        dual_sim_val = random.randint(0, 1)
        three_g_val = random.randint(0, 1)
        
        # 4G обычно есть, если есть 3G, но не всегда
        if three_g_val == 1:
            four_g_val = random.choices([0, 1], weights=[0.2, 0.8])[0]
        else:
            four_g_val = 0
            
        touch_val = 1 if price > 80000 else random.randint(0, 1)
        wifi_val = 1 if price > 60000 else random.randint(0, 1)
        
        # Тактовая частота (логика: чем выше класс, тем выше частота)
        if phone_class == 'budget':
            clock = round(random.uniform(1.0, 1.8), 2)
        elif phone_class == 'mid':
            clock = round(random.uniform(1.6, 2.4), 2)
        elif phone_class == 'high':
            clock = round(random.uniform(2.0, 2.8), 2)
        else:  # flagship
            clock = round(random.uniform(2.4, 3.2), 2)
        
        # Добавляем данные в списки
        battery_power.append(battery)
        blue.append(bluetooth)
        clock_speed.append(clock)
        dual_sim.append(dual_sim_val)
        fc.append(fc_val)
        four_g.append(four_g_val)
        int_memory.append(memory)
        m_dep.append(thickness)
        mobile_wt.append(weight)
        n_cores.append(cores)
        pc.append(pc_val)
        px_height.append(px_h)
        px_width.append(px_w)
        ram.append(ram_val)
        sc_h.append(screen_h)
        sc_w.append(screen_w)
        talk_time.append(talk)
        three_g.append(three_g_val)
        touch_screen.append(touch_val)
        wifi.append(wifi_val)
        price_range_tenge.append(price)
    
    # Создаем DataFrame
    data = {
        'battery_power': battery_power,
        'blue': blue,
        'clock_speed': clock_speed,
        'dual_sim': dual_sim,
        'fc': fc,
        'four_g': four_g,
        'int_memory': int_memory,
        'm_dep': m_dep,
        'mobile_wt': mobile_wt,
        'n_cores': n_cores,
        'pc': pc,
        'px_height': px_height,
        'px_width': px_width,
        'ram': ram,
        'sc_h': sc_h,
        'sc_w': sc_w,
        'talk_time': talk_time,
        'three_g': three_g,
        'touch_screen': touch_screen,
        'wifi': wifi,
        'price_range_tenge': price_range_tenge
    }
    
    df = pd.DataFrame(data)
    return df

def save_dataset(df, filename='mobile_phones_dataset.csv'):
    """Сохраняет датасет в CSV файл."""
    df.to_csv(filename, index=False)
    print(f"Датасет сохранен в файл: {filename}")
    print(f"Размер датасета: {df.shape[0]} строк, {df.shape[1]} столбцов")

def main():
    # Генерация датасета
    print("Генерация датасета характеристик мобильных телефонов...")
    df = generate_phone_dataset(3000)
    
    # Показать первые 10 строк
    print("\nПервые 10 строк датасета:")
    print(df.head(10))
    
    # Базовая статистика
    print("\nБазовая статистика по цене:")
    print(df['price_range_tenge'].describe())
    
    # Распределение по классам (примерно)
    print("\nРаспределение ценовых диапазонов:")
    price_bins = [0, 100000, 200000, 350000, 500000, 1000000]
    price_labels = ['Ultra-budget', 'Budget', 'Mid-range', 'High-end', 'Flagship']
    df['price_category'] = pd.cut(df['price_range_tenge'], bins=price_bins, labels=price_labels)
    print(df['price_category'].value_counts())
    
    # Сохранение в файл
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"mobile_phones_500_{timestamp}.csv"
    save_dataset(df, filename)
    
    # Также сохраняем без timestamp для простоты
    save_dataset(df, "mobile_phones_500.csv")
    
    return df

if __name__ == "__main__":
    df = main()
    
    # Дополнительная информация
    print("\n" + "="*50)
    print("Структура датасета:")
    print(df.info())
    
    print("\nПримеры из разных ценовых категорий:")
    # Показать по одному примеру из каждой категории
    for category in ['Ultra-budget', 'Budget', 'Mid-range', 'High-end', 'Flagship']:
        if category in df['price_category'].values:
            sample = df[df['price_category'] == category].iloc[0]
            print(f"\n{category} (цена: {sample['price_range_tenge']} тг):")
            print(f"  RAM: {sample['ram']}MB, Память: {sample['int_memory']}GB")
            print(f"  Камера: {sample['pc']}MP, Экран: {sample['sc_h']}x{sample['sc_w']} см")
            print(f"  Батарея: {sample['battery_power']}mAh, Вес: {sample['mobile_wt']}г")