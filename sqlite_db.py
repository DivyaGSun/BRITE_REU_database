import sqlite3

conn = sqlite3.connect('BRITEREU.db')
c = conn.cursor()

#drop tables - can comment out when tables are ready
c.execute('DROP TABLE Applicant;')
c.execute('DROP TABLE Reviewer;')
c.execute('DROP TABLE Review;')

#create table Applicant
c.execute('''create table if not exists Applicant(
				aid integer not null primary key,
				firstname text,
				lastname text,
				emailaddress text,
				state text,
				city text,
				country text,
				dateofbirth date,
				gender text,
				citizen text,
				firstgen text,
				veteran text,
				hispanicorlatino text,
				whengradschool integer,
				race text,
				housing text,
				institution text,
				standing text,
				major text,
				gpa float,
				communitycollege text,
				computationalexperience text,
				howheardabout text,
				reviewstatus text,
				submitdate date, 
				documents blob);''')


#create table Reviewer
c.execute('''create table if not exists Reviewer(
				rid integer not null primary key,
				lname text,
				fname text);''')
				
				
#create table Review 
c.execute('''create table if not exists Review(
				aid integer,
				rid integer,
				primary key(aid, rid),
				foreign key(aid)
					references Applicant(aid),
				foreign key(rid)
					references Reviewer(rid));''')

#create table Candidate
c.execute('''create table if not exists Candidate(
				cid integer not null primary key,
				ranking text,
				assigned text);''')


conn.commit()
conn.close()		

#import data from csv file
import pandas as pd
from pandas import DataFrame

conn = sqlite3.connect('BRITEREU.db')
c = conn.cursor()

read_file = pd.read_csv('BU_BRITE_REU_2021_Application_F2021-03-06_19_43_49_shuffle.csv')
read_file.columns = read_file.columns.str.replace('\s+', '').str.lower()  #can change the '' to '_' if that is better
read_file.to_sql('Applicant', conn, if_exists='append', index=False)
