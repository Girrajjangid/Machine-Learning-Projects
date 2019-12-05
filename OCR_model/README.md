# Date Extractor OCR Engine

## Aim: 
1. To build an OCR model that extracts only Expense date from ﬁnancial or any transaction receipts. 

## Sample Image:

We have to extract marked date in **YYYY-MM-DD** format.

![Alt text](https://github.com/Girrajjangid/Machine-learning-projects-deployment/blob/master/03.%20TextExtractor_OCR(Deploy_AWS)/sample.png)

## Let's Start:
*Run the following commands in terminal.*

```
git clone https://github.com/Girrajjangid/Machine-learning-projects-deployment.git
```

1. It ensures that you have required libraries.

```
pip install -r requirements.txt
```

2. Finding date by passing image path.

```
python model.py sample.png
```

`Expected Output:`

> With (3,3) filter and First preprocessed :  2017-05-09

> With (5,5) filter and First preprocessed :  2017-05-09

> With (7,7) filter and First preprocessed :  2017-05-09

> {'date': '2017-05-09'}

## Working flow diagram:

![alt text](https://github.com/Girrajjangid/Machine-learning-projects-deployment/blob/master/03.%20TextExtractor_OCR(Deploy_AWS)/utils/3.jpg)

## Problem which I faced:

It's really hard to recognize date format when in transaction receipt country code or name is not mentioned.

For example: 2/8/19 is either 2nd-August-2019 or 8th-feb-2019.

I even try to find country name by using context text related to that country. But accuracy was not so good.

## Note:
For more detailed implementation please click [Here](https://github.com/Girrajjangid/Machine-learning-projects-deployment/tree/master/03.%20TextExtractor_OCR(Deploy_AWS))



