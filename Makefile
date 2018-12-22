PYTHON=./venv/bin/python3
build:
	python3 -m venv venv
	${PYTHON} -m pip install -r requirements.txt
	chmod +x obj_finder.py
	chmod +x grep.py
