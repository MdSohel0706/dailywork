'''
CRUD
----------------------------------------------------------------------
UI                          Backend                     Database
----------------------------------------------------------------------
HTML         --->           Python                   ---> Postgresql
             --->  controller ->  service -> dao      <---
             <--             <-          <-

       VIEW              CONTROLLER            MODEL

REQ :  Signup functionality for MMAil   [Username Password MobileNo EmailID DOB Location]
        Frontend - Backend

MVC Architecture:
-----------------
CONTROLLER : 1. Receives request from UI*
             2*. Extract the data*
             3*. Perform server side validations
             4. If validation success -> 4.1. Send data to service layer
                              fails   -> 4.2. Send exception message to UI
            13. Receive the data from Service, and send to UI

SERVICE    : 5. Receives the data from Controller
             6*. Implement business logic for the given requirement
             7. Send the final data to DAO layer
            12. Receive the data from DAO , perform other operations on data and Send the response to Controller

DAO        : 8. Receive the data from Service
             9*. Prepare respective SQL Query (CRUD)
             10*.Execute query and commit the transaction with DB
             11. Send response to Service

SQL   -> Postgres Mysql Sqlite SQLServer Oracle
NoSQL -> Mongodb Cassandra
         Elastic Search
CLASS OBJECT : LOGICAL PHYSICAL 

CREATE    : CREATE TABLE EMPLOYEE(EID NAME SAL)
            INSERT INTO EMPLOYEE VALUES(100,'MADHU',1000)
RETRIEVE  : SELECT * FROM EMPLOYEE WHERE EID = 100
UPDATE    : UPDATE EMP SET SAL = 1500 WHERE EID = 100
DELETE    : DELETE FROM EMP WHERE EID = 100
'''

