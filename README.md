# GooHope

Инструкция по запуску проекта:

 - `bash setup.sh`

Необходимые инструменты для запуска проекта:

 - `docker`
 - `docker-compose`
 
 Развёрнутый проект можно просмотреть на `http://localhost`
 
 Postman:
 - [GooHope DOCS](https://www.postman.com/)
 
 Дизайн проекта:
 - [GooHope Figma](https://www.figma.com/file/YLZlFEEca9rP4ziNTJg1V5/GooHope?node-id=0%3A1)
 
 Примечание
 - Если отсутствует bash:
 ````
    docker-compose up -d --build
    cp api/.env.dev api/.env
    ДОПОЛНИТЬ
 ````