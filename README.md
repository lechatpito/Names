Names
=====

Names.py: a Python program and module to generate random personal information: names, addresses, birth dates and emails

Install: python setup.py

Usage: names.py [-h] [--firstname] [--lastname] [--email] [--birthdate]
                [--address]

optional arguments:
  -h, --help   show this help message and exit
  --firstname  returns a first name
  --lastname   returns a last name
  --email      returns an email
  --birthdate  returns a birth date
  --address    returns an address

Description: Names allows to generate imaginary persons information at random: first name, last names, address, age and email.
The first and last names are taken from the 2010 US census data. Names are randomly selected with a higher probability to be picked up if they are more common. Address information is extracted from a list of localities in the US and the list of streets in New-York city. No postal code is generated so far. Birth date are generated to allow persons of 101 years old max. Emails are generated using a list of emails domains. 

Notice: it is recommended to use this program as a python library if used many times. The command line command is slow as data files are loaded at each execution. 

Disclaimer: This programme is only intended for fun or experiments needing random, fake persons name. All characters appearing in this work are fictitious. Any resemblance to real persons, living or dead, is purely coincidental. Do not to try matching the generated data with real persons or send messages to the generated emails. 
