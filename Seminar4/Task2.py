# Пользователь вводит текст(строка).
# Словом считается последовательность не пробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.

in_string = "dfsf jjk jk k SDFF sd sdffdfs sdf SDF"

print(in_string.punctuation)

for char in in_string.punctuation:
    in_string = in_string.replace(char, ' ')

in_string = in_string.lower().split()

print("Количество слов:", len(in_string))
