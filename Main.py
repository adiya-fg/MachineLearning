from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
iris_dataset['data'], iris_dataset['target'], random_state=0)

print("X_train shape: {}".format(X_train.shape))
print("y_train shape: {}".format(y_train.shape))

 # create dataframe from data in X_train
 # label the columns using the strings in iris_dataset.feature_names
 iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
 # create a scatter matrix from the dataframe, color by y_train
 grr = pd.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
 hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)