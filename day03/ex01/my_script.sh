#!/bin/bash

pip --version

sleep 2
python3 -m pip install --log path.log --target=local_lib --force-reinstall --upgrade git+https://github.com/jaraco/path.py.git
if [ $? -eq 0 ]; then
	PYTHONPATH=local_lib python3 my_program.py
else
	echo "Install path failed"
fi