list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Для получения индекса срединного элемента воспользуемся формулой len(list_players)//2
first_team = list_players[:len(list_players)//2]
second_team = list_players[len(list_players)//2:]

''' 
Возможен также такой вариант разделения по четным и нечётным индексам, однако тест он не проходит
first_team = list_players[::2]
second_team = list_players[1::2]'''

print(first_team)
print(second_team)
