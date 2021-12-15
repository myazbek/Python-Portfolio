# -*- coding: utf-8 -*-
"""iris_species_predictor_decision_tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qOZSJOuj2Hebyy3a_Aon3qUzQlw9XaiT

#Mya's first super hot super cool machine learning algorithm! :)

Sources used to develop this can be explored in greater detail here:
* [Implementing Machine learning models on Iris Dataset.](https://https://medium.com/@harimittapalli/implementing-machine-learning-models-on-iris-dataset-a08e017dd3ee)
* [Visualizing Decision Trees with Python (Scikit-learn, Graphviz, Matplotlib)](https://towardsdatascience.com/visualizing-decision-trees-with-python-scikit-learn-graphviz-matplotlib-1c50b4aa68dc)
* [SciKit Learn Decision Trees](https://scikit-learn.org/stable/modules/tree.html)
* [Beautiful decision tree visualizations with dtreeviz](https://https://towardsdatascience.com/beautiful-decision-tree-visualizations-with-dtreeviz-af1a66c1c180)

Alright nerds lets get started

#Making Graphs

We will create a simple ML algorithm using the Iris dataset in seaborn to predict what class of iris a given instance is, when the user inputs an item such as a given iris's sepal and petal length/width
"""

#import your packages

import numpy as np
import pandas as pd
import seaborn as sns
import jupyter as jp
import matplotlib as mpl
import matplotlib.pyplot as plt
import sklearn as skl

#load the dataset

iris_data = sns.load_dataset("iris")


#prints the first 5 rows of the dataset
iris_data.head()

#describe the dataset

iris_data.describe()

#we have 150 observations in this dataset

#number of observations for each column

iris_data.count()

"""Great! We have our dataset. Now lets create some graphs to visualize our data. We will do this for each of our attributes (i.e. petal and sepal length/width). Let's mess around with a few different graphs we could make.  """

plt = sns.scatterplot( x = 'species', y = 'petal_length', hue='species', palette = 'spring_r', data=iris_data)
#plt.grid(True)

plt = sns.scatterplot( x = 'species', y = 'sepal_length', hue='species', palette = 'winter_r', data=iris_data)

#plt.style.use('ggplot')
#plt.grid(True)

#plt.style.use('ggplot')
#this makes our plots look a little nicer

petals = sns.relplot(x = 'petal_length', y = 'petal_width', col = 'species', hue = 'species', palette = 'cubehelix', data = iris_data)

#plt.suptitle('Petal Length x Petal Width by species', fontsize=10)
#adds an all encompassing title

sepals = sns.relplot(x = 'sepal_length', y = 'sepal_width', col='species', hue = 'species', palette = 'inferno', data = iris_data);
#plt.style.use('ggplot')
plt.grid(True);
print(sepals);
#other palettes I want to try: 
#cube, helix icefire, inferno, jet, magma, flare, Spectral, cividis, etc

"""Okay, let's make one final graph that plots petal length x petal width and has all three species in one grid. 

"""

petal_sepal = sns.scatterplot(x = 'petal_length', y ='petal_width', hue ='species', palette = 'pastel', data = iris_data);
plt.title("Petal length x Petal width for three species of Iris");
petal_sepal.set(xlabel = 'Petal Length cm', ylabel = 'Petal Width cm');

"""Cool! So we made some graphs and visualized our data. Lets build an easy decision tree.

#Creating our Decision tree
"""

#first we need to import all our shit again just in case it didn't carry over
#import your packages

import numpy as np
import pandas as pd
import seaborn as sns
import jupyter as jp
import matplotlib as mpl
import matplotlib.pyplot as plt
import sklearn as skl

#load the dataset

iris_data = sns.load_dataset('iris')

"""As a refresher, lets look at some metadata (information about our dataset). We will look at things like how many records our dataset has, what type of data we are working with (i.e. strings, intergers, floats, boolean), etc. """

iris_data.info() 

#tells us columns, their respective interger index, 
#whether they have any null values, and what data type is contained by that column.

iris_data.head()

"""To make our data easier to work with, we will transform our dataset into a pandas Data Frame. """

iris_df = pd.DataFrame(iris_data)
#creating a pandas DataFrame for easy indexing

iris_df.head()

"""Great! We successfully made our data a dataframe. We can see that the iris_data head and iris_df head produce the same results. """

#below is a quick example in indexing your dataframe

iris_df.iloc[1, :]

#gives us the second observation, because numeric indexing in python begins with 0 (see table above)

#.iloc[#row splicing, #column splicing]
#so .iloc[1, :] gives us the second row, and the : means we wants ALL columns
#associated with that row. If you only want the first two columns (sepal length and sepal width)
#for the second observation, you would use
#iris_df.iloc[1, 0:2]

iris_df.iloc[1, 0:2]
#you would use 0:2 and NOT 0:1 because Python thinks
#you want to stop before the 2nd position, which would be the third column.
#keep this in mind!
#you can check both of these .iloc examples in the 
#iris_df header to verify the output.

"""So now we need gather observations to train our model on. We want to divide our full dataset into a training and testing set. Since we have 150 obersevations, with 50 each being from our 3 species of iris, we should use about 20% of our total observations per species. This comes out to about 10 observations. I want to select observations at random, incase they are sorted in some way. We can use the randint function to randomly select observations.

Let's try to get python to display the full dataset so we can see how we need to index our
"""

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#print(iris_df)
#the above comment will print all 150 observations of the dataframe. 
#remove the # symbol in front of the print statement to view the dataframe.

"""Great! We can see the full dataset now. 0-49 are the positions for the setosa iris. 50-99 we have versicolor. 100-149 is our virginica species.

Okay great, we've got splicing and indexing down. Lets create 3 test sets that contain 10 randomly chosen intergers that correlate with the 3 species observed in our data. The three species are: 

*   setosa
*   versicolor
*   virginica
"""

#before we move on!!! We must add a target column to our dataframe! This is need for our decision tree. 
#we will also add a name column to add the unique identifier

iris_df.insert(5, 'target', 0)

#lets check to make sure our target column was added at the end of our dataframe

iris_df.head()

#inserting the numeric index as a column

#num_index = pd.Series(index = iris_df) 

iris_df['num_index'] = np.arange(iris_df.shape[0])

#iris_df.drop(['(0, num_index)'], axis=1)

iris_df.head()

"""We can now use the train_test_split function that sklearn has built in"""

from sklearn.model_selection import train_test_split


dt_train, dt_test =train_test_split(iris_df,test_size=0.2)

"""We will use 20% of our data to train our decision tree, as exhibited above. We can check the size of our respective training and testing datasets below"""

dt_train.shape, dt_test.shape

"""We now need to split the training and testing datasets into input and output datasets. Our input will be the sepal length/width, as well as the petal length/width. Our ouput will be the species. """

dt_train_x = dt_train[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

dt_train_y = dt_train['species']

dt_test_x = dt_test[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

dt_test_y = dt_test['species']

"""Great! We now have everything needed to train our decision tree. Let's give it a go!"""

species_id_tree = DecisionTreeClassifier()

#an empty decision tree

species_id_tree.fit(dt_train_x, dt_train_y)

"""Cool! Our tree has been trained using our training datasets. It knows that it will recieve an input of numeric values, and it wants an output of species."""

species_id = species_id_tree.predict(dt_test_x)

#we can now calculate the accuracy of these predictions

species_id_accuracy = skl.metrics.accuracy_score(species_id,dt_test_y)

print("Decision tree species prediction accuracy =", species_id_accuracy)

"""Our decision tree correclty predicited most of the input observations. Let's take a look at all of the info we fed it and it's predictions. """

final_df = pd.concat([dt_test_x, dt_test_y], axis=1)

final_df

#final_df.insert(column='predicted_species', value=species_id_ser, loc=5)

final_df['predicted_species'] = species_id

"""Okay now that we've joined our test input, test output, and decision tree results, lets take a look at it all together!"""

final_df

"""We can print a dataframe with only the wrongly identified values to see which ones were not accurately identified"""

incorrect_id = final_df.loc[dt_test['species'] != species_id]

incorrect_id

"""Great! We made our first decision tree! In the next section we will visualize our machine learning algorithm to get a better grasp on what just happened. 

"""



"""#Visualizing our Decision Tree"""

from matplotlib import pyplot as plt

tree_diagram = tree.plot_tree(species_id_tree);

plt.figure(figsize=(60,60));

#the ; at the end removes all the text. 
#try running the code without it to see what i mean

fn=['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']
cn=['setosa', 'versicolor', 'virginica']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (15,15), dpi=90)
tree.plot_tree(species_id_tree,
               feature_names = fn, 
               class_names=cn,
               filled = True); #filled = true indicates we want a color coded class.

"""Some things to note about the above tree:
gini index is an impurity measure that "calculates the amount of probability of a specific feature that is classified incorrectly when selected randomly" 
[source](https://https://medium.com/analytics-steps/understanding-the-gini-index-and-information-gain-in-decision-trees-ab4720518ba8)

Let's look at some other ways to visualize decision trees!
"""

from sklearn.datasets import *
from dtreeviz.trees import *
from IPython.display import Image, display_svg, SVG
import graphviz
import pandas as pd
import numpy as np

#below line installs packages in google collab
"""
import sys

if 'google.colab' in sys.modules:
  !pip install -q dtreeviz
"""

"""Below is a shorter way to train a decision tree, and then make a tree visualization using dtreeviz"""

iris_dt = tree.DecisionTreeClassifier(max_depth=2)  
iris = load_iris()

X_train = iris.data
y_train = iris.target
iris_dt.fit(X_train, y_train)

fn=['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']
cn=['setosa', 'versicolor', 'virginica']

tree_diagram2 = dtreeviz(iris_dt, 
               X_train, 
               y_train,
               target_name='species',
               feature_names= fn, 
               class_names= cn, 
               histtype= 'barstacked',  # barstackes is default
               orientation = 'LR');  # LR = left to right orientation
tree_diagram2