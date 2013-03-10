from dataForNB import *

def evaluationMetrics(real, predicted):
  if len(real) != len(predicted):
    print "Length not equal"
    print len(real)
    print len(predicted)
    return
  else:
    truePositive = falseNegative = falsePositive = trueNegative = 0
    for i in range(len(real)):
      if real[i] == 1:
        if predicted[i] == 1:
          truePositive = truePositive + 1
        else:
          falseNegative = falseNegative + 1
      else:
        if predicted[i] == 1:
          falsePositive = falsePositive + 1
        else:
          trueNegative = trueNegative + 1
    recall = precision = f1 = -1.0
    print truePositive, falseNegative, falsePositive, trueNegative
    if (truePositive + falseNegative != 0):
      precision = truePositive / (0.0 + truePositive + falsePositive)
    if (truePositive + falseNegative != 0):
      recall = truePositive / (0.0 + truePositive + falseNegative)
    if (recall + precision != 0 and precision != -1 and recall != -1):
      f1 = 2.0 * (precision * recall) / (0.0 + recall + precision)    
    return [precision, recall, f1]
    
def getPredictedY(words, senses, predictor):
  all = []
  setOfIndicator = []
  setOfIndicator.append(rawXTesting[0][3])
  for i in range(1, len(rawXTesting)):
    if rawXTesting[i][3] != rawXTesting[i-1][3]:
      setOfIndicator.append(rawXTesting[i][3])
      
  print setOfIndicator
  for word in setOfIndicator:
    temp = []
    for j in range(len(rawXTesting)):
      if rawXTesting[j][3] == word:
        temp.append([word, senses[j], predictor[j], j])
    all.append(sorted(temp, key = lambda temp: temp[2], reverse = True))

  # Now we have the best disambiguation for each ambiguous link we detected
  for item in all:
    print "Word : " + str(item[0][0]) + " Label number: " + str(item[0][1]) +  " with probability: " + str(item[0][2]) + "This is sense # in total: " + str(item[0][3])

  # Evaluate the result
  
  # checkTable = [[raw[i][2], raw[i][3]] for i in range(len(raw)) if (rawYTesting[i] == 1)]
  predictedTrue = [elem[0][-1] for elem in all]
  predictedY = [1 if i in predictedTrue else 0 for i in range(len(rawYTesting))]
  
  print rawYTesting
  print predictedY
  
  return predictedY


