#!/usr/bin/env python3

"""
OPS435 Assignment 1 - Winter 2020
Program: a1_jbinos.py
Author: James Binos
The python code in this file (a1_jbinos.py) is original work written by
James Binos. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
"""

#Import modukes
import sys
import os


def usage():
	'''
	The usage() function will take no argument and return a string
	describing the usage of the script.
	'''
	if ((len(sys.argv) != 4) and len(sys.argv) != 3):
		print(sys.argv[0] + '[--step] YYYY-MM-DD +/-n')
		exit()

def dbda(date, days): 
	'''
	The dbda() function accepts 2 arguments, a date and a number as the number of days. The function then adds or subtracts
	the given number to the given date.
	Example:
	dbda(2020-01-01, 5)
	2020-01-06  
	'''
	#Checking format is valid
	if len(days) == 10:
		valid_date(days)

		day_counter = 0
		temp_day = days

		if date > days:

			while date > temp_day:
				temp_day = after(temp_day)
				day_counter = day_counter + 1
			
		elif temp_day > date:
			while date != temp_day:
				temp_day = before(temp_day)
				day_counter = day_counter + 1

		print(day_counter)

	else:
		valid_date(date)
		
		str_year, str_month, str_day = date.split('-')
		year = int(str_year)
		month = int(str_month)
		day = int(str_day)

		counter = int(days)
		new_date = date

		if counter > 0:
			while counter != 0:
				if sys.argv[1] == '--step':
					new_date = after(new_date)
					counter = counter - 1
					print(new_date)
				else:
					new_date = after(new_date)
					counter = counter - 1
		elif counter < 0:
			while counter != 0:
				if sys.argv[1] == '--step':
					new_date = before(new_date)
					counter = counter + 1
					print(new_date)
				else:
					new_date = before(new_date)
					counter = counter + 1
	if sys.argv[1] == '--step':
		print('',end='')
	else:
		print(new_date)

def after(date):
	'''
	The after() function accepts the date argument in "YYYY-MM-DD" format, and returns the date after the given one.
	Example:
	after(2020-01-20)
	2020-01-21
	'''
	
	#Separating the date argument
	str_year, str_month, str_day = date.split('-')
	year = int(str_year)
	month = int(str_month)
	day = int(str_day)
	#Next Day
	temp_day = day + 1
	temp_month = month
	mon_max = days_in_mon(year)

	#If days go over 31
	if temp_day > mon_max[month]:	#Resetting the date for new month
		temp_day = 1
		temp_month = month + 1

	#If months go over a year
	if temp_month > 12:	#Resetting the date for new year
		temp_day = 1
		temp_month = 1
		year = year + 1

	tomorrow = str(year) + "-" + str(temp_month).zfill(2) + "-" + str(temp_day).zfill(2)
	return tomorrow

def before(date):
	'''
	The before() function accepts the date argument in "YYYY-MM-DD" format, and returns the date before the given one.
	Example:
	before(2020-01-20)
	2020-01-19
	'''
	str_year, str_month, str_day = date.split('-')
	year = int(str_year)
	month = int(str_month)
	day = int(str_day)
	#Previous Day
	temp_day = day - 1
	temp_month = month
	mon_max = days_in_mon(year)

	#If days are less than 0, month will revert to previous one
	if temp_day == 0:
		temp_day = mon_max[month] - 2
		temp_month = month - 1
	#If month is less than one, it will revert back to previous year
	if temp_month == 0:
		temp_day = 31
		temp_month = 12
		year = year - 1

	yesterday = str(year) + "-" + str(temp_month).zfill(2) + "-" + str(temp_day).zfill(2)
	return yesterday

def valid_date(date):
	'''
	The valid_date() function takes the date argument in "YYYY-MM-DD" format, and returns True if the date is a valid date. 
	If not, it returns False and an error message.
	Example:
	valid_date(2020-01-01)
	True
	valid_date(abcde)
	False   
	'''

	#Checking to see date format is correct
	if len(str(date)) != 10:
		print('Error: wrong date entered')
		exit()
	
	str_year, str_month, str_day = date.split('-')
	year = int(str_year)
	month = int(str_month) 
	day = int(str_day)

	#Checking to see if month given is correct
	days_per_month = days_in_mon(year)
	if month not in days_per_month.keys():
		print('Error: wrong month entered')
		exit()

	#Checkingto see if days given is correct
	month_days_dictionary = days_in_mon(year)
	month_days = month_days_dictionary[month]

	if day not in range(1, month_days + 1):
		print('Error: wrong day entered')
		exit()

def leap_year(year):
	'''
	The leap_year() function accepts the year argument in "YYYY" format, 
	and returns True if the given year is a leap year, false if not.
	'''

	#Using modulus to check if given year is divisible by 4
	if (year % 4 == 0):
		if (year % 100 == 0):
			if (year % 400 ==0):
				is_leapyear = True
			else:
				is_leapyear = False
		else:
			is_leapyear = True
	else:
		is_leapyear = False
    		
	return is_leapyear

def days_in_mon(year):
	'''
	The days_in_mon() function accepts the year argument in "YYYY" format, 
	and returns a dictionary object which contains the total number of days in each month for the given year.
        Example:
	days_in_mon(2020)
	{1:31, 2:29, 3:31, 4:30, 5:31, 6:30...................} 
	'''
	#Using the leap_year() function to check year given is a leap year to determine days in Feb.
	if leap_year(year) == True:
		feb = 29
	else:
		feb = 28
	days_per_month = {1:31, 2:feb, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	return days_per_month

if __name__ == '__main__':
	usage()
	if sys.argv[1] == '--step':
		date = sys.argv[2]
		days = sys.argv[3]
	else:
		date = sys.argv[1]
		days = sys.argv[2]

	dbda(date, days)
