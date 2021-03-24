import sqlite3

conn = sqlite3.connect('BRITEREU.db')
c = conn.cursor()

#create table Applicant
c.execute('''create table Applicant(
				aid integer not null auto_increment primary key,
				fname text,
				lname text,
				email text,
				state text,
				city text,
				country text,
				dob date,
				gender text,
				citizen text,
				firstgen text,
				veteran text,
				hispanic text,
				gradyear integer,
				race text,
				housing text,
				institution text,
				standing text,
				major text,
				gpa float,
				comcollege text,
				experience text,
				referenced text,
				reviewstatus text,
				submitdate date, 
				documents blob);''')


#create table Reviewer
c.execute('''create table Reviewer(
				rid integer not null auto_increment primary key,
				lname text,
				fname text);''')
				
				
#create table Review 
c.execute('''create table Review(
				aid integer,
				rid integer,
				primary key(aid, rid),
				foreign key(aid)
					references Applicant(aid),
				foreign key(rid)
					references Reviewer(rid));''')	

conn.commit()
conn.close()		

#import data from csv file
import pandas as pd
from pandas import DataFrame

conn = sqlite3.connect('BRITEREU.db')
c = conn.cursor()

read_file = pd.read_csv(r'BU_BRITE_REU_2021_Application_F2021-03-06_19_43_49_shuffle.csv')
read_file.to_sql('Applicants', conn, if_exists='append', index=False)
