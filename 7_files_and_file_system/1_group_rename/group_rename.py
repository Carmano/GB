import os

# Напишите функцию группового переименования файлов. Она должна:
# 1. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# 2. принимать параметр количество цифр в порядковом номере.
# 3. принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


def group_rename(result_filename, count_numbers_in_rename, s_file_extension, r_file_extension, start_range=None, end_range=None):
    """
    :param result_filename:
    :param count_numbers_in_rename:
    :param s_file_extension:
    :param r_file_extension:
    :param start_range:
    :param end_range:
    Переименовывает группу файлов с расширением s_file_extension в текущей директории на переданный шаблон result_filename + index с расширением r_file_extension,
    если не заданны star_range и end_range. Если они заданы то к результат будет исходного_файла[start_range, end_range] + result_filename + index

    Файлы уже должны быть созданны
    """
    directory_files = next(os.walk('.'), (None, None, []))[2]
    index = 1
    for file in directory_files:
        if file.endswith('.' + s_file_extension):
            if len(str(index)) > count_numbers_in_rename:
                break
            if start_range is None and end_range is None:
                os.rename(file, result_filename + str(index) + "." + r_file_extension)
            else:
                str_range = file[start_range - 1: end_range - 1]
                os.rename(file, str_range + result_filename + str(index) + "." + r_file_extension)
            index += 1


def main():
    group_rename('test', 1, 'txt', 'txt', 1, 3)


if __name__ == '__main__':
    main()
