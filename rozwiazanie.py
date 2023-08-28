def format_user_info(user_data):
    # Zamieniamy stringa na listę, elementy rozdzielone są spacjami
    user_data = user_data.split(" ")
    # Z utworzonej listy pobieramy dane rozpakowując listę
    first_name, last_name, age, email = user_data
    """
    Rozpakowując listę wszystkie zmienne tworzymy naraz przypisując do nich 
    kolejne elementy, ale oczywiście możemy to też zrobić klasyczną metodą:
    first_name = user_data[0]
    last_name = user_data[1]
    age = user_data[2]
    email = user_data[3]
    """

    # Teraz najważniejsze - tworzymy sformatowane dane za pomocą f-stringa:
    formatted_info = f"""imie: {first_name}
nazwisko: {last_name}
wiek: {age}
pełnoletni: {"tak" if int(age) >= 18 else "nie"}
email: {email}"""

    return formatted_info


# Gotowa część ---------------------------
file_name = "users.txt"

try:
    with open(file_name, "r") as file:
        for line in file:
            print(f"{'-' * 30}")
            formatted_info = format_user_info(line)
            print(formatted_info, end="")
        print(f"\n{'-' * 30}")
except FileNotFoundError:
    print(f'Nie znaleziono pliku: {file_name}.')
except:
    print(f"Błąd odczytu pliku: {file_name}.")
