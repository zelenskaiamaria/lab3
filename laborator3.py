# 8
# x=-4
# while x<=4:
#     y = 2*x*x - 5*x - 8
#     print(f'dla x = {x} wartosc funkcji wynosi {y}')
#     x+=0.5

# 9
# while True:
#     licz = int(input('podaj liczbe calkowitę: '))
#     if licz < 0:
#         print("wychodze z petli")
#         break


# 10
# x = int(input("Podaj pierwszą liczbę całkowitą: "))
# y = int(input("Podaj drugą liczbę całkowitą: "))
# while x<y:
#     pprint(x)
#     x+=1
# while y<=x:
#     pprint(y)
#     y+=1



# 11
# n = int(input("Podaj liczbę wierszy: "))


# for i in range(1, n + 1):
#     # Sprawdzenie, czy liczba jest parzysta
#     if i % 2 != 0:
#         continue  # Jeśli liczba nie jest parzysta, pomijamy tę iterację

#     print('*' * i)
# 12
# n = int(input("Podaj liczbę studentów w grupie: "))
# suma_punktow = 0
# licznik = 0
#
# while licznik < n:
#     punkty = float(input(f"Podaj liczbę punktów dla studenta {licznik + 1}: "))
#     suma_punktow += punkty
#     licznik += 1
#
# srednia = suma_punktow / n
#
# print(f"Średnia liczba punktów w grupie wynosi: {srednia}")
# 13
# while True:

#     punkty = int(input("Podaj liczbę punktów (0-100): "))


#     if punkty < 0 or punkty > 100:
#         print("Liczba punktów spoza przedziału 0-100. Pomijam dalsze działanie pętli.")
#         continue

#     n = punkty
#     for i in range(1, n + 1):
#         print('*' * i)

#     break
# 14
# import math
# while True:

#     dana = int(input("Podaj liczbę: "))

#     if dana >= 0:
#         print("To jest liczba dodatnia.")
#         pierwiastek = math.sqrt(dana)
#         print(f"Pierwiastek kwadratowy z {dana} to {pierwiastek}")
#         continue
#     else:
#         print("Dziękujemy za skorzystanie z naszej aplikacji.")
#         break


# 1
# imiona = ['Anna', 'Marek', 'Zofia', 'Piotr']
# imiona.sort()
# print(imiona)
# imiona.append('Kasia')
# imiona.append('Tomasz')
# ostatnia_osoba = imiona.pop()
# print(imiona)
# print(f'Ostatnia dodana osoba: {ostatnia_osoba}')
# imiona.insert(2, 'Jacek')
# print(imiona)
# imiona.reverse()
# imiona = imiona * 2
# print(imiona)


# 2
#
# a)
# import string
# sentence = input("Введите предложение: ")
# sentence = sentence.lower()
# letters_in_sentence = set([char for char in sentence if char in string.ascii_lowercase])
# alphabet = set(string.ascii_lowercase)
# missing_letters = alphabet - letters_in_sentence
# print("Буквы, встречающиеся в предложении (по алфавиту):")
# print("".join(sorted(letters_in_sentence)))
# print("Буквы, которых нет в предложении:")
# print("".join(sorted(missing_letters)))

# b)
# sentence = input("Введите строку: ")
# modified_sentence = sentence[::2]
# print("Строка после удаления символов с нечётными индексами:")
# print(modified_sentence)
#
# с)
# sentence = input("Введите предложение: ")
# words = sentence.split()
# longest_word = max(words, key=len)
# print(f"Самое длинное слово: {longest_word}")
# print(f"Длина слова: {len(longest_word)}")

#d)
# sentence = input("Введите строку: ")
# char_count = {}
# for char in sentence:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
#
# modified_sentence = ''.join('@' if char_count[char] > 1 else char for char in sentence)
# print("Изменённая строка:")
# print(modified_sentence)

#3
#sentence = input("Введите строку: ")
#cleaned_sentence = sentence.replace(" ", "").lower()

#if cleaned_sentence == cleaned_sentence[::-1]:
 #   print("Строка является палиндромом.")
#else:
 #   print("Строка не является палиндромом.")

#5
# Tworzymy słownik z artykułami i ich cenami
# shopping_list = {
#     "mleko": 3.4,
#     "chleb": 4.5,
#     "chałka": 3.5,
#     "mydło": 4.0,
#     "ser": 3.4
# }
# print("Lista zakupów:")
# for item, price in shopping_list.items():
#     print(f"{item}: {price} PLN")
# total_cost = sum(shopping_list.values())
# print(f"\nCałkowite wydatki: {total_cost} PLN")
# 6
# electricity_bills = {
#     "styczeń": 150.50,
#     "luty": 135.75,
#     "marzec": 105.30,
#     "kwiecień": 60.60,
#     "maj": 59.90
# }
# max_bill = max(electricity_bills.values())
# min_bill = min(electricity_bills.values())
# total_bill = sum(electricity_bills.values())
# average_bill = total_bill / len(electricity_bills)
#
# print(f"najwyższy rachunek: {max_bill} PLN")
# print(f"najniższy rachunek: {min_bill} PLN")
# print(f"suma rachunków: {total_bill} PLN")
# print(f"sredni rachunek: {average_bill:.2f} PLN")

# 7
# a)
#
import random
def create_random_set(min_size=3, max_size=7, value_range=(0, 10)):

    set_size = random.randint(min_size, max_size)
    random_set = set(random.randint(value_range[0], value_range[1]) for _ in range(set_size))
    return random_set

a = create_random_set()
b = create_random_set()

# a=[2,4,5,7,8]
# b=[1,2,3,4,5,6,7,8,9]
# s = a.count(5)
# if s > 0:
#     print('yes')
# b)
# if set(a).issubset(set(b)):
#    print('True')
# c)
# if set(b).issubset(set(a)):
#      print('True')
# else:
#     print('False')
# d)
# print(sum(a)+sum(b))
# e)
# dif = a.difference(b)
# print(dif)
# f)
# diff = b.difference(a)
# print(diff)
# g)
# res = a.union(b)
# print(res)
# h)
# res = max(a)
# print(res)
# rew = max(b)
# print(rew)
# i)
# res = a[0]
# a.pop(0)
# b.insert(0, res)
# print(a)
# print(b)
# j)
# X = create_random_set()
# Y = create_random_set()
#
# # Wyświetlamy zbiory przed kopiowaniem
# print("Zbiór X przed kopiowaniem:", X)
# print("Zbiór Y przed kopiowaniem:", Y)
#
# # Przekopiowanie wszystkich elementów ze zbioru X do zbioru Y
# Y.update(X)
#
# # Wyświetlamy zbiory po kopiowaniu
# print("\nZbiór X po kopiowaniu:", X)
# print("Zbiór Y po kopiowaniu:", Y)
# k)
# a.clear()
# b.clear()
# print(a)
# print(b)

# 4)
# krotka = ('asdfgh', 'drftgyuhijm','gvyhbuhij''xrtyguh')
# suma = 0
# liczbak = 0
# for slowo in krotka:
#     # A
#     suma += len(slowo)
#     print(suma)
#     # B
#     for znak in slowo:
#         if znak =='k':
#             liczbak += 1
#             print(liczbak)
#     # C
#     if slowo.find('kt')>=0:
#         liczbak += 1
#         if len (slowo)<= suma: liczbak += 1
#         print(liczbak)
#         print(suma)




