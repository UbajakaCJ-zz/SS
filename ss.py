import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

	print('Loading data...')
	training = pd.read_excel('SS1.xlsx', header=0)
	testing = pd.read_excel('SS2.xlsx', header=0)

	# training.loc[training['GRADE'] == 'A1', 'GRADE'] = 1
	# training.loc[training['GRADE'] == 'B2', 'GRADE'] = 2
	# training.loc[training['GRADE'] == 'B3', 'GRADE'] = 3

	# testing.loc[testing['GRADE'] == 'A1', 'GRADE'] = 1
	# testing.loc[testing['GRADE'] == 'B2', 'GRADE'] = 2
	# testing.loc[testing['GRADE'] == 'B3', 'GRADE'] = 3


	train_x = training.drop(['SUBJECT', 'GRADE'], axis=1)
	train_y = training['GRADE']

	test_x = testing.drop(['SUBJECT', 'GRADE'], axis=1)
	test_y = testing['GRADE']

	test_sbj = testing['SUBJECT']


	model = DecisionTreeClassifier(min_samples_split=5)
	print('Training...')
	model.fit(train_x,train_y)

	print('Predicting...')

	pred = model.predict(test_x)

	accuracy = accuracy_score(pred, test_y)
	print 'Accuracy:', accuracy

	results_df = pd.DataFrame(data = {'GRADE': pred})
	joined = pd.DataFrame(test_sbj).join([testing['AVERAGE'], results_df])
	# joined.loc[joined['GRADE'] == 1, 'GRADE'] == 'A1'
	# joined.loc[joined['GRADE'] == 2, 'GRADE'] == 'B2'
	# joined.loc[joined['GRADE'] == 3, 'GRADE'] == 'B3'

	print 'Print results to predictions.csv'
	joined.to_csv('predictions.csv', index=False)






if __name__ == '__main__':
	main()