## ML-Model-Flask-Deployment

In this project we deploy salary prediction model as a flask API.

### Prerequisites
```pip install -r requirements.txt```

### Project Structure
This project has four major parts :
1. _model.py_ - This file contain Modelling.
2. _app.py_ - This contains Flask APIs that receives employee details through GUI or API calls.
3. _request.py_ - This file used to test API.
4. _templates_ - This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee salary.


### Steps to run the project.

1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

You should be able to view the homepage as below :
![alt text](http://www.thepythonblog.com/wp-content/uploads/2019/02/Homepage.png)

Enter valid numerical values in all 3 input boxes and hit Predict.

If everything goes well, you should  be able to see the predcited salary vaule on the HTML page!
![alt text](http://www.thepythonblog.com/wp-content/uploads/2019/02/Result.png)

4. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to send the request with some pre-popuated values -
```
python request.py
```
