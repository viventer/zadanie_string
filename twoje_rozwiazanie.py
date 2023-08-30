# ROZWIĄZANIE ---------------------------------------------------------

def format_post(post_info):
    # Tutaj uzupełnij funkcje

    return formatted_post_info


# GOTOWA CZĘŚĆ KODU ---------------------------------------------------------

input_filename = 'posts.txt'
output_filename = 'formatted_posts.txt'

with open(input_filename, 'r') as input_file:
    posts_info = input_file.readlines()

formatted_posts_info = []
for post_line in posts_info:
    formatted_post_info = format_post(post_line)
    formatted_posts_info.append(formatted_post_info + "\n\n")

with open(output_filename, 'w') as output_file:
    output_file.writelines(formatted_posts_info)


# SPRAWDZENIE CZY KOD DZIAŁA PRAWIDŁOWO --------------------------------------

checker_filename = "properly_formatted_posts.txt"

with open(checker_filename, "r") as checker_file:
    properly_formatted_posts_info = checker_file.readlines()

with open(output_filename, "r") as output_file:
    formatted_posts_info = output_file.readlines()

is_correct = "".join(formatted_posts_info) == "".join(
    properly_formatted_posts_info)

if is_correct:
    print("Gratulacje! Twoja funkcja zadziałała prawidłowo.")
else:
    print(f"""Niestety twoja funkcja nie działa prawidłowo.
Sprawdź swój plik wyjściowy - {output_filename} 
i porównaj go z prawidłowym plikiem - {checker_filename}
""")
