# -*- coding: utf-8 -*-
from att.models import Registrati11on, Attendance
import shutil
import csv

#Assuming only one file name. Will have to modify for multiple file names and figure out a way of naming.

arr=csv.reader(open('Unprocessed/1086.att', 'r'),delimiter='.')
#for row in arr:
row=arr.next()
a = Registration(School_ID=row[0],School_Name=row[1],Max_Students=row[2],Date=row[3])
a.save()

shutil.move("Unprocessed/1086.att", "Processed/1086.att")
