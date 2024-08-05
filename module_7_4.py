team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
# Использование %:
print("В команде Мастера кода участников: %d !" % team1_num)
# Использование % с двумя переменными:
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))
# Использование format():
print("Команда Волшебники данных решила задач: {} !".format(score2))
# Использование format() с форматированием времени:
print("Волшебники данных решили задачи за {:.1f} с !".format(team1_time))
# Использование f-строк:
print(f"Команды решили {score1} и {score2} задач.")
# Использование f-строк с переменной challenge_result:
challenge_result = 'Победа команды Волшебники данных!'
print(f"Результат битвы: {challenge_result}")
# Использование f-строк с переменными tasks_total и time_avg:
tasks_total = score1 + score2
time_avg = round((team2_time + team1_time) / 82, 1)
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу.")
