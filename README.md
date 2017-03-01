# LogisticRegressor
Single logistic regressor program with linear model to draw decision boundary and mark or predict class of test samples
--------------------------------------------------------------------------------------
Files in this directory:
logreg.py: 	Single logistic regressor program with linear model to draw decision boundary and mark or predict class of test samples
sample.csv:	Training sample file which should be used to build linear model
test1.csv:	Test dataset1 with linearly separable samples for which we need to predict classes
test2.csv   Test dataset2 with non-linearly separable samples for which we need to predict classes
			
How to run the single logistic regressor: 1. Make sure that all porgram and date files are in same folder 2. Run logreg.py python program by giving sample.csv as command line argument - Usage: python logreg.py samplefile 3. Program will run 'test1.csv' file by default. To make it run for test2.csv file, please update 107th line with test2.csv name instead of test1.csv 4. A graph will be plotted which shows spcific epoc vs sum of squared error for samples in each epoc 5. Please close the plot window, so that next plot of decision boundary can be plotted. 6. Decision boundary plot will be plotted with required results in console

Interpretations:
	1. First graph of epoc vs sqaured error for samples in each epoc tells us the error is getting reduced as we are updating weights per line per epoc.
	   Eventually, the curve is graph settles as parallel line after 60 epocs for test1.csv. This means, the weights are not changing that much.
	2. Second graph of decision boundary shows two decision surfaces with class 0 and class 1. It shows data points with predicted class values. 
	   The blue color is tagged with class 0 and red color is tagged with class 1. 
	3. From results in console and plotted graph, we can say that test1 file has linearly separable data where we have two decision surfaces for class 1 
	   and class 0 values. There are total of 3 instances which are not classified properly. This may be due to we didn’t have enough data to 
	   represent those instances in training sample. 
	4. ‘test2’ file clearly doesn’t have linearly separable data i.e. the predicted class doesn’t depend on given attribute. This can be due 
	   to there is no specific relationship between the given attributes and predicted class or we need extra attributes(non-linear) which also 
	   affect class prediction.
