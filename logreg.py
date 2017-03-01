#logreg.py
#Author: Vinay More
import sys
import matplotlib.pyplot as plotter
import matplotlib.patches as pat
import numpy as nm
import random as r
import math

def gethx(list,w):
    """gethx function calculate h(x) factor which is used for updating weights."""
    result = (float(list[0])*float(w[0]))+(float(list[1])*float(w[1]))
    result = 1.0 + math.exp(1) **(-1.0 * result)
    result = 1.0 / result
    return result

def updateWeights(list,weights):
    """updateWeights function updates the weight."""
    hx=gethx(list,weights)
    for j in range(2):
        weights[j]=float(weights[j])+(0.06*(float(list[2])-float(hx))*(1.0-float(hx))*float(list[j]))
    return weights

def squaredError(list,w):
    """squaredError function calculates squared error difference."""
    return (float(list[2])-gethx(list,w))*(float(list[2])-gethx(list,w))

def plotterFunction(finalX,finalY,minX,maxX,minY,maxY):
    """Initializing and then plotting points and decision boundary."""
    plotter.xlabel('x values')
    plotter.ylabel('y values')
    finalX=nm.asarray(finalX,dtype=float)
    finalY=nm.asarray(finalY,dtype=float)
    fit = nm.polyfit(finalX,finalY, 1)
    p = nm.poly1d(fit)
    plotter.axis([minX-2, maxX+2, minY-2, maxY+2])
    xp = nm.linspace(minX-2,maxX+2)
    red = pat.Patch(color='red', label='Class 1')
    blue = pat.Patch(color='blue', label='Class 0')
    plotter.legend(handles=[red,blue])
    plotter.plot(xp, p(xp), label='Linear Separator')
    plotter.show()
    return

#Main program
def main():
    """main function """
    if len(sys.argv) != 2:
        print('Usage: python logreg.py samplefile')
        return
    else:
        #reading sample training file
        list = []
        with open(sys.argv[1]) as file:
            for line in file:
                sublist = []
                str=line.split(",")
                for j in range(0,3):
                    sublist.append(str[j])
                list.append(sublist)

        #Initializing weights
        weights=[]
        weights.append(r.random())
        weights.append(r.random())

        #initializing weights.csv file before writing
        f=open("weights.csv","w")
        sys_org=sys.stdout
        sys.stdout=f

        #plotting squared error difference and adding weight values in weights.csv
        plotter.figure("Epoc vs Sum of squared error")
        plotter.xlabel('Number of Epocs')
        plotter.ylabel('Sum of squared error')
        sumSquare=[]
        for i in range(1000):
            sum=0.0
            for i in range(len(list)):
                weights=updateWeights(list[i],weights)
                print(weights[0],",",weights[1])
                sum=sum+squaredError(list[i],weights)
            sumSquare.append(sum)
        f.close()
        sys.stdout=sys_org
        #print(sumSquare)
        plotter.plot(sumSquare)
        plotter.show()

        #Intializing counters to count correct and incorrect class predictions
        correctCount0=0;
        incorrectCount0=0;
        correctCount1=0;
        incorrectCount1=0;

        #Initialzing minimum and maximum values of x and y for better plotting
        minX=sys.float_info.max
        maxX=sys.float_info.min
        minY=sys.float_info.max
        maxY=sys.float_info.min

        #Initializing lists
        finalX=[]
        finalY=[]

        plotter.figure("Decision boundary")
        with open("test1.csv") as ofile:
            for l in ofile:
                #print("Instance:",l,end="")
                olist=l.split(",")

                #Identifying minimum and maximum values of x and y for better plotting
                if(float(olist[0])>maxX):
                    maxX=float(olist[0])
                if (float(olist[0])<minX):
                    minX=float(olist[0])
                if(float(olist[1])>maxY):
                    maxY=float(olist[1])
                if (float(olist[1])<minY):
                    minY=float(olist[1])

                #Adding x and y values from test.csv in different lists for plotting
                finalX.append(olist[0])
                finalY.append(olist[1])

                #Tagging sample instances with their class
                if(gethx(olist,weights)>=0.5):
                    plotter.plot(olist[0],olist[1],"ro")
                    #print("Actual class",olist[2],"Predicted class",1)
                    if(int(olist[2])==1):
                        correctCount1=correctCount1+1
                    else:
                        incorrectCount1=incorrectCount1+1
                else:
                    plotter.plot(olist[0],olist[1],"bo")
                    #print("Actual class",olist[2],"Predicted class",0)
                    if(int(olist[2])==0):
                        correctCount0=correctCount0+1
                    else:
                        incorrectCount0=incorrectCount0+1

            print("Class 0 - Correctly identified instances",correctCount0)
            print("Class 0 - Incorrectly identified instances",incorrectCount0)
            print("Class 1 - Correctly identified instances",correctCount1)
            print("Class 1 - Incorrectly identified instances",incorrectCount1)

            #Plotting x and y values from test.csv with colors describing the class
            plotterFunction(finalX,finalY,minX,maxX,minY,maxY)

main()