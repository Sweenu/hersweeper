init:
	pip install pipenv
	pipenv install --dev

update:
	pipenv --update
	pipenv update

test:
	pipenv run pytest tests

flake8:
	pipenv run flake8
