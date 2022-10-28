"""
Zadanie: palindromy
Pamiętaj, że wszystkie zadania, które wysyłasz Mentorowi powinny być umieszczone w Twoim zdalnym repozytorium,
jako osobne projekty. W czasie pracy zapisuj więc kolejne commity i prześlij całość na serwer w serwisie GitHub.

Twoim zadaniem będzie napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem. Palindrom to słowo,
które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.

Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False,
mówiącą czy podany tekst jest palindromem.

Podpowiedź
Pamiętaj, że string/tekst, to kolekcja znaków. Znasz już funkcje kolekcji,
które pozwalają odnosić się do elementów indeksowanych od początku i od końca.

Do zadania dodaj krótką dokumentację i umieść je w zdalnym repozytorium. Link prześlij Mentorowi.
"""

def is_palindrome(word):
    """
    Function which checks if word is palindrome. Takes one argument(string).

    :param word: takes string argument which will be checked if is palindrome.
    :return: True / False
    """
    length = len(word) + 1
    is_word_palindrome = ''
    for i in range(-1, -length, -1):
        is_word_palindrome += word[i]
    if word == is_word_palindrome:
        return True
    else:
        return False

print(is_palindrome('kajak'))
print(is_palindrome('potop'))
print(is_palindrome('epopeja'))