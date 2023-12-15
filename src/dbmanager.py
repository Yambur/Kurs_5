import psycopg2

class DBManager():


    def get_companies_and_vacancies_count(self):
        """Список компаний и количество вакансий у каждой компании."""
        query = "SELECT employer, COUNT(*) AS vacancies_count FROM vacancies GROUP BY employer"
        with self.conn, self.conn.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return results

    def get_all_vacancies(self):
        """Возвращает все вакансии из базы данных."""
        query = "SELECT * FROM vacancies"
        with self.conn, self.conn.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return results

    def get_avg_salary(self):
        """Возвращает среднюю зарплату всех вакансий, где зарплата указана."""
        query = "SELECT AVG(salary) AS avg_salary FROM vacancies WHERE salary IS NOT NULL"
        with self.conn, self.conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
        return round(result[0]) if result[0] else None
    def get_vacancies_with_higher_salary(self):
        """Возвращает все вакансии, у которых зарплата выше средней зарплаты."""
        avg_salary = 62091
        query = "SELECT * FROM vacancies WHERE salary > %s"
        with self.conn, self.conn.cursor() as cursor:
            cursor.execute(query, (avg_salary,))
            results = cursor.fetchall()
        return results

    def get_vacancies_with_keyword(self, keyword, cur):
        cur.execute(f'''SELECT * FROM vacancies WHERE vacancy_name LIKE "%{keyword}%"''')
        result = cur.fetchall()
        return result
