# selector-bot
Данный телеграмм бот выбирает одного человека из участников игры и оповещает чат кто стал победителем дня.
Ссылка на бота: https://t.me/selector_bot

Имеется следующие игры:

- Красавчик дня!

# Запуск бота
## 1 способ - используя исходный код

Для запуска бота выполните:

1. запишите токен в следующий файл `/token/token.json`

```json
{
  "TOKEN": "0123456789:ABCDEFGHIABCDEFGHIJKLMNOPQRSTUVWXYZ"
}
```

2. Запустите в оболочке shell

```shell
$ python src/bot/models/create_tables.py && python src/bot/app.py
```

## 2 способ - используя docker-compose

1. создайте `docker-compose.yaml` со следующим содержимым, вставьте свой запишите токен в поле `TOKEN`

```docker
version: "3.3"

services:
  selected-tgbot:
    image: quteas/selected-tgbot:latest
    container_name: selected-tgbot
    command: bash -c "python /app/src/bot/models/create_tables.py && python /app/src/bot/app.py"
    environment:
      TOKEN: "0123456789:ABCDEFGHIABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ports:
      - 80:80
      - 443:443
      - 88:88
      - 8443:8443
    volumes:
      - './database:/app/database'
```

2. Запустите в оболочке shell docker контейнер

```shell
$ docekr-compose up -d
```
