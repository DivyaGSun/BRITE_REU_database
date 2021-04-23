import sqlite3

conn = sqlite3.connect('BRITEREU.db')
c = conn.cursor()

#drop tables - can comment out when tables are ready
c.execute('DROP TABLE Applicant;')
c.execute('DROP TABLE User;')
c.execute('DROP TABLE Review;')
c.execute('DROP TABLE Candidate;')
c.execute('DROP TABLE Assignment;')
c.execute('DROP TABLE Faculty_Rank_Can;')

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


#create table User
c.execute('''create table if not exists User(
				uid integer not null primary key,
				lname text,
				fname text,
				username text UNIQUE,
				password text,
				role text);''')


#create table Review
c.execute('''create table if not exists Review(
				rid integer,
				aid integer,
				uid integer,
				reviews blob,
				created_at TEXT DEFAULT CURRENT_TIMESTAMP,
				primary key(rid),
				foreign key(aid)
					references Applicant(aid),
				foreign key(uid)
					references User(uid));''')

#create table Candidate
c.execute('''create table if not exists Candidate(
				cid integer not null primary key,
				assigned text);''')

#create table Project - this table stores faculty with their projects from the Input Projects page
#please feel free to change this table
c.execute('''create table if not exists Project(
				uid integer,
				project_name text,
				primary key(uid, project_name),
				foreign key(uid)
					references User(uid));''')

#create table Assignment - this table is used to store candidate and faculty assignment pairs from the Assign Candidates to Faculty Members page
c.execute('''create table if not exists Assignment(
				cid integer,
				uid integer,
				primary key(cid, uid),
				foreign key(cid)
					references Candidate(cid),
				foreign key(uid)
					references User(uid));''')

#create Faculty rank candidate table 
c.execute('''create table if not exists Faculty_Rank_Can(
				cid integer,
				uid integer, 
				rank integer,
				foreign key(cid)
					references Candidate(cid),
				foreign key(uid)
					references User(uid));''')


conn.commit()
conn.close()

#import data from csv file
import pandas as pd
from pandas import DataFrame

conn = sqlite3.connect('BRITEREU.db')
c = conn.cursor()

read_file = pd.read_csv('BU_BRITE_REU_2021_Application_F2021-03-06_19_43_49_shuffle.csv',encoding = "ISO-8859-1")
read_file.columns = read_file.columns.str.strip()
read_file.columns = read_file.columns.str.replace('\s+', '').str.lower()  #can change the '' to '_' if that is better
read_file.to_sql('Applicant', conn, if_exists='append', index=False)


#insert statements to add our names into user table
c.execute('''INSERT INTO User(lname, fname, role)
			Values('Chiaradio', 'Marissa', 'reviewer'), ('Knox', 'Kenzie', 'reviewer'), ('Patel', 'Janvee', 'reviewer'), ('Sundaresan', 'Divya', 'reviewer')''')

#insert statements to add sample faculty names into the user table
c.execute('''INSERT INTO User(lname, fname, role)
			Values('Z', 'A', 'faculty'), ('Y', 'B', 'faculty'), ('X', 'C', 'faculty'), ('W', 'D', 'faculty')''')


conn.commit()
conn.close()
