import os


def get_text_from_file(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    return text


def get_words(text):
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def get_char_dict(text):
    text=''.join(sorted(text))
    char_dict = dict()

    for ch in text:
        if ch in char_dict:
            char_dict[ch] = char_dict[ch] + 1
        else:
            char_dict[ch] = 1
    return char_dict


filename = input("Введіть повне ім'я файлу: ")
if not os.path.exists(filename):
    print("Вказаного файлу не існує")
else:
    text = get_text_from_file(filename)
    words = get_words(text)
    words_dict = get_words_dict(words)
    print("Кількість слів: %d" % len(words))
    print("Кількість унікальних слів: %d" % len(words_dict))
    print("Всі слова:")
    for word in words_dict:
        print(word.ljust(20), words_dict[word])
    dict = get_char_dict(text)
    print("\nКількість символів: %d" % len(text))
    print("Кількість унікальних символів: %d" % len(dict))
    print("Статистика:")
    for ch in dict:
        print(ch.ljust(10), dict[ch])
