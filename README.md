# Тестовое задание по анализу потребления кофе студентами

CLI-приложение для формирования отчётов по затратам на кофе на основе CSV-файлов.

---

## Установка

### Создание виртуального окружения и активация

```bash
python -m venv .venv
````

Активация окружения

```powershell
.\.venv\Scripts\Activate.ps1
```

или

```bash
source .venv/bin/activate
```

### Установка зависимостей

```bash
python -m pip install -U pip
python -m pip install -e ".[dev]"
```

---

## Запуск

```bash
python main.py --files data/math.csv data/physics.csv data/programming.csv --report median-coffee
```

Вывод формируется в консоль в виде таблицы.

---

## Тесты и покрытие

```bash
python -m pytest --cov
```