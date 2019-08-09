lint:
    pylint --disable=R,C, W1203 main.py

install:
    # pip install --upgrade pip &&\
    pip install -r requirements.txt

#run:
	#python main.py 

#test:
    #pytest
#all:
	#make install 
	#make lint
    #call all scripts/commands