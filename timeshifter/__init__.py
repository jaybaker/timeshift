"""
A simple time zone conversion utility with 
Daylight Saving Time conversion implementation.
It is absurdly myopic, only covering the United States of America.
It is only valid through 2025.

With all these faults it is also highly effective.
It does not need any database or service calls. 
It can simply be imported and used. 
It has no dependencies.
It can also be extended beyond 2025 or changed if 
the rules change as it is very simple.

This is not the Olson database.

Usage:
    >>> import timeshift
    >>> my_date = timeshift.est(date_in_utc)
"""

from datetime import datetime as dt, timedelta

# the format for the rules is they are indexed by year
# the first date is when DST begins in local time
# the second date is when DST ends in local
_rules = {2009: (dt(2009, 3, 8, 2, 0),  dt(2009, 11, 1, 2, 0)),
          2010: (dt(2010, 3, 14, 2, 0), dt(2010, 11, 7, 2, 0)),
          2011: (dt(2011, 3, 13, 2, 0), dt(2011, 11, 6, 2, 0)),
          2012: (dt(2012, 3, 11, 2, 0), dt(2012, 11, 4, 2, 0)),
          2013: (dt(2013, 3, 10, 2, 0), dt(2013, 11, 3, 2, 0)),
          2014: (dt(2014, 3, 9, 2, 0),  dt(2014, 11, 2, 2, 0)),
          2015: (dt(2015, 3, 8, 2, 0),  dt(2015, 11, 1, 2, 0)),
          2016: (dt(2016, 3, 13, 2, 0), dt(2016, 11, 6, 2, 0)),
          2017: (dt(2017, 3, 12, 2, 0), dt(2017, 11, 5, 2, 0)),
          2018: (dt(2018, 3, 11, 2, 0), dt(2018, 11, 4, 2, 0)),
          2019: (dt(2019, 3, 10, 2, 0), dt(2019, 11, 3, 2, 0)),
          2020: (dt(2020, 3, 8, 2, 0),  dt(2020, 11, 1, 2, 0)),
          2021: (dt(2021, 3, 14, 2, 0), dt(2021, 11, 7, 2, 0)),
          2022: (dt(2022, 3, 13, 2, 0), dt(2022, 11, 6, 2, 0)),
          2023: (dt(2023, 3, 12, 2, 0), dt(2023, 11, 5, 2, 0)),
          2024: (dt(2024, 3, 10, 2, 0), dt(2024, 11, 3, 2, 0)),
          2025: (dt(2025, 3, 9, 2, 0),  dt(2025, 11, 2, 2, 0)),
        }

# when DST is in effect, UTC is 4 hours ahead of EDT
# when DST is not in effect, UTC is 5 hours ahead of EST

def between(test, dates):
    return test >= dates[0] and test < dates[1]

def offset(utc, delta=0):
    standard = utc + timedelta(hours=delta)
    if hasattr(utc, 'year'):
        yr = utc.year
    else:
        yr = dt.utcnow().year
    rule = _rules.get(yr, _rules[2025])
    # if in DST
    if between(standard, rule):
        offset = 1
    else:
        offset = 0
    dst_corrected = standard + timedelta(hours=offset)

    # now check if the corrected time is in that
    # 'does not exist' hour just after DST end
    rollback_window = (rule[1], rule[1] + timedelta(hours=1))
    if between(dst_corrected, rollback_window) and between(standard, rule):
        dst_corrected = dst_corrected + timedelta(hours=-1)
    return dst_corrected

def _delta(val):
    return lambda x: offset(x, delta=val)

# for convenience, represent some commonly used
# timezones given their standard time offsets from UTC
est = _delta(-5)
edt = est
cst = _delta(-6)
cdt = cst
mst = _delta(-7)
mdt = mst
pst = _delta(-8)
pdt = pst
