import datetime

import klok

import pytest


@pytest.mark.parametrize(('hour', 'minute', 'expected'), [
    (3, 0, u"drie uur"),
    (0, 0, u"twaalf uur"),
    (12, 0, u"twaalf uur"),
    (19, 0, u"zeven uur"),

    (0, 10, u"tien over twaalf"),
    (2, 14, u"veertien over twee"),
    (20, 3, u"drie over acht"),

    (3, 15, u"kwart over drie"),
    (3, 45, u"kwart voor vier"),
    (23, 45, u"kwart voor twaalf"),
    (12, 45, u"kwart voor een"),

    (0, 16, u"veertien voor half een"),
    (4, 20, u"tien voor half vijf"),
    (23, 29, u"een voor half twaalf"),

    (3, 30, u"half vier"),
    (0, 30, u"half een"),
    (16, 30, u"half vijf"),
    (23, 30, u"half twaalf"),

    (0, 31, u"een over half een"),
    (3, 38, u"acht over half vier"),
    (21, 35, u"vijf over half tien"),

    (0, 45, u"kwart voor een"),
    (3, 45, u"kwart voor vier"),
    (11, 45, u"kwart voor twaalf"),
    (23, 45, u"kwart voor twaalf"),

    (0, 50, u"tien voor een"),
    (2, 53, u"zeven voor drie"),
    (5, 59, u"een voor zes"),
    (23, 46, u"veertien voor twaalf"),
])
def test_tell_time(hour, minute, expected):
    actual = klok.tell_time(
        hour=hour,
        minute=minute,
        part_of_day=False)
    assert actual == expected


def test_datetime_module_support():
    dt = datetime.time(6, 12)
    actual = klok.tell_time(dt, part_of_day=False)
    expected = "twaalf over zes"
    assert actual == expected

    dt = datetime.datetime(2015, 1, 1, 6, 12)
    actual = klok.tell_time(dt, part_of_day=False)
    expected = "twaalf over zes"
    assert actual == expected


@pytest.mark.parametrize(('hour', 'minute', 'expected'), [
    (0, 0, "twaalf uur 's nachts"),
    (0, 10, u"tien over twaalf 's nachts"),
    (4, 55, u"vijf voor vijf 's nachts"),
    (5, 0, u"vijf uur 's nachts"),
    (5, 15, u"kwart over vijf 's nachts"),
    (5, 20, u"tien voor half zes 's nachts"),
    (6, 0, u"zes uur 's nachts"),
    (6, 3, u"drie over zes 's ochtends"),
    (11, 50, u"tien voor twaalf 's ochtends"),
    (12, 0, "twaalf uur 's middags"),
    (12, 30, "half een 's middags"),
    (17, 00, "vijf uur 's middags"),
    (17, 50, "tien voor zes 's middags"),
    (18, 0, "zes uur 's middags"),
    (18, 5, "vijf over zes 's avonds"),
    (23, 55, "vijf voor twaalf 's avonds"),
])
def test_part_of_day(hour, minute, expected):
    actual = klok.tell_time(
        hour=hour,
        minute=minute)
    assert actual == expected
