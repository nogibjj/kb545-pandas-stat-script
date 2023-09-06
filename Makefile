install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=src test/test_*.py

format:
	#Uncomment once a python file is present, and ready to be formatted correctly. No python files now is causing an error	
	black src/*.py 

lint: 
	#Whenever a lint check needs to occur, either have a mylib folder, or change mylib to the respective folder name
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy
