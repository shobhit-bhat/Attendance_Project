# -*- coding: utf-8 -*-
from att.models import Registration, Attendance
import shutil
import csv

#Assuming only one file name. Will have to modify for multiple file names and figure out a way of naming.

file=csv.reader(open('Unprocessed/r.*.att', 'r'),delimiter='.')
arr=file.next()
entry = Registration(School_ID=arr[0],School_Name=arr[1],Max_Students=arr[2],Date=arr[3])
entry.save()
shutil.move("Unprocessed/r.*.att", "Processed/r.*.att")
