SHELL=/bin/bash

test: test_conf test_keys

test_%:
	pytest "test/$@.py"
