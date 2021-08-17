bootstrap:
		$(VENV_PATH)/python ./crmpro/manage.py migrate;
up:
		docker-compose up
stop-all:
		docker stop $(docker ps -aq)
down:
		docker-compose down

# production commands
p-down:
		docker-compose -f docker-compose.prod.yml down
p-up:
		docker-compose -f docker-compose.prod.yml down


