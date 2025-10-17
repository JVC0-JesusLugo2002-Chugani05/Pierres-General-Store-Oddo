start:
    docker compose up -d --build

stop:
    docker compose down

reset:
    docker compose down && docker compose up -d --build
