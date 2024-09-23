Внесенные изменения:
В функции parse_neti_company_page(url) удалено получение регистрационного кода, KMKR, адреса и email. Теперь функция возвращает только URL сайта компании.
В методе fill_company_data() теперь заполняется только поле website для каждого объекта Company.
Метод _parse_neti_companies_list() также был изменен — он собирает только имя компании и URL её сайта.
Объяснение:
Основной процесс парсинга остался неизменным. Парсер использует Selenium для автоматизации работы с браузером, заходя на страницы компаний и извлекая URL сайта.
Многопоточность через ThreadPool(4) помогает ускорить процесс, особенно при парсинге большого количества компаний.