# Główna funkcja formatująca informacje o poście
def format_post(post_info):
    # Dzielę stringa w miejscach spacji
    parts = post_info.split()
    # Jego pierwsza część to nazwa użytkownika
    username = parts[0]
    # Tytuł to wszystkie części od pierwszej do przedostatniej
    title = ' '.join(parts[1:-1])
    # A data stworzenia to ostatnia cześć
    creation_date = format_date(parts[-1])

    formatted_post_info = f"""autor: {username}
tytuł: {title}
data utworzenia: {creation_date}"""

    return formatted_post_info


# Funkcja pomocnicza formatująca datę
def format_date(date_str):
    """
    Do oddzielenia liczb skorzystałem z funkcji split, a oprócz tego używałem odpakowania 
    listy, dzięki czemu wszystkie zmienne (day, month, year) tworzę jednocześnie z kolejnych 
    elementów listy.
    Można to też zrobić w klasyczny sposób:
    date_list = date_str.split(".")
    day = date_list[0]
    month = date_list[1]
    year = date_list[2]
    """
    day, month, year = date_str.split('.')
    # Stworzyłem słownik dzięki któremu zamienię miesiące podane liczbowo na ich nazwy
    months = {
        '01': 'stycznia', '02': 'lutego', '03': 'marca', '04': 'kwietnia',
        '05': 'maja', '06': 'czerwca', '07': 'lipca', '08': 'sierpnia',
        '09': 'września', '10': 'października', '11': 'listopada', '12': 'grudnia'
    }
    # Jeśli dzień rozpoczyna się od 0 - usuwam je
    day = day.removeprefix("0")
    formatted_date = f"{day} {months[month]} 20{year} r."
    return formatted_date


# GOTOWA CZĘŚĆ KODU ---------------------------------------------------------
input_filename = 'posts.txt'
output_filename = 'properly_formatted_posts.txt'

with open(input_filename, 'r') as input_file:
    posts_info = input_file.readlines()

formatted_posts_info = []
for post_line in posts_info:
    formatted_post_info = format_post(post_line)
    formatted_posts_info.append(formatted_post_info + "\n\n")

with open(output_filename, 'w') as output_file:
    output_file.writelines(formatted_posts_info)
