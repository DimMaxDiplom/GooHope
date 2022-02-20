#!/bin/bash

docker-compose up -d --build

cp api/.env.dev api/.env

echo 'Project is ready for testing!'