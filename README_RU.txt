Лабораторная работа 28 — организованный набор Selenium/pytest.

Сайт: https://www.saucedemo.com/
Учебные публичные данные Sauce Demo:
  пользователь: standard_user
  пароль: secret_sauce

Первый запуск в Windows (из папки проекта):
  py -m venv .venv
  .venv\Scripts\activate
  py -m pip install -r requirements.txt
  py generate_data.py

Проверки:
  py -m pytest --collect-only
  py -m pytest -m smoke -v
  py -m pytest -v
  py -m pytest -x -v
  py -m pytest --lf -v

Ожидается 17 результатов: 8 тестовых функций, одна из них параметризована
10 строками CSV. В smoke-наборе 3 теста.
