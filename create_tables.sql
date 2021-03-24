
BEGIN TRANSACTION;

--*******************************************************
-- Applicant table
-- use WITHOUT ROWID
-- NO ENUM so should we create a new table for those probably unnecessary?

DROP TABLE IF EXISTS Applicant;
CREATE TABLE Applicant (
  ApplicantID INT PRIMARY KEY,
  Lname TEXT NOT NULL,
  Fname TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  state TEXT,
  zip INT,
  city TEXT,
  country TEXT,
  straddress TEXT,
  phone TEXT NOT NULL UNIQUE,
  dob TEXT,
  gender TEXT,
  citizen/resident TEXT,
  firstgen INT,
  vet INT,
  Race TEXT,
  hispanic INT,
  revstatus TEXT,
  submit_date TEXT,
  gradschool TEXT,
  gradschool YEAR INT
  major TEXT,
  gpa REAL,
  Applicant_info BLOB
) WITHOUT ROWID;

--*******************************************************


--*******************************************************

COMMIT;
