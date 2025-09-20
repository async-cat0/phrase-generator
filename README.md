# Phrase Generator


Простой и удобный генератор случайных фраз на Python. Идеально подходит для творческих задач, поиска вдохновения или просто для развлечения.

---

## ✨ Возможности

*   **Генерация случайных фраз**: Комбинирует слова из разных наборов для создания уникальных сочетаний.
*   **Простота использования**: Запуск одной командой.
*   **Легкая настройка**: Простое добавление своих слов в файлы констант.

## 🚀 Установка и запуск

1.  **Клонируй репозиторий**:
    ```bash
    git clone https://github.com/async-cat0/phrase-generator.git
    cd phrase-generator
    ```

2.  **Убедись, что у тестан установлен Python 3.8+**.
    Проверь версию:
    ```bash
    python --version
    # или
    python3 --version
    ```

3.  **Запусти скрипт**:
    ```bash
    python main.py
    # или
    python3 main.py
    ```

## 🛠️ Как это работает

Код использует модуль `random` для выбора случайного слова из трех списков (`DCT`, `DCT2`, `DCT3`), расположенных в файле `constants.py`также можно менять содержимое списков. Выбранные слова объединяются в одну фразу и выводятся в терминал с цветным оформлением.Файл constants.py можно найти в `project/constant/conastants.py`


**Пример кода:**
```python
import random
from constant.constants import RESET,YELLOW
from constant.constants import DCT,DCT2,DCT3



def generate():
    space = ' '
    print(f"{random.choice(DCT) + space + random.choice(DCT2) + space + random.choice(DCT3)}")
    print(f"{YELLOW} by async-cat0{RESET}")
generate()
