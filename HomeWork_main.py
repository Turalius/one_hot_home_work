import pandas as pd

# Создаем DataFrame
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получаем уникальные категории
categories = data['whoAmI'].unique()

# Создаем новые столбцы для каждой категории и заполняем их one-hot кодировкой
for category in categories:
    data[category] = (data['whoAmI'] == category).astype(int)

# Удаляем исходный столбец 'whoAmI'
data.drop('whoAmI', axis=1, inplace=True)

data.head()
