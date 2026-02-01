from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def get_current_url(self):
        return self.driver.current_url

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_to(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        return self

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def send_keys(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def switch_to_second_tab(self):
        current = self.driver.current_window_handle # текущее кол-во хэндлесов (табов)
        self.wait.until(lambda d: len(d.window_handles) == 2) # ждём, пока появится новый
        second = next(h for h in self.driver.window_handles if h != current) # записываем в переменную
        self.driver.switch_to.window(second) # переключаемся на его

        return self

    def title_equal(self, expected_title):
        try:
            return self.wait.until(EC.title_is(expected_title))
        except:
            current_url = self.driver.current_url
            raise AssertionError(f"Переданного заголовка: '{expected_title}' нет на странице: '{current_url}'")