# create install instruction to pip install requirements.txt
install: requirements.txt
	pip install -r requirements.txt
# solving issue make: *** No rule to make target 'install'.  Stop.
# https://stackoverflow.com/questions/2145590/what-is-the-purpose-of-phony-in-a-makefile


