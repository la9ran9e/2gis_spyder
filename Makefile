PYTHON=./venv/bin/python3
build:
	python3 -m venv venv
	${PYTHON} -m pip install -r requirements.txt
	chmod +x obj_finder.py grep.py store.sh packer.py \
		client.py server.py peer.py
	mkdir -p storage
