#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from department import Department
import ipdb

Department.drop_table()
Department.create_table()

# Create departments
payroll = Department.create("Payroll", "Building A, 5th Floor")
hr = Department.create("HR", "Building F, 10th Floor")

# Query them back
print(Department.find_by_id(1))  # <Department 1: Payroll, Building A, 5th Floor>
print(Department.all())          # [<Department 1: Payroll, ...>, <Department 2: HR, ...>]

ipdb.set_trace()
