#
DEFAULT: help
.DEFAULT: help

VE_DIR = venv
BIN_DIR = $(VE_DIR)/bin
PIP_CMD = $(BIN_DIR)/pip
PYTHON_CMD = $(BIN_DIR)/python
NOSE_CMD = $(BIN_DIR)/nosetests
FLAKE8_CMD = $(BIN_DIR)/flake8
# Reset the commands when running with travis.
ifdef TRAVIS
	NOSE_CMD = nosetests
	FLAKE8_CMD = flake8
	PIP_CMD = pip
	PYTHON_CMD = python3
endif
#
SYS_PYTHON = python3
#
NOSE_ARGS =
FLAKE8_ARGS =


dev:
	pyvenv $(VE_DIR)
	$(PIP_CMD) install versioneer==0.16
	$(PIP_CMD) install -r tests/requirements.txt
	$(PIP_CMD) install -r requirements.txt
	$(PIP_CMD) install iPython
	$(PYTHON_CMD) setup.py develop

test:
	@echo "Using flake8 command: $(FLAKE8_CMD)"
	@echo "   with args: $(FLAKE8_ARGS)"
	$(FLAKE8_CMD)
	@echo "Usng nose command: $(NOSE_CMD)"
	@echo "   with args: $(NOSE_ARGS)"
	$(NOSE_CMD) $(NOSE_ARGS)

clean:
	rm -rf $(VE_DIR)
	rm -rf build
	rm -rf dist
	rm -rf __pycache__
	rm -rf lib/*.egg-info

help:
	@echo "Choose from the following:"
	@echo "	dev		Create virtualenv for development."
	@echo "	test		Run unit tests using nose (from virtualenv."
	@echo "	clean		Delete various development files and dirs."
	@echo "	help		This message."
# End of file.
