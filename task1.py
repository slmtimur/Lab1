num = int(input("Введите число: "))
word = input("Введите любое слово: ")
string = input("Введите любую строку: ")
arr = list(input("Через пробел введите данные для списка: ").split())
cort = tuple(input("Через пробел введите данные для кортежа: ").split())

num -= 1
word += " with a new text"
string = string.split()
arr.reverse()
n = len(cort)

print("\n")
print("Число минус единица: ", num)
print("Слово с новым текстом: ", word)
print("Разделённая строка: ", string)
print("Перевёрнутый список: ", arr)
print("Размер кортежа: ", n)
