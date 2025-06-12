build:
	docker build -t fraud-workbench .

test:
	pytest -q

run:
	python manage.py runserver 0.0.0.0:8000
