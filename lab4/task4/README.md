# Задание №4 по выбору  : `Скобочная последовательность. Версия 2`
Студентка ИТМО,  Трусова Светлана Викторовна 467766

## Вариант 22

## Задание 
Определение правильной скобочной последовательности такое же, как и в
задаче 3, но теперь у нас больше набор скобок: []{}().
Нужно написать функцию для проверки наличия ошибок при использовании
разных типов скобок в текстовом редакторе типа LaTeX.
Для удобства, текстовый редактор должен не только информировать о наличии
ошибки в использовании скобок, но также указать точное место в коде (тексте) с
ошибочной скобочкой.
В первую очередь объявляется ошибка при наличии первой несовпадающей
закрывающей скобки, перед которой отсутствует открывающая скобка, или которая не соответствует открывающей, например, ()[} - здесь ошибка укажет на
}.
Во вторую очередь, если описанной выше ошибки не было найдено, нужно
указать на первую несовпадающую открывающую скобку, у которой отсутствует
закрывающая, например, ( в ([].
Если не найдено ни одной из указанный выше ошибок, нужно сообщить, что
использование скобок корректно.
Помимо скобок, код может содержать большие и маленькие латинские буквы,
цифры и знаки препинания.
Формально, все скобки в коде (тексте) должны быть разделены на пары совпадающих скобок, так что в каждой паре открывающая скобка идет перед закрывающей скобкой, а для любых двух пар скобок одна из них вложена внутри другой,
как в (foo[bar]) или они разделены, как в f(a,b)-g[c]. Скобка [ соответствует
скобке ], соответствует и ( соответствует ) .


## Input / Output

| Input       | Output |
|-------------|--------|
| foo(bar[i); | 10     |


## Ограничения по времени и памяти

- Ограничение по времени. 2сек.
- Ограничение по памяти. 256 мб.


## Запуск проекта
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/SvetaTrusova/algorithms-and-data-structures
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd algorithms-and-data-structures/lab4
   ```
3. Запустите программу:
   ```bash
   python task4/src/task4.py
   ```


## Тестирование
Для запуска тестов выполните:
```bash
    python -m unittest -v lab4.task4.tests.test_4_4.py
```