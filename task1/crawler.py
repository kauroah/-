import requests
import os

# List of Russian Wikipedia pages
urls = [
"https://ru.wikipedia.org/wiki/Россия",
"https://ru.wikipedia.org/wiki/Москва",
"https://ru.wikipedia.org/wiki/Санкт-Петербург",
"https://ru.wikipedia.org/wiki/Казань",
"https://ru.wikipedia.org/wiki/Новосибирск",
"https://ru.wikipedia.org/wiki/Екатеринбург",
"https://ru.wikipedia.org/wiki/Нижний_Новгород",
"https://ru.wikipedia.org/wiki/Самара",
"https://ru.wikipedia.org/wiki/Омск",
"https://ru.wikipedia.org/wiki/Челябинск",
"https://ru.wikipedia.org/wiki/Ростов-на-Дону",
"https://ru.wikipedia.org/wiki/Уфа",
"https://ru.wikipedia.org/wiki/Красноярск",
"https://ru.wikipedia.org/wiki/Воронеж",
"https://ru.wikipedia.org/wiki/Пермь",
"https://ru.wikipedia.org/wiki/Волгоград",
"https://ru.wikipedia.org/wiki/Краснодар",
"https://ru.wikipedia.org/wiki/Саратов",
"https://ru.wikipedia.org/wiki/Тюмень",
"https://ru.wikipedia.org/wiki/Тольятти",
"https://ru.wikipedia.org/wiki/Ижевск",
"https://ru.wikipedia.org/wiki/Барнаул",
"https://ru.wikipedia.org/wiki/Иркутск",
"https://ru.wikipedia.org/wiki/Хабаровск",
"https://ru.wikipedia.org/wiki/Ярославль",
"https://ru.wikipedia.org/wiki/Владивосток",
"https://ru.wikipedia.org/wiki/Махачкала",
"https://ru.wikipedia.org/wiki/Томск",
"https://ru.wikipedia.org/wiki/Оренбург",
"https://ru.wikipedia.org/wiki/Кемерово",
"https://ru.wikipedia.org/wiki/Новокузнецк",
"https://ru.wikipedia.org/wiki/Рязань",
"https://ru.wikipedia.org/wiki/Астрахань",
"https://ru.wikipedia.org/wiki/Пенза",
"https://ru.wikipedia.org/wiki/Липецк",
"https://ru.wikipedia.org/wiki/Тула",
"https://ru.wikipedia.org/wiki/Киров",
"https://ru.wikipedia.org/wiki/Чебоксары",
"https://ru.wikipedia.org/wiki/Калининград",
"https://ru.wikipedia.org/wiki/Брянск",
"https://ru.wikipedia.org/wiki/Курск",
"https://ru.wikipedia.org/wiki/Тверь",
"https://ru.wikipedia.org/wiki/Магнитогорск",
"https://ru.wikipedia.org/wiki/Иваново",
"https://ru.wikipedia.org/wiki/Белгород",
"https://ru.wikipedia.org/wiki/Сочи",
"https://ru.wikipedia.org/wiki/Севастополь",
"https://ru.wikipedia.org/wiki/Симферополь",
"https://ru.wikipedia.org/wiki/Архангельск",
"https://ru.wikipedia.org/wiki/Мурманск",
"https://ru.wikipedia.org/wiki/Ставрополь",
"https://ru.wikipedia.org/wiki/Якутск",
"https://ru.wikipedia.org/wiki/Кострома",
"https://ru.wikipedia.org/wiki/Орёл",
"https://ru.wikipedia.org/wiki/Вологда",
"https://ru.wikipedia.org/wiki/Смоленск",
"https://ru.wikipedia.org/wiki/Калуга",
"https://ru.wikipedia.org/wiki/Тамбов",
"https://ru.wikipedia.org/wiki/Грозный",
"https://ru.wikipedia.org/wiki/Нальчик",
"https://ru.wikipedia.org/wiki/Майкоп",
"https://ru.wikipedia.org/wiki/Элиста",
"https://ru.wikipedia.org/wiki/Псков",
"https://ru.wikipedia.org/wiki/Великий_Новгород",
"https://ru.wikipedia.org/wiki/Петрозаводск",
"https://ru.wikipedia.org/wiki/Южно-Сахалинск",
"https://ru.wikipedia.org/wiki/Чита",
"https://ru.wikipedia.org/wiki/Улан-Удэ",
"https://ru.wikipedia.org/wiki/Кызыл",
"https://ru.wikipedia.org/wiki/Абакан",
"https://ru.wikipedia.org/wiki/Благовещенск",
"https://ru.wikipedia.org/wiki/Биробиджан",
"https://ru.wikipedia.org/wiki/Магадан",
"https://ru.wikipedia.org/wiki/Анадырь",
"https://ru.wikipedia.org/wiki/Камчатка",
"https://ru.wikipedia.org/wiki/Сибирь",
"https://ru.wikipedia.org/wiki/Урал",
"https://ru.wikipedia.org/wiki/Дальний_Восток",
"https://ru.wikipedia.org/wiki/Волга",
"https://ru.wikipedia.org/wiki/Байкал",
"https://ru.wikipedia.org/wiki/Алтай",
"https://ru.wikipedia.org/wiki/Кавказ",
"https://ru.wikipedia.org/wiki/Арктика",
"https://ru.wikipedia.org/wiki/Антарктида",
"https://ru.wikipedia.org/wiki/Европа",
"https://ru.wikipedia.org/wiki/Азия",
"https://ru.wikipedia.org/wiki/Африка",
"https://ru.wikipedia.org/wiki/Северная_Америка",
"https://ru.wikipedia.org/wiki/Южная_Америка",
"https://ru.wikipedia.org/wiki/Австралия",
"https://ru.wikipedia.org/wiki/Океания",
"https://ru.wikipedia.org/wiki/Интернет",
"https://ru.wikipedia.org/wiki/Компьютер",
"https://ru.wikipedia.org/wiki/Программирование",
"https://ru.wikipedia.org/wiki/Алгоритм",
"https://ru.wikipedia.org/wiki/Искусственный_интеллект",
"https://ru.wikipedia.org/wiki/Машинное_обучение",
"https://ru.wikipedia.org/wiki/Нейронная_сеть",
"https://ru.wikipedia.org/wiki/База_данных",
"https://ru.wikipedia.org/wiki/Операционная_система"
]

# create folder
os.makedirs("pages", exist_ok=True)

index_file = open("index.txt", "w", encoding="utf-8")

for i, url in enumerate(urls, start=1):

    try:
        response = requests.get(url, timeout=10)

        filename = f"pages/{i}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)

        index_file.write(f"{i} {url}\n")

        print(f"Downloaded: {url}")

    except Exception as e:
        print("Error:", url)

index_file.close()

print("Finished downloading pages")