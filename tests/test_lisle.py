#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Lisle
# https://github.com/scorphus/pylisle

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2018, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from lisle import find_best_link_station
from pytest import fixture, mark


@fixture
def link_stations():
    return [(0, 0, 10), (20, 20, 5), (10, 0, 12)]


@mark.parametrize('device_point, output_line', [
    ((0, 0), 'Best link station for point 0,0 is 0,0 with power 100.0'),
    ((100, 100), 'No link station within reach for point 100,100'),
    ((15, 10), 'Best link station for point 15,10 is 10,0 with power 0.7'),
    ((18, 18), 'Best link station for point 18,18 is 20,20 with power 4.7'),
])
def test_find_best_link_station(link_stations, device_point, output_line):
    assert find_best_link_station(link_stations, device_point) == output_line
