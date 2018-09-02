<!--
This file is part of Lisle
https://github.com/scorphus/pylisle

Licensed under the BSD-3-Clause license:
https://opensource.org/licenses/BSD-3-Clause
Copyright (c) 2018, Pablo S. Blum de Aguiar <scorphus@gmail.com>
-->

# Lisle (Link Station Locator)

Lisle (Link Station Locator) helps you find the best link station based on its
reach and distance from a given device.

## Requirements

Lisle requires Python 3.5 or later.

## Installation

Just clone the repository and install with pip:

```bash
git clone git@github.com:scorphus/pylisle.git
pip install ./pylisle
```

## Usage

Below is a usage example:

```python
import lisle

link_stations = [(0, 0, 10), (20, 20, 5), (10, 0, 12)]
device_point = (0, 0)
print(lisle.find_best_link_station(link_stations, device_point))
```

The example above prints:

```text
Best link station for point 0,0 is 0,0 with power 100.00
```

## Documentation

This project is documented with [Sphinx](http://www.sphinx-doc.org) with autodoc
from docstrings. See the [docs](docs) directory.

## Developing and testing

To create a development environment, you should first create a virtualenv.
[pyenv](https://github.com/pyenv/pyenv) is recommended for easily switching
between multiple versions of Python and managing virtualenvs.

There are multiple [Makefile](Makefile) targets to help you:

- `make list`: list all available targets
- `make setup`: install in editable mode with all test dependencies
- `make flake8`: run flake8 for style guide enforcement
- `make unit`: run unit tests with coverage displayed in terminal
- `make test`: run `flake8` and `unit`
- `make coverage-html`: same as `unit` but also create HTML with visual coverage
- `make tox`: run tests against all supported python versions
- `make gendocs`: generate docs with Sphinx

## License

Code in this repository is distributed under the terms of the 3-Clause BSD
License (BSD-3-Clause).

See [LICENSE](LICENSE) for details.
