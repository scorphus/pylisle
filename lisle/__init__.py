#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Lisle
# https://github.com/scorphus/pylisle

# Licensed under the BSD-3-Clause license:
# https://opensource.org/licenses/BSD-3-Clause
# Copyright (c) 2018, Pablo S. Blum de Aguiar <scorphus@gmail.com>

'''Lisle – Link Station Locator

This module provides the :py:meth:`find_best_link_station` function that solves
the most suitable (with most power) link station (x, y, r) for a device at given
point (x, y).

Link stations are provided as a list of tuples. Each tuple represents a single
link station ``(x, y, r)`` – ``x`` and ``y`` are its location and ``r`` its
reach.

Point where device is located is given as a tuple ``(x, y)``.

Note: ``x``, ``y`` and ``r`` are expected to be numeric values.

'''

from functools import partial


def calc_power(link_station, device_point):
    '''Helper function that calculates the distance from a link station to the
    point where a device is located.

    :arg tuple link_station: The link station
    :arg tuple device_point: The point where the device is located
    :return: The distance from the station to the device
    :rtype: float
    '''
    station_x, station_y, reach = link_station
    point_x, point_y = device_point
    distance = pow(pow(station_x - point_x, 2) + pow(station_y - point_y, 2), 0.5)
    return 0.0 if distance > reach else pow(reach - distance, 2)


def find_best_link_station(link_stations, device_point):
    '''Finds the best link station for a device based on its reach and distance
    from the point where the device is located.

    :arg list link_stations: The list of link stations
    :arg tuple device_point: The point where the device is located
    :return: A sentence with the result of the search
    :rtype: str
    '''
    best_station, max_power = None, 0.0
    for station in link_stations:
        power = calc_power(station, device_point)
        if max_power < power:
            best_station, max_power = station, power
    if not max_power:
        return 'No link station within reach for point {},{}'.format(*device_point)
    return 'Best link station for point {},{} is {},{} with power {:.1f}'.format(
        *device_point, *best_station[:2], max_power
    )


def _find_best_link_station_with_max(link_stations, device_point):
    '''Same as find_best_link_station but using `max`.

    :arg list link_stations: The list of link stations
    :arg tuple device_point: The point where the device is located
    :return: A sentence with the result of the search
    :rtype: str
    '''
    calc_power_from_point = partial(calc_power, device_point=device_point)
    best_station = max(link_stations, key=calc_power_from_point)
    power = calc_power(best_station, device_point)
    if not power:
        return 'No link station within reach for point {},{}'.format(*device_point)
    return 'Best link station for point {},{} is {},{} with power {:.1f}'.format(
        *device_point, *best_station[:2], power
    )


def _find_best_link_station_with_sorted(link_stations, device_point):
    '''Same as find_best_link_station but using `sorted`.

    :arg list link_stations: The list of link stations
    :arg tuple device_point: The point where the device is located
    :return: A sentence with the result of the search
    :rtype: str
    '''
    calc_power_from_point = partial(calc_power, device_point=device_point)
    sorted_tuples = sorted(link_stations, key=calc_power_from_point)
    power = calc_power(sorted_tuples[-1], device_point) if sorted_tuples else 0
    if not power:
        return 'No link station within reach for point {},{}'.format(*device_point)
    return 'Best link station for point {},{} is {},{} with power {:.1f}'.format(
        *device_point, *sorted_tuples[-1][:2], power
    )
