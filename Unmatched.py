import random
import time

def print_text(text):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(0.01)
    print()

arr_excep = ["Шапка", "Т-рэкс", "Рапторы", "Том2", "Гудини vs. Джинн"]
arr_pers = ["Красная шапочка", "Беовульф", "Робин Гуд", "Бигфут", "Дракула", "Человек-невидимка", "Шеролок Холмс",
            "Джекил и Хайд", "Медуза", "Король Артур", "Симбад", "Алиса", "Deadpool", "Т-рэкс", "Малдун", "Рапторы", "Доктор Сэттлер", "Золотой Крылан" , "Энни Кристмас", "Джилл Трент", "Никола Тесла", "Гудини", "Джинн", "Ахиллес", "Йенненгой", "Кровавая Мэри", "Сунь Укун"]
arr_map = ["Том 1", "Битва легенд", "Шапка", "Робингуд", "Т-рэкс", "Рапторы", "Том2", "Гудини vs. Джинн"]
arr_gamers = ["Катя", "Дима"]
arr_map_front = ["чёт", "нечёт"]
for _ in range(5):
    random.shuffle(arr_pers)

for _ in range(5):
    random.shuffle(arr_map)

for _ in range(5):
    print('.', end='', flush=True)
    time.sleep(0.1)

print()

while True:
    first = random.choice(arr_pers)
    text = "Екатерина играет за персонажа " + first
    second = random.choice(arr_pers)
    while (second == first):
        second = random.choice(arr_pers)
    print_text(text)
    text = "Дмитрий играет за персонажа " + second
    print_text(text)
    play_map = random.choice(arr_map)
    count = 0
    for i in arr_excep:
        if i == play_map:
            count+=1
	
    text = "Карта " + play_map + ' ' +(' ' if 0!= count else random.choice(arr_map_front))
    print_text(text)
    text = "первый игрок " + random.choice(arr_gamers)
    print_text(text)
    if input("Введите (В)ыход  ").upper() == 'В':
        berak
print_text("Приятной иргы                       ")