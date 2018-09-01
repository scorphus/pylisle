#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Lisle
# https://github.com/scorphus/pylisle

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2018, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from lisle import find_best_link_station


def test_find_best_link_station():
    assert find_best_link_station(None, None)
