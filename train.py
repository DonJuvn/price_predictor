import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Загружаем расширенный датасет
df = pd.read_csv("dataset.csv")
df.columns = df.columns.str.strip()  # убираем пробелы

# Признаки и целевая переменная
X = df[['ram', 'battery', 'camera', 'storage', 'processor_speed']]
y = df['price_category']

# Делим на train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Модель
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Сохраняем модель
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Проверяем точность
accuracy = model.score(X_test, y_test)
print(f"Model trained! Accuracy on test set: {accuracy:.2f}")
