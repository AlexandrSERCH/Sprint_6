# Sprint_6

## Установка зависимостей
Зависимости устанавливаются из файла `requirements.txt`.

```
python -m pip install -r requirements.txt
```

## Запуск тестов с указанием окружения `ENV`
Переменная окружения `ENV` выбирает стенд в `core/config.py`. Доступные значения: `prod` (по умолчанию), `dev`.

### Параллельный запуск (4 потока)
По умолчанию тесты запускаются в 4 потока за счёт `pytest-xdist` — это настроено в `pytest.ini` (параметр `addopts = -n 4`). При необходимости измените число потоков в `pytest.ini`.

### Bash (Linux/macOS/Git Bash)
```bash
# разово для команды
ENV=dev pytest

# запуск тестов с Allure-результатами
ENV=dev pytest tests --alluredir=allure_results

# просмотр отчёта
allure serve allure_results
```

### Windows
**PowerShell**
```powershell
$env:ENV = "dev"
pytest

# запуск тестов с Allure-результатами
pytest tests --alluredir=allure_results

# просмотр отчёта
allure serve allure_results
```

**CMD**
```cmd
set ENV=dev
pytest tests --alluredir=allure_results
allure serve allure_results
```
