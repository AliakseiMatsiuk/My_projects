import re

def cipher(text) -> str:
    """
    На вход программе подается строка текста на английском языке,
    в которой нужно зашифровать все слова.
    Каждое слово строки следует зашифровать с помощью шифра Цезаря
    (циклического сдвига на длину этого слова).
    Строчные буквы при этом остаются строчными, а прописные – прописными.
    :param text: Предложение на аглийском
    :return: Зашифрованый текст
    """
    lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text_split = text.split(" ")
    text_best_split = [len(i) for i in re.findall(r'\b\w+\b',text)]
    lis = []
    for i,v in enumerate(text_split):
        nam = text_best_split[i]
        for j, w in enumerate(v):
            if w in upper:
                for y, x in enumerate(upper):
                    if x == w:
                        lis.append(upper[y+nam])
                        break
            elif w in lower:
                for y, x in enumerate(lower):
                    if x == w:
                        lis.append(lower[y+nam])
                        break
            else:
                lis.append(w)
        lis.append(' ')
    return ''.join(lis)[:-1]


text = input()
print(cipher(text))