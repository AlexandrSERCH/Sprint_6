# Sprint_6

## Запуск тестов с указанием окружения `ENV`
Переменная окружения `ENV` выбирает стенд в `core/config.py`. Доступные значения: `prod` (по умолчанию), `dev`.

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
