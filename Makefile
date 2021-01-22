SHELL:=/bin/bash
ARGS = $(filter-out $@,$(MAKECMDGOALS))
MAKEFLAGS += --silent
BASE_PATH=${PWD}
PYTHON_EXEC=python
DOCKER_COMPOSE_FILE=$(shell echo -f docker-compose.yml)

export $(shell sed 's/=.*//' src/.env)

show_env:
	# Show wich DOCKER_COMPOSE_FILE and ENV the recipes will user
	# It should be referenced by all other recipes you want it to show.
	# It's only printed once even when more than a recipe executed uses it
	sh -c "if [ \"${ENV_PRINTED:-0}\" != \"1\" ]; \
	then \
		echo DOCKER_COMPOSE_FILE = \"${DOCKER_COMPOSE_FILE}\"; \
		echo OSFLAG = \"${OSFLAG}\"; \
	fi; \
	ENV_PRINTED=1;"

init: show_env _cp_env_file

_rebuild: show_env
	docker-compose ${DOCKER_COMPOSE_FILE} down
	docker-compose ${DOCKER_COMPOSE_FILE} build --no-cache --force-rm

up: show_env
	docker-compose ${DOCKER_COMPOSE_FILE} up -d --remove-orphans --build

log: show_env
	docker-compose ${DOCKER_COMPOSE_FILE} logs -f --tail 200 app

logs: show_env
	docker-compose ${DOCKER_COMPOSE_FILE} logs -f --tail 200

stop: show_env
	docker-compose ${DOCKER_COMPOSE_FILE} stop

status: show_env
	docker-compose ${DOCKER_COMPOSE_FILE} ps

restart: show_env
	docker-compose ${DOCKER_COMPOSE_FILE} restart

sh: show_env
	docker-compose ${DOCKER_COMPOSE_FILE} exec ${ARGS} bash
