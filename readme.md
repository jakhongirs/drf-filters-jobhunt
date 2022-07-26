`api/v1/swagger/schema/` - swagger

`vacancies/ `- all vacancies

`vacancy/<int:pk> `- Detail Vacancy

`api/v1/vacancies/?status=URGENT` - Filter by status

`api/v1/vacancies/?region=1` - Filter region by ID

`api/v1/vacancies/?region__slug=toshkent` - Filter region by slug name

`/api/v1/vacancies/?category=4` - Filter by Category