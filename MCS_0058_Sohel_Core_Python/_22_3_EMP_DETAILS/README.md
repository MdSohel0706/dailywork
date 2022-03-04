Project has 3 layers
                              PYTHON 
              =====================================
UI --1-->     Controller  --2--> Service --3--> DAO   --4--> Database
   <--8--                 <--7--         <--6--       <--5--
   
1. Controller : Receives request from client, processes data and call Service Layer  
                1 2 8
2. Service    : Implements business logic and call dao layer to perform db operations
                3 7 
3. DAO        : Interacts with Databse(postgrsql) and performs CRUD operations
                4 5 6  
 
1. Controller will receive the request from UI
2. Controller will validate the data,and 
          - sends to Service layer
          - else sends error message to UI
3. Service layer will implement the 'Business Logic'
          - transfers result data to dao layer
4. Dao layer,prepares the respective sql query(SELECT,INSERT,UPDATE,DELETE)
          - executes the query and sends to database
5. In database,query will be executed and 
          - results will be given to dao layer
6. dao layers passes the response to service layer
7. Service layer passes the response to controller layer
8. Controller layers passes the response to UI