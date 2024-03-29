#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Lisle
# https://github.com/scorphus/pylisle

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2018, Pablo S. Blum de Aguiar <scorphus@gmail.com>

from pytest import approx, fixture, mark
from random import randint

import lisle


@fixture
def link_stations():
    return [(0, 0, 10), (20, 20, 5), (10, 0, 12)]


random_link_stations = [
    (randint(0, 50), randint(0, 50), randint(0, 100)) for _ in range(1000)
]


@mark.parametrize('link_station, device_point, power', [
    ((0, 0, 10), (0, 0), 100),
    ((0, 0, 10), (100, 100), 0),
    ((0, 0, 10), (15, 10), 0),
    ((0, 0, 10), (18, 18), 0),
    ((20, 20, 5), (0, 0), 0),
    ((20, 20, 5), (100, 100), 0),
    ((20, 20, 5), (15, 10), 0),
    ((20, 20, 5), (18, 18), 4.7),
    ((10, 0, 12), (0, 0), 4),
    ((10, 0, 12), (100, 100), 0),
    ((10, 0, 12), (15, 10), 0.7),
    ((10, 0, 12), (18, 18), 0),
])
def test_calc_power(link_station, device_point, power):
    assert lisle.calc_power(link_station, device_point) == approx(power, 0.1)


@mark.parametrize('device_point, output_line', [
    ((0, 0), 'Best link station for point 0,0 is 0,0 with power 100.0'),
    ((100, 100), 'No link station within reach for point 100,100'),
    ((15, 10), 'Best link station for point 15,10 is 10,0 with power 0.7'),
    ((18, 18), 'Best link station for point 18,18 is 20,20 with power 4.7'),
])
def test_find_best_link_station(link_stations, device_point, output_line):
    assert lisle.find_best_link_station(link_stations, device_point) == output_line


@mark.parametrize('device_point, output_line', [
    ((0, 0), 'Best link station for point 0,0 is 0,0 with power 100.0'),
    ((100, 100), 'No link station within reach for point 100,100'),
    ((15, 10), 'Best link station for point 15,10 is 10,0 with power 0.7'),
    ((18, 18), 'Best link station for point 18,18 is 20,20 with power 4.7'),
])
def test_find_best_link_station_with_max(link_stations, device_point, output_line):
    assert lisle._find_best_link_station_with_max(link_stations, device_point) == output_line


@mark.parametrize('device_point, output_line', [
    ((0, 0), 'Best link station for point 0,0 is 0,0 with power 100.0'),
    ((100, 100), 'No link station within reach for point 100,100'),
    ((15, 10), 'Best link station for point 15,10 is 10,0 with power 0.7'),
    ((18, 18), 'Best link station for point 18,18 is 20,20 with power 4.7'),
])
def test_find_best_link_station_with_sorted(link_stations, device_point, output_line):
    assert lisle._find_best_link_station_with_sorted(link_stations, device_point) == output_line


@mark.benchmark
def test_bench_find_best_link_station(benchmark):
    assert benchmark(lisle.find_best_link_station, random_link_stations, (0, 0))


@mark.benchmark
def test_bench_find_best_link_station_with_max(benchmark):
    assert benchmark(lisle._find_best_link_station_with_max, random_link_stations, (0, 0))


@mark.benchmark
def test_bench_find_best_link_station_with_sorted(benchmark):
    assert benchmark(lisle._find_best_link_station_with_sorted, random_link_stations, (0, 0))
