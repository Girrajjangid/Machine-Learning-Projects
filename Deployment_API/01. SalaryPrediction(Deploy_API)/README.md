## ML-Model-Flask-Deployment

In this project we deploy salary prediction model as a API using flask library.

**Note:** It's always better to write model and API code in different files.

### Project Structure
This project has four major parts :
1. _model.py_ - This file contains Modelling/Training.
2. _app.py_ - This contains Flask APIs code that receives employee details from GUI or API calls.
3. _request.py_ - This file used to test API.
4. _templates_ - This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee salary.

Ensure that you are in the project home directory.

***Warning: It's better to see requirements.txt file first because if you directly run this command may be you get install old version of libraries.***

### Steps to run the project

**1.**  Install required libararies. It ensures that you have the correct libraries.
```
pip install -r requirements.txt
```

**2.** Create the machine learning model by running below command -
```
python model.py
```
Expected Output 

> Model Saved Successfully.

This would create a serialized file of our model as model.pkl


**3.** Create Flask API server(uWSGI server) by using below command -
```
python api.py
```
This create a WSGI mini server which responsible for communication between web to python.
By default, flask will run on port 5000.

**4.** Navigate to URL http://localhost:5000/

Now you will see something like this:

![alt text](https://github.com/Girrajjangid/Machine-Learning-Projects/blob/master/Deployment_API/01.%20SalaryPrediction(Deploy_API)/images/1.png)

Enter valid numerical values in all 3 input boxes and hit Predict.

If everything goes well, you should  be able to see the predicted salary value on the HTML page!

![alt text](https://github.com/Girrajjangid/Machine-Learning-Projects/blob/master/Deployment_API/01.%20SalaryPrediction(Deploy_API)/images/2.png)


**5.** You cannot directly access this URL http://localhost:5000/predict_api. You need some kind of API client which send your request to flask.

*5.1.* You can send your request by using [Postman](https://www.getpostman.com/downloads/).Download this application.

Postman application is used for to test our API's.

After installation you would see something like this:

![alt text](https://github.com/Girrajjangid/Machine-Learning-Projects/blob/master/Deployment_API/01.%20SalaryPrediction(Deploy_API)/images/3.png)

> Here, Enter http://localhost:5000/predict_api on Post method

> Enter details in body.

*5.2.* You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to send the request with some pre-popuated values -

```
python request.py
```
or
```
run request.ipynb
```




