import pandas as pd

#Импортируйте библиотеку pandas как pd. Прочитайте датасет bookings.csv
# с разделителем ;

df = pd.read_csv('2_bookings.csv', encoding="windows-1251", sep=";")
df.shape
df.dtypes
df.head()

#приведите названия столбцов к нижнему регистру и замените пробелы на знак нижнего подчёркивания
row, cols = df.shape
rename_cols = {}
for col in df.columns:
    rename_cols[col] = col.replace(' ', '_').lower()
rename_cols
df = df.rename(columns=rename_cols)

#Пользователи из каких стран совершили наибольшее число успешных бронирований?
df.loc[df.is_canceled == 0].country.value_counts().head(5)

#На сколько ночей (stays_total_nights)  в среднем бронируют отели типа City Hotel? Resort Hotel?
df.groupby('hotel').stays_total_nights.mean().round(2)

 #Иногда тип номера, полученного клиентом (assigned_room_type),
# отличается от изначально забронированного (reserved_room_type).
# Такое может произойти, например, по причине овербукинга.
# Сколько подобных наблюдений встретилось в датасете?
len(df.loc[df.assigned_room_type != df.reserved_room_type])

#На какой месяц чаще всего успешно оформляли бронь в 2016 году? Изменился ли самый популярный месяц в 2017?
df.groupby('arrival_date_year').arrival_date_month.agg(pd.Series.mode)

# на какой месяц (arrival_date_month) бронирования отеля типа City Hotel отменялись чаще всего в 2015, 2016 и 2017 годах.
df.groupby(['arrival_date_year', 'arrival_date_month']).is_canceled.sum()
df.groupby(['arrival_date_year', 'arrival_date_month']).is_canceled.sum().groupby(['arrival_date_year']).nlargest(1)

#Посмотрите на числовые характеристики трёх переменных: adults, children и babies
df[['adults', 'children', 'babies']].mean().round(2)

#Создайте колонку total_kids, объединив столбцы children и babies.
#Для отелей какого типа среднее значение переменной оказалось наибольшим?
df['total_kids'] = df.children + df.babies
df.groupby('hotel').total_kids.mean().round(2)

