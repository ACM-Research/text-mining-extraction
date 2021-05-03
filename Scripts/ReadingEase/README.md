## Overview
<p>The scripts folder contains Python scripts that generate Reading Ease scores for a given set of .txt files.</p> 

<p>The graphing folder contains a script that generates a box-plot of the reading scores of all the datasets used in this research process. It also contains a script that generates bar graphs comparing the reading ease scores of different demographics.</p>

## Directory Overview

    ├── graphing	# sub-folder containing Python scripts that generate graphs
		├── cross-referencing	# sub-folder containing Python scripts that generate graphs by demographic
		├── data.csv	# CSV file containing reading ease scores and grade level scores for all datasets
		├── reGraph.py	# Python script that generates a box plot of all reading ease scores

    ├── script	# sub-folder contining scripts that generate reading ease scores for a given dataset
		├── entertainment-articles	# sub-folder containing .txt files of BBC articles of the entertainment genre from 2004-2005
		├── modern-texts	# sub-folder containing .txt files of modern novels
		├── politics-articles	# sub-folder containing .txt files of BBC articles of the politics genre from 2004-2005
		├── texts	# sub-folder containing .txt files from the primary dataset, Documenting the American South
		├── function.py	# Python function that calculates reading ease scores
		├── parse.py	# Driver code

    └── README.md # You are viewing this right now

## Libraries Used
- [textstat](https://github.com/shivam5992/textstat)
- [seaborn](https://seaborn.pydata.org/index.html)
- [matplotlib](https://matplotlib.org/stable/contents.html)

## Datasets Used

- [First-Person Narratives of the American South](https://docsouth.unc.edu/fpn/)
- [Project Gutenberg](https://www.gutenberg.org/)
- [BBC News Collection](https://www.kaggle.com/pariza/bbc-news-summary)
