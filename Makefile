lint:
	pylint --disable=R,C main.py
install:
	pip install -r requirements.txt
#run:
	#main.py 
#test:
    #pytest
all:
	install lint
    #call all scripts/commands