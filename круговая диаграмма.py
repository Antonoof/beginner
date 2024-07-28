import matplotlib.pyplot as plt

# Пример данных
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # "взрыв" 1-го сегмента (0.1)

# Создание круговой диаграммы
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)

# Добавление заголовка
plt.title('Пример круговой диаграммы')

# Отображение графика
plt.show()
