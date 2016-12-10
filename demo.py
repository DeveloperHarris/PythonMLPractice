from sklearn import tree

#training data
#[height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
	[166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40],
	[159, 55, 37], [171, 75, 42], [181,85,43]]

#classifications for training data
Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']


#creating the decision tree
clf = tree.DecisionTreeClassifier()
#training the tree
clf = clf.fit(X,Y)
#prediction using trained classifier and given inputs
prediction = clf.predict([[175, 73, 40]])

print(prediction)