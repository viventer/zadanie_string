def format_user_info(user_data):
    # Wypełnij funkcję
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
