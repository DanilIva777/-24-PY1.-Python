# TODO Найдите количество книг, которое можно разместить на дискете

# Задаём константы
Mb_in_floppy = 1.44
num_pages_in_book = 100
line_in_page = 50
letter_in_line = 25
letter_in_byte = 4

# Рассчитываем сколько пометится книг на дискету

# Сначала переведём мегабайт в байты
byte_in_floppy = Mb_in_floppy * 1024 * 1024

# Рассчитаем сколько байт занимает одна книга
byte_in_book = num_pages_in_book * line_in_page * letter_in_line * letter_in_byte

# И получим искомое значение в целых числах
books_in_floppy = byte_in_floppy // byte_in_book

# При выводе округляем кол-во книг, которое поместится на дискете
print(f"Количество книг, помещающихся на дискету: {books_in_floppy:.0f}")
