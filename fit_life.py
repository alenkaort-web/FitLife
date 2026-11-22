# FitLife - проект приложения фитнес-бота
WATER_PER_KG = 30
ML_IN_LITER = 1000

user_name = input('Добро пожаловать! Как я могу к Вам обращаться? ')
user_age = int(input('Укажите, Ваш возраст '))

user_weight = float(input('Пожалуйста, введите Ваш вес в кг: '))
user_height = float(input('Введите Ваш рост в метрах (например: 1.75): '))
bmi = round(user_weight / (user_height ** 2), 1)
water_l = user_weight * WATER_PER_KG / ML_IN_LITER

print(f'Приветствую Вас {user_name}! Возраст: {user_age} г.')
print(f'Ваш индекс массы тела: {bmi}')
print(f'Рекомендуемая норма воды {water_l:.3f} л. в день')
print('Расчет окончен. Будьте здоровы!')
