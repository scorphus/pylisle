#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Lisle
# https://github.com/scorphus/pylisle

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2018, Pablo S. Blum de Aguiar <scorphus@gmail.com>


def find_best_link_station(link_stations, device_point):
    best_station, max_power = None, 0.0
    point_x, point_y = device_point
    for station in link_stations:
        station_x, station_y, reach = station
        distance = pow(pow(station_x - point_x, 2) + pow(station_y - point_y, 2), 0.5)
        power = 0.0 if distance > reach else pow(reach - distance, 2)
        if max_power < power:
            best_station, max_power = station, power
    if not max_power:
        return 'No link station within reach for point {},{}'.format(*device_point)
    return 'Best link station for point {},{} is {},{} with power {:.1f}'.format(
        *device_point, *best_station[:2], max_power
    )
