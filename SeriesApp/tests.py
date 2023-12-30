from django.test import TestCase
import datetime

current_year = datetime.datetime.now().year
YEAR_RANGES = [f"{start}-{end}" for start, end in zip(range(1950, current_year, 5), range(1955, current_year + 1, 5))]

print(YEAR_RANGES)