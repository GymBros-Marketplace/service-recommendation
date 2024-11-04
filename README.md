Сервис для рекомендации товаров пользователям

Запустить
```
docker-compose up --build
```

Тестирование
```
curl -X 'POST' \
    'http://localhost:8001/recommendations/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{"user_id": 123, "item_ids": [1, 2, 3, 4, 5]}'
```