bootstrap:
		$(VENV_PATH)/python ./crmpro/manage.py migrate;
up:
		docker-compose up
stop-all:
		docker stop $(docker ps -aq)
down:
		docker-compose down




