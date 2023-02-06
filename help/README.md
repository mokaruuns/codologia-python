# Шпаргалка по PostgreSQL

## Содержание

* [Основы](#Основы)

## Основы

### Подключение к базе данных

```bash
$ psql -h localhost -U postgres -d postgres
```

### Создание базы данных

```sql
CREATE DATABASE test;
```

### Создание таблицы

```sql
CREATE TABLE users (

id SERIAL PRIMARY KEY,

name VARCHAR(255) NOT NULL,

email VARCHAR(255) NOT NULL,

created_at TIMESTAMP NOT NULL

);

```


### Вставка данных

```sql
INSERT INTO users (name, email, created_at) VALUES ('John', '', NOW());
```

### Выборка данных

```sql
SELECT * FROM users;
```

### Обновление данных

```sql
UPDATE users SET name = 'John Doe' WHERE id = 1;
```

### Удаление данных

```sql
DELETE FROM users WHERE id = 1;
```

### Удаление таблицы

```sql
DROP TABLE users;
```

### Удаление базы данных

```sql
DROP DATABASE test;
```

### Inner join

```sql
SELECT * FROM users INNER JOIN posts ON users.id = posts.user_id;
```

### Where

```sql
SELECT * FROM users WHERE name = 'John';
```

### Order by

```sql
SELECT * FROM users ORDER BY name DESC;
```

### Limit

```sql
SELECT * FROM users LIMIT 10;
```

### Having

```sql
SELECT name, COUNT(*) AS count FROM users GROUP BY name HAVING count > 1;
```


