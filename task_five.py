'''
1.Дана строка, состоящая из слов,
разделенных пробелами. Определите,
сколько в ней слов.
'''

def main():

    string = input("Введите текст: ")
    line = string.split()
    print("Вывод строки: ", line)
    print("Количество слов: ", len(line))

if __name__ == '__main__':
    main()