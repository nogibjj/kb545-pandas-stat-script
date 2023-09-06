install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test: install
	python -m pytest -vv --cov=src.stat1 test/*.py

format:	
	black src/*.py 

lint: 
	#Whenever a lint check needs to occur, either have a mylib folder, or change mylib to the respective folder name
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy
