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
from box import Box

from utilmy import log


##################################################################################
def hypotest_is_all_means_equal(df, col=['col1', 'col2'], mean_target=4):
    """# To test whether All columns have same means.

    """    
    vlist = []
    if isinstance(df, pd.DataFrame):
        for coli in cols:
            vlist.append(df[coli].values)
    elif isinstance(df, list):
       vlist = df

    ddict = Box({})    

    log(""" ANOVA""")
    dd = test.aov.AnovaOneWay(*vlist)
    log(dd.test_summary)
    ddict.anova = aov.test_summary


    log(""" Friedman""")
    dd = test.nonparametric.FriedmanTest(*vlist, group = None)
    log(dd.test_summary)
    ddict.friedman = dd.test_summary


    log(""" Cochran's Q test """)
    dd = test.contingency.CochranQ(*vlist)
    log(dd.test_summary)
    ddict.cochran = dd.test_summary

    return ddict




def hypotest_is_equal_fixed_mean(df, col='mycol', mean_target=4):
    """# To test whether sample has come from a population with mean 54
    Docs::
        # H0: μ = 54 
        # H1: μ != 54

        ### One sample test (parameter estimation)
    np.random.seed(10)        
    Population = [np.random.randint(10, 100) for _ in range(1000)]
    Sample = [np.random.randint(11, 99) for _ in range(25)]
    Population_Mean = round(sum(Population)/len(Population))
    Population_Mean


    """    
    if isinstance(df, pd.DataFrame):
       samples = df[col].values
    else :
       samples = df 

    log("""# 1) Student's t-test (One sample)""")
    ttest = test.hypothesis.tTest(samples, mu = Population_Mean)
    print( ttest.test_summary)

    # As p-value is < 5% Level of significance, we reject H0.
    # The sample has not come from a population with mean 54.






def hypotest_is_all_group_means_equal(df, col=['col_group', 'val'], mean_target=4):
    """# To test whether All columns have same means.
    Docs::

        # Is there difference in ratings for vegan and non-vegan food?
        # H0: No difference in the stars
        # H0: There is a difference in stars
        # create dataframe
        # for 'Vegan', 1 stands for vegan food.
        data = pd.DataFrame({'Vegan':[1,1,1,0,0,0,1,0,1,0,1,0],
                                    'Stars':[5.0,2.5,1.5,3.5,4.75,3.0,4.0,3.0,3.0,2.75,1.0,1.0]})
        data.head()

        # With a p-value > 0.05, we fail to reject the null hypothesis that there is no 
        # difference in rating between vegan and non-vegan food.
    """    
    vlist = []
    if isinstance(df, pd.DataFrame):
        for coli in cols:
            vlist.append(df[coli].values)
    elif isinstance(df, list):
       vlist = df
    ddict = Box({})    

    log("""#2) Mann Whitney Test""")
    mw = test.nonparametric.MannWhitney(group=vlist[0], y1=vlist[1] )
    ddict.MannWhitney  = mw.test_summary
    return ddict








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