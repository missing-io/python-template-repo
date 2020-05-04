.PHONY = local-image prod-image

local-image:
	docker image build -t  {{ cookiecutter.app_name }} .

prod-image:
	docker image build --pull -t  {{ cookiecutter.app_name }}:latest .
