from pyspark.sql import SparkSession
header_text = "source,isTrueDirect,sourceKeyword,medium,isVideoAd,fullVisitorId,visitId,date,newVisits,hitReferer,hitType,hitAction_type,hitNumber,hitHour,hitMin,timeMicroSec,v2ProductName,productListName,isClick,isImpression,sessionQualityDim,timeOnScreen,timeOnSite,totalTransactionRevenue"
from pyspark.sql.types import *
attr_list = []
for each_attr in header_text.split(','):
    attr_list.append(StructField(each_attr, StringType(), True))
custom_schema = StructType(attr_list)


# coding: utf-8



#spark.stop()

spark = SparkSession     .builder     .appName("Funnel")     .master("yarn")     .config("spark.total.executor.cores","12")    .config("spark.executor.memory","1G")    .getOrCreate();
spark.sparkContext.setLogLevel("ERROR");
#raw_df = spark.read.format('csv').schema(custom_schema).option('header','true').option('mode','DROPMALFORMED').load('/user/rawzone/funnel/*')
raw_df = spark.read.format('csv').schema(custom_schema).option('header','true').option('mode','DROPMALFORMED').load('/user/rawzone/funnel-sqoop-toHDFS/*')
mem_raw_df = raw_df.repartition(60).cache()


mem_raw_df.columns

allCol_list = mem_raw_df.columns

removeCol_list = ['timeOnScreen']

for i in removeCol_list:
    allCol_list.remove(i)

newCol_list = []

newCol_list = allCol_list

filtered_raw_df = mem_raw_df.select(newCol_list)


# # 2. Data Preparation

# ## Data Cleansing: Remove missing values
from pyspark.sql.functions import udf
from pyspark.sql.types import *


# ### Remove Null
def f_removenull(origin):
    if origin == None:
        return 'NULL'
    else:
        return origin

removenull = udf(lambda x: f_removenull(x),StringType())


# ### Make Binary
def f_makebinary(origin):
    if origin == None:
        return 'FALSE'
    elif origin == 'true':
        return 'TRUE'
    elif origin == '1':
        return 'TRUE'
    else:
        return 'NULL'

makebinary = udf(lambda x: f_makebinary(x),StringType())



# ### Clean Null with Zero
def f_cleanNullwithZero(item):
    if item == None:
        new = '0'
        return new
    else:
        return item

cleanNullwithZero = udf(lambda x:f_cleanNullwithZero(x),StringType())


# ### Make Dollar
def f_makedollar(revenue):
    if revenue == None:
        return 0
    else:
        return revenue/1000000

makedollar = udf(lambda x: f_makedollar(x),FloatType())

from pyspark.sql.functions import col

#filtered_raw_df.describe().toPandas().transpose()

crunched_df = filtered_raw_df.withColumn('hitHour',col('hitHour').cast(FloatType())).withColumn('hitMin',col('hitMin').cast(FloatType())).withColumn('hitNumber',col('hitNumber').cast(FloatType())).withColumn('timeMicroSec',col('timeMicroSec').cast(FloatType())).withColumn('timeOnSite',col('timeOnSite').cast(FloatType())).withColumn('totalTransactionRevenue',cleanNullwithZero(col('totalTransactionRevenue')).cast(FloatType())).withColumn('newVisits',makebinary(col('newVisits'))).withColumn('sourceKeyword',removenull(col('sourceKeyword'))).withColumn('isVideoAd',makebinary(col('isVideoAd'))).withColumn('hitReferer',removenull(col('hitReferer'))).withColumn('isClick',makebinary(col('isClick'))).withColumn('isImpression',makebinary(col('isImpression'))).withColumn('sessionQualityDim',removenull(col('sessionQualityDim'))).withColumn('timeOnSite',removenull(col('timeOnSite'))).withColumn('totalTransactionRevenue',makedollar(col('totalTransactionRevenue'))).withColumn('isTrueDirect',makebinary(col('isTrueDirect')))

#crunched_df.describe().toPandas().transpose()

#crunched_df.filter(col('fullVisitorId') == '0131989137375171234').filter(col('visitId') == '1493252333').show()


# ### Summary within Partition
#importing libraries
#from sklearn.datasets import load_boston
#import pandas as pd
#import numpy as np
#import matplotlib
#import matplotlib.pyplot as plt
#import seaborn as sns
#import statsmodels.api as sm
#get_ipython().magic('matplotlib inline')
#from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LinearRegression
#from sklearn.feature_selection import RFE
#from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso

#from com.crealytics.spark.excel import *
from pyspark.sql.functions import col, udf, sum
from pyspark.sql.types import *
from pyspark.sql import Row
from pyspark.sql.window import Window

crunched_df

crunched_df.columns

import sys

from pyspark.sql.types import *

from pyspark.sql.functions import *

w = Window()   .partitionBy('fullVisitorId','visitId')   .orderBy(col("hitNumber").cast("long"))

windowSpec = Window.partitionBy('fullVisitorId','visitId').orderBy(col("hitNumber").cast("long")).rangeBetween(-sys.maxsize, sys.maxsize)

from pyspark.sql import functions as func

Diff_hitNumber = func.max(col('hitNumber').cast(IntegerType())).over(windowSpec) - func.min(col('hitNumber').cast(IntegerType())).over(windowSpec)

Diff_timeMicroSec = func.max(col('timeMicroSec').cast(IntegerType())).over(windowSpec) - func.min(col('timeMicroSec').cast(IntegerType())).over(windowSpec)

Diff_hitHour = func.max(col('hitHour').cast(IntegerType())).over(windowSpec) - func.min(col('hitHour').cast(IntegerType())).over(windowSpec)

Diff_hitMin = func.max(col('hitMin').cast(IntegerType())).over(windowSpec) - func.min(col('hitMin').cast(IntegerType())).over(windowSpec)

first_hitNumber = func.first(col('hitNumber').cast(IntegerType())).over(windowSpec)

last_hitNumber = func.last(col('hitNumber').cast(IntegerType())).over(windowSpec)

first_Action_type = func.first(col('hitAction_type').cast(StringType())).over(windowSpec)

last_Action_type = func.last(col('hitAction_type').cast(StringType())).over(windowSpec)

from pyspark.sql.functions import to_timestamp

partitionCal_df = crunched_df.withColumn('first_hitNumber', first_hitNumber).withColumn('last_hitNumber', last_hitNumber).withColumn('Diff_hitNumber', Diff_hitNumber).withColumn('Diff_timeMicroSec', Diff_timeMicroSec).withColumn('Diff_hitHour', Diff_hitHour).withColumn('Diff_hitMin', Diff_hitMin).withColumn('first_Action_type', first_Action_type).withColumn('last_Action_type', last_Action_type).dropna()

partitionCal_df.columns

partitionCal_df.columns

partitionCal_df.columns

def f_removeLastItem(list):
    list.pop()
    return list

removeLastItem = func.udf(lambda x:removeLastItem(x))

collectList_df = partitionCal_df.groupBy([
'source',
 ##'isTrueDirect',
 ##'sourceKeyword',
 ##'medium',
 'isVideoAd',
 'fullVisitorId',
 'visitId',
 #'date',
 ##'newVisits',
 ##'hitReferer',
 #'hitType',
 #'hitAction_type',
 #'hitNumber',
 #'hitHour',
 #'hitMin',
 #'timeMicroSec',
 #'v2ProductName',
 #'productListName',
 #'isClick',
 #'isImpression',
 ##'sessionQualityDim',
 #'timeOnSite',
 #'totalTransactionRevenue',
 'first_hitNumber',
 'last_hitNumber',
 'Diff_hitNumber',
 'Diff_timeMicroSec',
 'Diff_hitHour',
 'Diff_hitMin',
 'first_Action_type',
 'last_Action_type']).agg(func.collect_list('hitAction_type'))\
#.withColumn('collect_list(hitAction_type)',removeLastItem(col('collect_list(hitAction_type)')))
#raw_df.select(['fullVisitorId','visitId']).distinct().count()

#collectList_df.count()


# # EDA

# ##### The action type. Click through of product lists = 1, Product detail views = 2, Add product(s) to cart = 3, Remove product(s) from cart = 4, Check out = 5, Completed purchase = 6, Refund of purchase = 7, Checkout options = 8, Unknown = 0.


funnel_col_list = collectList_df.columns

funnel_col_list

raw_funnel_df = collectList_df.select(['fullVisitorId',
 'visitId',
 'first_hitNumber',
 'last_hitNumber',
 'Diff_hitNumber',
 'Diff_hitHour',
 'Diff_hitMin',
 'Diff_timeMicroSec',
 'first_Action_type',
 'last_Action_type',
 'collect_list(hitAction_type)'])




# ### Declare Functions for Removing Duplication and Last items in List
def f_removedupINLIST(l):
    seen = set()
    new_list = [x for x in l if not (x in seen or seen.add(x))]
    new_list.pop()
    return new_list

removedupINLIST = func.udf(lambda x: f_removedupINLIST(x))

raw_funnel_df.columns

f_length_list = func.udf(lambda x: len(x),IntegerType())

seq_funnel_df = raw_funnel_df.withColumn('seq_hitAction_type',removedupINLIST(col('collect_list(hitAction_type)'))).withColumn('length_hitAction_type',f_length_list(col('collect_list(hitAction_type)')))

seq_funnel_df.columns

seq_funnel_df


# ##### The action type. Click through of product lists = 1, Product detail views = 2, Add product(s) to cart = 3, Remove product(s) from cart = 4, Check out = 5, Completed purchase = 6, Refund of purchase = 7, Checkout options = 8, Unknown = 0.
seq_funnel_df.printSchema()

seq_funnel_df.count()

final_df = seq_funnel_df

#final_df.select(['fullVisitorId','visitId']).distinct().count()

#final_df.count()


# # 3. Data Modeling
import pyspark
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.ml.feature import OneHotEncoder, StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark.ml.feature import StringIndexer, VectorAssembler, OneHotEncoder,VectorIndexer, QuantileDiscretizer
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator
from pyspark.ml.evaluation import MulticlassClassificationEvaluator, BinaryClassificationEvaluator
from pyspark.ml.classification import LogisticRegression, GBTClassifier, NaiveBayes, RandomForestClassifier, DecisionTreeClassifier
from pyspark.ml import Pipeline
from pyspark.ml.clustering import *
from pyspark.ml.feature import Bucketizer

def get_evaluation(trainingSet,testingSet,algo,                   categoricalCols,continuousCols,discretedCols,split_range,labelCol):

    from pyspark.ml import Pipeline
    from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
    from pyspark.sql.functions import col
    
    
    labelIndexer = StringIndexer(inputCol=labelCol,                             outputCol='indexedLabel',                             handleInvalid='keep')

    indexers = [ StringIndexer(handleInvalid='keep',                               inputCol=c, outputCol="{0}_indexed".format(c))
                 for c in categoricalCols ]

    # default setting: dropLast=True
    encoders = [ OneHotEncoder(inputCol=indexer.getOutputCol(),
                 outputCol="{0}_encoded".format(indexer.getOutputCol()))
                 for indexer in indexers ]
    discretizers = [ Bucketizer(inputCol=d, outputCol="{0}_discretized".format(d)                 ,splits=split_range)
                 for d in discretedCols ]
    
    
    featureCols = ['features']
    assembler = VectorAssembler(inputCols=[encoder.getOutputCol() for encoder in encoders]
                                + continuousCols +\
                                [discretizer.getOutputCol() for discretizer in discretizers], \
                                outputCol='features')
    
    
    #var_name = algo
    ml_algorithm = algo(featuresCol='features',                                labelCol='indexedLabel')
    


    
    pipeline = Pipeline(stages=[labelIndexer] + indexers + encoders + discretizers +                         [assembler] + [ml_algorithm])
    
    

    model=pipeline.fit(trainingSet)
    result_df = model.transform(testingSet)
    evaluator_RF = MulticlassClassificationEvaluator(predictionCol="prediction",                                              labelCol='indexedLabel', metricName='accuracy')
    print(algo,'====>',evaluator_RF.evaluate(result_df)*100)

    return model

final_df.printSchema()

final_df.columns

catcols = ['first_Action_type',
           'seq_hitAction_type'
          ]

num_cols = ['first_hitNumber',
 'last_hitNumber',
 'Diff_hitNumber',
 'Diff_hitHour',
 'Diff_hitMin',
 'Diff_timeMicroSec',
            'length_hitAction_type'
           ]

discols = [           #'pub_rec',\
           #'seq_hitAction_type'\
          ]



labelCol = 'last_Action_type'

splits = [-1.0, 0.0, 10.0, 20.0, 30.0, 40.0, float("inf")]

selected_algo = [DecisionTreeClassifier, RandomForestClassifier, LogisticRegression]
#selected_algo = [LogisticRegression]

training_df, testing_df = final_df.randomSplit(weights = [0.80, 0.20], seed = 13)

for a in selected_algo:
    model = get_evaluation(training_df,testing_df,a,catcols,num_cols,discols, splits, labelCol)

testing_df.count()



model.write().overwrite().save('/user/refinedzone/model')