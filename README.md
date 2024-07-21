Demonstration of using PostgreSQL function `json_agg` to optimize the number of queries for fetching related data from the database, as well as comparing the number of queries with simple ORM use and using ORM with `prefetch_related`.

```bash
# run migrations
./manage.py migrate

# init database with data
./manage.py init_db_records

# version with naive ORM
./manage.py print_books_naive_method

# version with ORM + prefetch_related
./manage.py print_books_with_prefetch

# version with json_agg
./manage.py print_books_with_json
```
