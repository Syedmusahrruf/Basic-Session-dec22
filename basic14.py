from datetime import date
f_date = date(2022, 12, 12)
l_date = date(2022, 12, 19)
delta = l_date - f_date
print(delta.days)