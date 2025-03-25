dev:
		python app/manage.py runserver
lint:
		uv run ruff check
lint-fix:
		uv run ruff check --fix