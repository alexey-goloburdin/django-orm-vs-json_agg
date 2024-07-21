Demonstration of using PostgreSQL function `json_agg` to optimize the number of queries for fetching related data from the database, as well as comparing the number of queries with simple ORM use and using ORM with `prefetch_related`.

```bash
# run migrations
./manage.py migrate

# init database with data
./manage.py init_db_records

# version with naive ORM
./manage.py print_books_naive_method
# 9 queries

# version with ORM + prefetch_related
./manage.py print_books_with_prefetch
# 3 queries

# version with json_agg
./manage.py print_books_with_json
# 1 query
```

And with `json_agg` we get all the data of all the relation entities we need and can initialize Python classes with them in the same way as ORM. In this case book class, category class, author class. No problem. Just instead of a ton of queries, we get all the data with a single query.
