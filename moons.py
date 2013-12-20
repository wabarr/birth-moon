#the astral module deals nicely with moon phases http://pythonhosted.org/astral/module.html

import astral, datetime
a = astral.Location()
a.moon_phase(datetime.date(1911,02,13))

#returns an integer from 0 - 27 representing moon phase
# 0 = New moon
# 7 = First quarter
# 14 = Full moon
# 21 = Last quarter
