DROP DATABASE Pharm;
CREATE DATABASE Pharm;
USE DATABASE Pharm;

CREATE TABLE Doctor
{
DOC_ID int PRIMARY KEY AUTO_INCREMENT,
DOC_FIRST varchar(32) not null,
DOC_LAST varchar(32) not null,
DOC_PHONE varchar(10) not null
};

CREATE TABLE Patient
{
PAT_ID int PRIMARY KEY AUTO_INCREMENT,
PAT_SSN varchar(12) unique not null,
PAT_FIRST varchar(32) not null,
PAT_LAST varchar(32) not null,
PAT_DOB date
};

CREATE TABLE RX
{
RX_ID int PRIMARY KEY AUTO_INCREMENT,
DOC_ID int not null,
PAT_ID int not null,
DRU_ID int not null,
PAT_DATE date not null,
RX_REFILLS int not null,
RX_COST DECIMAL(10,2) not null,
FOREIGN KEY(DOC_ID) REFERENCES Doctor(DOC_ID) ON UPDATE RESTRICT ON DELETE RESTRICT,
FOREIGN KEY(PAT_ID) REFERENCES Patient(PAT_ID) ON UPDATE RESTRICT ON DELETE RESTRICT,
FOREIGN KEY(DRU_ID) REFERENCES DRUG(DRU_ID) ON UPDATE RESTRICT ON DELETE RESTRICT,
};

CREATE TABLE DRUG
{
DRU_ID int PRIMARY KEY AUTO_INCREMENT,
DRU_NAME varchar(30) not null
}

INSERT INTO Doctor(DOC_FIRST, DOC_LAST, DOC_PHONE) VALUES ("Mark", "Smith", "111-111-1111");
INSERT INTO Doctor(DOC_FIRST, DOC_LAST, DOC_PHONE) VALUES ("Mark", "Jones", "222-222-2222");
INSERT INTO Doctor(DOC_FIRST, DOC_LAST, DOC_PHONE) VALUES ("Mark", "Stump", "333-333-3333");

INSERT INTO Patient(PAT_SSN, PAT_FIRST, PAT_LAST) VALUES ("018-111-4512", "David", "Firby");
INSERT INTO Patient(PAT_SSN, PAT_FIRST, PAT_LAST) VALUES ("158-222-4512", "David", "Grant");
INSERT INTO Patient(PAT_SSN, PAT_FIRST, PAT_LAST) VALUES ("003-181-8812", "David", "Yen");

INSERT INTO DRUG(DRU_NAME) VALUES ("Monopril");
INSERT INTO DRUG(DRU_NAME) VALUES ("Paxil");
INSERT INTO DRUG(DRU_NAME) VALUES ("Avandia");

INSERT INTO RX(DOC_ID, PAT_ID, DRU_ID, PAT_DATE, RX_REFILLS, RX_COST) VALUES(1, 1, 1, "2015-01-15", 0, 50.00)
INSERT INTO RX(DOC_ID, PAT_ID, DRU_ID, PAT_DATE, RX_REFILLS, RX_COST) VALUES(2, 2, 2, "2014-09-14", 0, 65.00)
INSERT INTO RX(DOC_ID, PAT_ID, DRU_ID, PAT_DATE, RX_REFILLS, RX_COST) VALUES(3, 3, 3, "2015-03-13", 3, 75.00)
INSERT INTO RX(DOC_ID, PAT_ID, DRU_ID, PAT_DATE, RX_REFILLS, RX_COST) VALUES(1, 2, 3, "2015-11-13", 5, 100.00)
INSERT INTO RX(DOC_ID, PAT_ID, DRU_ID, PAT_DATE, RX_REFILLS, RX_COST) VALUES(2, 1, 2, "2012-05-11", 4, 75.00)
INSERT INTO RX(DOC_ID, PAT_ID, DRU_ID, PAT_DATE, RX_REFILLS, RX_COST) VALUES(3, 1, 2, "2015-04-12", 0, 50.00)
INSERT INTO RX(DOC_ID, PAT_ID, DRU_ID, PAT_DATE, RX_REFILLS, RX_COST) VALUES(1, 2, 2, "2013-05-14", 0, 65.00)
INSERT INTO RX(DOC_ID, PAT_ID, DRU_ID, PAT_DATE, RX_REFILLS, RX_COST) VALUES(2, 3, 1, "2015-10-13", 3, 75.00)
INSERT INTO RX(DOC_ID, PAT_ID, DRU_ID, PAT_DATE, RX_REFILLS, RX_COST) VALUES(2, 1, 3, "2014-05-12", 5, 100.00)
INSERT INTO RX(DOC_ID, PAT_ID, DRU_ID, PAT_DATE, RX_REFILLS, RX_COST) VALUES(3, 3, 1, "2016-01-01", 4, 75.00)

SELECT * FROM Doctors ORDER BY DOC_LAST, DOC_FIRST ASC;
SELECT * FROM Patient ORDER BY PAT_LAST, PAT_FIRST ASC;
SELECT * FROM DRUG ORDER BY DRU_NAME ASC;

SELECT DRUG_NAME FROM DRUG ORDER BY DRUG_NAME ASC;

SELECT AVG(RX_COST) FROM RX

SELECT SUM(RX.RX_COST)
  FROM RX
  INNER JOIN Patient
    ON RX.PAT_ID = PATIENT.PAT_ID
  WHERE PATIENT.PAT_LAST = 'Firby';

SELECT COUNT(RX_ID)
FROM RX
INNER JOIN DRUG
  ON RX.DRU_ID = DRUG.DRU_ID
WHERE DRUG DRU_NAME = 'Paxil';
