start:
	docker-compose -f docker-compose.dev.yml up --build -d

stop:
	docker stop $$(docker ps -qa) || true

run: stop
	docker-compose -f docker-compose.dev.yml run -d  web python3 manage.py runserver 0.0.0.0:80 || true

cleandir:
	docker rm $$(docker ps -qa)
	docker rmi $$(docker images -qa)
