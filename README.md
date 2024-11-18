Сервис для рекомендации товаров пользователям

Запустить
```
docker-compose up --build
```

Тестирование
```
curl -X 'POST' \
    'http://localhost:8001/api/recommend/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{"user_id": 123}'
```

```
curl -X 'GET' \
    'http://localhost:8001/api/healthcheck/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
```