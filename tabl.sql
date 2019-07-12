    CREATE TABLE CHEZHIYA( id int NOT NULL,
    primary key(id),
     name        VARCHAR(20) NULL,
    age     int NOT NULL,
    address VARCHAR(20) NOT NULL,
    salary       int NOT NULL
    );
    insert into CHEZHIYA values(1,'RAMESH',32,'AHMEDABAD',2000);
    insert into CHEZHIYA values(2,'KHILAN',25,'DELHI',1500);
    insert into CHEZHIYA values(3,'KAUSHIK',23,'KOTA',2000);
    insert into CHEZHIYA values(4,'CHAITALI',25,'MUMBAI',6500);
    insert into CHEZHIYA values(5,'HARDIK',27,'BHOPAL',8500);
    insert into CHEZHIYA values(6,'KOMAL',22,'MP',4500);
    insert into CHEZHIYA values(7,'MUFFY',24,'INDORE',10000);
    UPDATE CHEZHIYA SET ADDRESS='MAHARASHTRA' WHERE NAME ='KOMAL';
    SELECT * FROM CHEZHIYA WHERE age = '32' or age='22';
    
