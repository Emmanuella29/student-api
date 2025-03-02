run:
	python wsgi.py

migrate:
	flask db migrate -m "Migration message"

upgrade:
	flask db upgrade
 
