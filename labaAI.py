import numpy as np
# задание массива размером 16 с элементами от 0 до 15 - функция arange
a = np.arange(0, 16)
# поле shape определяет форму массива
print('Shape =', a.shape)
print(a)
a = np.array([0, 1, 2, 3, 4])
print('Shape =', a.shape)
print(a)
# создание матрицы из списка списков
a = np.array(
 [[0, 1],
 [2, 3]]
)
print('Shape =', a.shape)
print(a)
# создание массива из нулевых элементов
a = np.zeros(shape=(3, 2), dtype=np.float32)# необходимо задать форму массива
print(a)
# создание массива единиц
a = np.ones(shape=(3, 2), dtype=np.float32)
print(a)
# Заполнение массива элементами
a.fill(10) # заполняемый элемент
print(a)
# создание массивов случайных чисел, модуль numpy.random
# равномерное распределение целых чисел
# фиксация генератора случайных чисел
np.random.seed(0)
# равномерное распределение целых чисел
a = np.random.randint(low=0, high=10, size=(4, 4, 3))
print(a)
# равномерное распределение вещественных чисел
a = np.random.uniform(low=0, high=1, size=(4, 4, 3))
print(a)
# нормальное распределние вещественных чисел
a = np.random.normal(size=(4, 4, 3))
print(a)
# Нумерация начинается с нуля (dim0, dim1, ..., dimN)
a = np.arange(1, 13)
# превращение массива в тензор, который имеет размер (2 строки, 2 столбца, 3
a = a.reshape((2, 2, 3))
print(a)
print()
# Доступ к отдельному элементу по его индексу
print(a[0, 0, 0])
# Эти записи эквивалентны
print(a[0][0][0])
# доступ к i-й строке тензора
print(a[0])
# доступ к j-му столбцу тензора
print(a[:, 0])
# доступ к k-му каналу тензора
print(a[:, :, 0])
# создаем матрицу 4x3
a = np.arange(1, 13).reshape((4, 3))
print(a)
print()
# получение строк в нужном нам порядке сначала 2, потом 0, затем 1
print(a[[2, 0, 1]])
# получение столбцов в нужном нам порядке сначала 2, потом 0, затем 1
print(a[:, [2, 0, 1]])
a = np.arange(1, 13).reshape((4, 3))
print(a)
print('Mean =', a.mean())
bool_indices = a > a.mean()
print('Bool indices:', bool_indices, sep='\n')
print()
# фильтрация значений по индексу
print(a[bool_indices])
# Создаем тензор из 2 строк, 2 столбцов, 3 каналов
a = np.arange(1, 13).reshape((2, 2, 3))
print(a)
# выделяем с нулевой по первую строку, выделение всех столбцов, выделение отд

print(a[:1, :, 0])
# создаем матрицу 4x3 из последовательных элементов
a = np.arange(1, 13).reshape((4, 3))
print(a)
# выделяем строки матрицы от нулевой до второй, не включая
# выделяем стролбцы матрицы от первой до последней, включая
print(a[:2, 1:])
# создание вектора из 16 элементов со значениями от 0 до 15
a = np.arange(0, 16)
# превращение вектора в матрицу при помощи метода reshape
# в скобках указан целевой размер матрицы (строки, столцы)
a = a.reshape((4, 4))
print('Matrix shape:', a.shape)
print('Matrix:', a, sep='\n')
print()
# транспонирование матрицы
a = a.transpose()
print('Transposed matrix shape:', a.shape)
print('Matrix:', a, sep='\n')
print()
# с помощью reshape с аргументом -1 можно из матрицы снова сделать вектор
a = a.reshape(-1)
print('Flattened transposed matrix:', a, sep='\n')
print()
x = np.array([[1,2],
 [3,4]], dtype=np.float64)
y = np.array([[5,6],
 [7,8]], dtype=np.float64)
print(x+y)
print()
# np.add эквивалентна оператору +
print(np.add(x, y))
print(x - y)
print()
# np.subtract эквивалентна оператору -
print(np.subtract(x, y))
print(x * y)
print()
# np.multiply эквивалентна оператору *
print(np.multiply(x, y))
print(x / y)
print()
# np.divide эквивалентна оператору /
print(np.divide(x, y))
# синус
print(np.sin(x))
# косинус
print(np.cos(x))
# квадратный корень
print(np.sqrt(x))
# экспонента
print(np.exp(x))
# натуральный логарифм
print(np.log(x))
x = np.arange(1, 17)
# сумма
print(np.sum(x))
# произведение
print(np.prod(x))
# среднее значение
print(np.mean(x))
# скалярное произведение
a = np.arange(4)
b = np.arange(4)
print('Vector a: ', a)
print('Vector b: ', b)
print()
print('Result:', np.dot(a, b), sep='\n')
# матрично-векторное произведение
A = np.arange(0, 16)
A = A.reshape((4, 4))
b = np.arange(4)
print('Matrix A: ', A, sep='\n')
print('Vector b: ', b, sep='\n')
print()
print('Result:', np.dot(A, b), sep='\n')
# матричное произведение
A = np.arange(0, 16)
A = A.reshape((4, 4))
B = np.arange(0, 12)
B = B.reshape((4, 3))
print('Matrix A: ', A, sep='\n')
print('Matrix B: ', B, sep='\n')
print()
print('Result:', np.dot(A, B), sep='\n')