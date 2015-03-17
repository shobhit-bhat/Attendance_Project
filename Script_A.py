# -*- coding: utf-8 -*-
from att.models import Registration, Attendance
import shutil
import csv

#Assuming only one file name. Will have to modify for multiple file names and figure out a way of naming.

file=csv.reader(open('Unprocessed/a.*.att', 'r'),delimiter='.')
arr=file.next()
entry = Attendance(Registration=arr[0],Date=arr[1],Attendance=arr[2])
entry.save()
shutil.move("Unprocessed/a.*.att", "Processed/a.*.att")
