# TerrorAnalyzer
### Introduction 
Terrorism is a terrible, but predictable phenomenon. Predicting Terrorism allows us to be prepared for it and to prevent it, and by attempting to predict it, we learn more about what causes terrorism, what doesn't, and what can be done about it. TerrorAnalyzer is my attempt at this, using linear regression and a collection of factors including past terrorism, human development, inequality, and civilian casualties. <br>


You input these factors for a certain country in a particular year (and previous years), and get a prediction on future deaths due to terrorism. <br>
Try it out [here](braingen.github.io/TerrorAnalyzer). It may take a minute to load.<br><br>
***Disclaimer**: This is a hobbyist project built to help me learn how to build regression models and clean data. I don't claim this model is accurate, on the contrary I say it is not. Furthermore, it is built on data that is, in spite of the best of attempts, not entirely complete. I'm not making a statement on human worth, and this model certainly shouldn't be used for real world decision making. All the data used to train the model is open source. This is an experimental project and data outputted from it should be treated with extreme caution. This model is not fit for real world usecases, and should NOT be used for any purpose other than experimentation and other mundane and harmless tasks.*


Factors used:<br>
nkilldelay1: Deaths due to terrorism from the previous year.<br>
nkilldelay2: Deaths due to terrorism from 2 years prior to the input year.<br>
deaths_civilians: number of civilian deaths perpetrated by the government and all non state actors operating in that country<br>

Other Factors Considered:<br>
value - Human Development Index value, used to measure impoverishment.<br>
inequality - thought it would increase the likelihood of terrorism.

### Reasoning

I used a scatterplot of my target variable (number of deaths due to terrorism this year) and the feature to decide whether a feature should be kept. If I saw a relationship on the graph , the factor was considered, if not, it was discarded.

Failures of this approach: Terrorism is a complex phenomenon. A factor may become important only in certain conditions, and it may have no predictive power in others. Plus, a graph can be misleading. If I build a next version, I'll use a different kind of model which can account for diverse interactions, and a framework such as hypothesis testing in order to rigorously evaluate and reject factors.

Why I used it: Time. A relationship is easy to spot on a graph, and some factors, such as civilian deaths and past terrorism, do directly correlate.

### Findings
Findings: Due to the uneven distribution of terrorism (the vast majority of attacks kill few people, while a few attacks kill many), all the factors I included in my analysis shared a power law relationship with my data. Hence, I had to apply a log-log transform, and exponentiate the predictions that came out of the model.

The model: A linear regression model was trained on the data. It achieved an R2 score of 0.7 on the logarithmic scale. On a real scale (graph), it seems to be bad at predicting massive outliers but good at predicting average values.

### Errors, Processes and Methods
Data Cleaning: This was my first time data cleaning. Naturally, I made mistakes, some of which I'm going to list below:
- I once allowed an AI to delete my code (I was *NOT* coding with it, just trying to undo a github issue)
- The last bits of data cleaning code are unreadable (and the first ones were too. I used method chaining at a point, to make it cleaner and more understandable)
- Cleaned all the data without checking for statistical relationship first (I have to look up how to do this). This wasted about six hours
- and many, many more.

Since I had to merge 3 datasets, I ensured that I used 2 consistent keys - country, and year. These were consistent in every dataset and made merging much easier.
For the global terrorism dataset, significant amount of cleaning was required for groupname values, a lot of columns not useful for me had to be removed, and many, many values had to be imputed in. Date Parsing took a *long* time , driven by multiple date formats. I also decided to filter some of the groups, so that the groups with 0 kills would not affect my analysis. I originally planned to include group names and create a groupwise interface, but I ran out of time, hence I chose to build the project country-wise. Groupby was probably what I struggled with the most, with merges taking a lot of time too. But I've gotten faster since I started, so I'll take this as a win. 

For the linear regression, I tried to use regularization. It made minimal impact, and some of the higher values aren't getting fit properly. I'm not entirely sure why. One possibility is time based train-test split (which was going to be needed anyway, given that this is an autoregressive model). 

By far the biggest error I've knowingly made is assuming that terrorism works the same way in all countries. Each country has its own culture, its own rebel groups, and its own story. Some terrorist organizations drive civil wars (such as in Mali) while others exploit already existing ones to dominate (such as ISIS). Some are contained through sheer force, while others are contained through social programs. Despite the non result of inequality and HDI, I'm still not convinced that discrimination plays *No* role in terrorism. I don't think I've found the right way to measure it yet. Perhaps discrimination is corelated with rebellion, and terrorism is one particularly brutal, particularly barbaric subset of that, which is much harder to predict. No simple model could account for all of these disparities. Hence, an architecture which can account for them (Decision Trees, perhaps?) would be more appropriate. 

So yes, this project is very much half baked. Thanks for reading through it anyway. 

## Setup
If you just want to try out the project, you can do so here without any setup: [terroranalyzer website](https://braingen.github.io/TerrorAnalyzer/). <br>
It may take a minute to load, so please have patience. <br>
Prerequisite: Python 3.11 onwards, Jupyter.<br>
Install dependancies:
`pip install -r requirements.txt`
### Local Setup
Navigate [here](model_app) and run python -m http.server 8000<br>
Then, open [localhost 8000](http://localhost:8000/)
It may take a minute to load.

### Model Training
Run [RegressionTraining.ipynb](Code/RegressionTraining.ipynb)<br>
The model will be generated as a .pkl file. Loading code is given in the last cell.
### Visualization of Statistical Relationship 
Run [Stats_Verification.ipynb](Code/Stats_Verification.ipynb)

### Data Cleaning
Create a folder named `Global Terrorism Dataset` and add the following datasets in it (important: Do not change the names):<br>
[Global Terrorism Database](https://www.kaggle.com/datasets/START-UMD/gtd)<br>
[UCDP One-Sided violence Dataset](https://ucdp.uu.se/downloads/#onesided)<br>
[Ethnic Power Relations Dataset](https://icr.ethz.ch/data/epr/core/2018.html)<br>
[World Cities Database](https://www.kaggle.com/datasets/max-mind/world-cities-database)
[HDI Data](https://hdr.undp.org/data-center/documentation-and-downloads)<br>

Note on HDI: Enter the following filters: HDI, Human Development Index (value) , Select All, (No filter on group, country etc). Download Excel and rename it as `hdr-data.xlsx`
Run [data_cleaning.ipynb](Code/data_cleaning.ipynb)

## PS
AI use was limited to tutoring only and was used once to generate a script for visualization. This readme was written entirely by me with no AI assistance.

## Citations: 
• Shawn Davies, Therése Pettersson, Magnus Öberg, Organized violence 1989–2025, and violent political protests, Journal of Peace Research, 2026. https://doi.org/10.1093/jopres/xjag046

• Eck, Kristine & Lisa Hultman (2007) Violence Against Civilians in War. Journal of Peace Research 44(2).

• UCDP is part of and funded by DEMSCORE, national research infrastructure grant 2021-00162 from the Swedish Research Council.

Vogt, Manuel, Nils-Christian Bormann, Seraina Rüegger, Lars-Erik Cederman, Philipp Hunziker, and Luc Girardin. 2015. “Integrating Data on Ethnicity, Geography, and Conflict: The Ethnic Power Relations Data Set Family.” Journal of Conflict Resolution 59(7): 1327–42.
