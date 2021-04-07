
BEGIN TRANSACTION;

/*******************************************************************************
   Drop Tables
********************************************************************************/

DROP TABLE IF EXISTS Applicant;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Review;
/*******************************************************************************
   Create Tables
********************************************************************************/


CREATE TABLE Applicant (
  aid integer not null auto_increment primary key,
	fname text,
	lname text,
	email text,
	state text,
	city text,
	country text,
	dob text,
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
	compexperience text,
	referenced text,
	reviewstatus text,
	submitdate text,
	documents blob
) WITHOUT ROWID;


create table User (
  uid integer not null auto_increment primary key,
  	lname text,
  	fname text,
  	role text, 
) WITHOUT ROWID;



create table Review (
  aid integer,
	uid integer,
	primary key(aid, uid),
	foreign key(aid) references Applicant(aid),
	foreign key(uid) references User(uid)
) WITHOUT ROWID;
--*******************************************************

COMMIT;
