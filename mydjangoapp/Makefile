up:
	docker compose -f compose/development.yml up -d

down:
	docker compose down

bash:
	docker compose exec web bash

logs:
	docker compose logs -f

test:
	pytest -q

lint:
	ruff check .

format:
	black .
