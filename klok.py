"""
klok, convert times into Dutch words
"""

import datetime as _datetime
import functools as _functools

import telwoord as _telwoord


__all__ = ['tell_time']


def _to_human_hour(h):
    h = h % 12
    return h if h > 0 else 12


_spell_out = _functools.partial(_telwoord.cardinal, friendly=False)


def tell_time(dt=None, hour=None, minute=None, part_of_day=True):
    """
    TODO: docstring
    """
    if dt is not None:
        if not isinstance(dt, (_datetime.time, _datetime.datetime)):
            raise TypeError("'dt' argument must be a time or datetime")
        if hour is None:
            hour = dt.hour
        if minute is None:
            minute = dt.minute
    else:
        if not 0 <= hour < 24:
            raise TypeError("hour must be between 0 and 23 inclusive")
        if not 0 <= minute < 60:
            raise TypeError("minute must be between 0 and 59 inclusive")

    # From 16 minutes past the hour we pronounce the next hour. Weird
    # but true.
    if minute <= 15:
        hour_adjusted = hour
    else:
        hour_adjusted = hour + 1 % 24
    s_hour = _spell_out(_to_human_hour(hour_adjusted))

    if minute == 0:
        s = u"{0} uur".format(s_hour)
    elif minute < 15:
        s = u"{0} over {1}".format(_spell_out(minute), s_hour)
    elif minute == 15:
        s = u"kwart over {0}".format(s_hour)
    elif minute < 30:
        s = u"{0} voor half {1}".format(_spell_out(30 - minute), s_hour)
    elif minute == 30:
        s = u"half {0}".format(s_hour)
    elif minute < 45:
        s = u"{0} over half {1}".format(_spell_out(minute - 30), s_hour)
    elif minute == 45:
        s = u"kwart voor {0}".format(s_hour)
    else:
        s = u"{0} voor {1}".format(_spell_out(60 - minute), s_hour)

    if part_of_day:
        if hour == 0 and minute == 0:
            # Spooky case, eh, special case.
            s = u"middernacht"
        else:
            n = hour * 100 + minute
            if n <= 601:
                # The phrase "zes uur 's nachts" is much more common than
                # "zes uur 's ochtends".
                suffix = u"'s nachts"
            elif n < 1200:
                suffix = u"'s ochtends"
            elif n < 1801:
                # The phrase "zes uur 's middags" is much more common than
                # "zes uur 's avonds".
                suffix = u"'s middags"
            else:
                suffix = u"'s avonds"
            s = u"{0} {1}".format(s, suffix)

    return s
