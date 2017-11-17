from numpy import *
import SVM
print "step 1: load data..."
dataSet = []
labels = []
fileIn = open('C:\\Users\\Administrator\\Desktop\\iris.txt')
for line in fileIn.readlines():
    lineArr = line.strip().split(',')
    # print lineArr[0],' ',lineArr[4]
    print type(lineArr[0])
    # dataSet.append(lineArr[0])
    dataSet.append([float(lineArr[0]), float(lineArr[1])])
    labels.append(float(lineArr[2]))
    # labels.append(lineArr[0])



dataSet = mat(dataSet)
labels = mat(labels).T
train_x = dataSet[0:81, :]
train_y = labels[0:81, :]
test_x = dataSet[80:101, :]
test_y = labels[80:101, :]

## step 2: training...
print "step 2: training..."
C = 0.6
toler = 0.001
maxIter = 50
svmClassifier = SVM.trainSVM(train_x, train_y, C, toler, maxIter, kernelOption=('linear', 0))

## step 3: testing
print "step 3: testing..."
accuracy = SVM.testSVM(svmClassifier, test_x, test_y)

## step 4: show the result
print "step 4: show the result..."
print 'The classify accuracy is: %.3f%%' % (accuracy * 100)
SVM.showSVM(svmClassifier)