# Steps:
First create a bucket in which data has to be pushed and also upload all required files 
Create a dataset in big query  and a table inside that data set
Create a data flow which will push data in table 
create a cloud function which will automatically trigger the data flow when new data (.csv or other) file will get uploaded.