# -*- coding: utf-8 -*-
"""Hypothesis testing using utilmy.ipynb
Docs ::

    Original file is located at
        https://colab.research.google.com/drive/1yIucO552adP4DaWhKvokIYrTuytHLUcS
"""
import pandas as pd
import numpy as np
import utilmy.stats.hypothesis as test
import utilmy.stats.statistics as stats




### One sample test (parameter estimation)

"""# 1) Student's t-test (One sample)"""

np.random.seed(10)
Population = [np.random.randint(10, 100) for _ in range(1000)]
Sample = [np.random.randint(11, 99) for _ in range(25)]
Population_Mean = round(sum(Population)/len(Population))
Population_Mean

# To test whether sample has come from a population with mean 54
# H0: μ = 54 
# H1: μ != 54

ttest = test.hypothesis.tTest(Sample, mu = Population_Mean)
ttest.test_summary

# As p-value is < 5% Level of significance, we reject H0.
# The sample has not come from a population with mean 54.

"""#2) Mann Whitney Test"""

# create dataframe
# for 'Vegan', 1 stands for vegan food.
data = pd.DataFrame({'Vegan':[1,1,1,0,0,0,1,0,1,0,1,0],
                            'Stars':[5.0,2.5,1.5,3.5,4.75,3.0,4.0,3.0,3.0,2.75,1.0,1.0]})
data.head()

# Is there difference in ratings for vegan and non-vegan food?
# H0: No difference in the stars
# H0: There is a difference in stars

mw = test.nonparametric.MannWhitney(group=data.Vegan, y1=data.Stars)
mw.test_summary

# With a p-value > 0.05, we fail to reject the null hypothesis that there is no 
# difference in rating between vegan and non-vegan food.


### Test for checking goodness of fit

"""# 1) Chi-square Test"""

# Let's say we're testing whether a die is fair or not.
# H0: Die is fair
# H1: Die is unfair

np.random.seed(10)
die_roll = [np.random.randint(1, 7) for _ in range(100)]
observed = pd.Series(die_roll).value_counts()
observed

ch = test.gof.ChiSquareTest(observed)
ch.test_summary
# P-value = 0.2942 > 5% level of significance, we fail to reject H0. 
# We don't have enough statistical evidence that die is unfair.

### Test for comparing 2 or more means

"""# 1) ANOVA"""

# Time (in minutes) to solve a puzzle
# Grouped based on what beverage they drank before solving
coffee = [8,20,26,36,39,23,25,28,27,25]
coke = [25,26,27,29,25,23,22,27,29,21]
tea = [14,25,23,27,28,21,26,30,31,34]

# To test whether there is variation in solving time based on beverage intake
# H0: No variation in the solving time based on the beverages
# H1: Variation in the solving time based on the beverages

aov = test.aov.AnovaOneWay(coffee, tea, coke)
aov.test_summary

# As p-value > 0.05, we fail to reject H0
# No significant statistical evidence to prove variation in the three groups.


"""# 2) Mc Nemar Test"""

# create random sample data
data = [['Toyota', 'Toyota'] for i in range(55)] + \
       [['Toyota', 'Mitsubishi'] for i in range(5)] + \
       [['Mitsubishi', 'Toyota'] for i in range(15)] + \
       [['Mitsubishi', 'Mitsubishi'] for i in range(25)]
df = pd.DataFrame(data, columns = ['Before Ad Screening', 'After Ad Screening']) 

# create contingency table
data_crosstab = pd.crosstab(df['Before Ad Screening'],
                            df['After Ad Screening'],
                            margins=True, margins_name="Total")
data_crosstab

#P0 : The true proportion of customers who prefer Toyota before the ad screening
#P1 : The true proportion of customers who prefer Toyota after the ad screening
#To test:
#H0 : P1 = P2
#H1 : P1 != P2

m = test.contingency.McNemarTest([[25, 5], [15, 55]], continuity=True)
m.test_summary
# As p-value < 0.05, we reject H0. 
# True proportion of customers who prefer Toyota before and after the ad screening is not the same, at 5% significant level.

"""# 3) Friedman Test"""

group1 = [4, 6, 3, 4, 3, 2, 2, 7, 6, 5]
group2 = [5, 6, 8, 7, 7, 8, 4, 6, 4, 5]
group3 = [2, 4, 4, 3, 2, 2, 1, 4, 3, 2]

# Test whether the samples are same
# H0: Mean for each population is equal
# H1: Atleast one population mean is different

Friedman = test.nonparametric.FriedmanTest(group1, group2, group3, group = None)
Friedman.test_summary

# P-value < 5%. Reject H0
# Atleast one population mean is different.

"""# 4) Cochran's Q test"""

# three columns for 3 sessions
# 1 represents depression
# 0 represents no more depression

cases = np.array([[0, 0, 0],
                  [1, 0, 0],
                  [1, 1, 0],
                  [1, 1, 1]])
                      
count = np.array([ 6,  16, 4,  2])
data = np.repeat(cases, count, 0)
data[:,0]

#Is there a difference in depression cases over the 3 subsequent courses of therapy
# H0: No difference in depression cases
# H1: Difference in depression cases

cq = test.contingency.CochranQ(data[:,0],data[:,1],data[:,2])
cq.test_summary

# p-value < 0.05. There is a statistical difference in the batches of patients 
# experiencing depression and no depression between the different number of sessions.

### Tests to determine if data distributions are similar or not

"""# 1) Kruskal Wallis Test"""

np.random.seed(10)
# generate three independent samples
data1 = 5 * np.random.randn(100) + 50
data2 = 5 * np.random.randn(100) + 50
data3 = 5 * np.random.randn(100) + 50

# To test: Whether the three distributions are similar or not 
# H0: All sample distribution are similar 
# H1: Atleast one pair of sample distributions is different

kw = test.nonparametric.KruskalWallis(data1, data2, data3)
kw.test_summary

# p-value > 5% level of significance. Thus, fail to reject H0
# No statistical evidence to prove that the sample distributions are different.

"""# 2) WaldWolfowitz"""

data1 = [20, 55, 29, 24, 75, 56, 31, 45]
data2 = [23, 8, 24, 15, 8, 6, 15, 15, 21, 23, 16, 15, 24, 15, 21, 15, 18, 14, 22, 15, 14]

# Test whether the samples are same
# H0: The two samples are same
# H1: The two samples are different

ww = test.nonparametric.WaldWolfowitz(x = data1, y = data2)
ww.test_summary

# P-value > 5%. Fail to Reject H0
# Data may be similar.

### test to determine normality of data
"""# 1) Shapiro - Wilk test for normality"""

weight = np.random.triangular(left = 40, right = 70, mode = 60, size = 1000)
roll = [i for i in range(1000)]
df = pd.DataFrame({
    "Movie": roll,
    "Weight": weight
    })

df.head()

# To test: Whether the marks are normally distributed.
# H0: Distribution is normally distributed.
# H1: Distribution is not normally distributed.

stats.test_normality2(df, "Weight", "Shapiro")

# p-value is 0, reject H0.
# The distribution of weight is not normal.