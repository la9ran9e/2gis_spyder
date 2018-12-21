PYTHON=./venv/bin/python3.6
build:
	python3.6 -m venv venv
	${PYTHON} -m pip install -r requirements.txt
	chmod +x obj_finder.py
	chmod +x grep.py
