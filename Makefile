# This file is part of Lisle
# https://github.com/scorphus/pylisle

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2018, Pablo S. Blum de Aguiar <scorphus@gmail.com>

# list all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
# required for list
no_targets__:

# install in editable mode with all test dependencies (requires a virtualenv)
setup:
	@PIP_REQUIRE_VIRTUALENV=true pip install -Uc constraints.txt -e .\[tests\]

# run flake8 for style guide enforcement
flake8:
	@flake8 2> /dev/null  # https://gitlab.com/pycqa/flake8/issues/437

# run unit tests with coverage displayed in terminal
unit:
	@pytest -sv --cov-config setup.cfg --cov lisle tests

# run `flake8` and `unit`
test: flake8 unit

# same as `unit` but also create HTML with visual coverage
coverage-html:
	@pytest -sv --cov-config setup.cfg --cov lisle \
		--cov-report term-missing --cov-report html tests

# run tests against all supported python versions
tox:
	@tox

.PHONY: list setup flake8 unit test coverage-html tox
