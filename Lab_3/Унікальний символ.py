def get_char_dict(text):
    char_dict = dict()

    for ch in text:
        if ch in char_dict:
            char_dict[ch] = char_dict[ch] + 1
        else:
            char_dict[ch] = 1
    return char_dict


print("Введіть текст")
dict = get_char_dict(input())
print("Кількість унікальних символів: %d" % len(dict))
print("Статистика:")
for ch in dict:
    print(ch.ljust(10), dict[ch])