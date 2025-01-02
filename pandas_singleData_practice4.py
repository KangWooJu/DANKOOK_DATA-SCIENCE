import pandas as pd
import numpy as np

mydata = [60,62,64,65,68,69,120]
mydata = pd.Series(mydata)
mydata.quantile(0.25)
mydata.quantile(0.5)
mydata.quantile(0.75)
mydata.quantile([0.25,0.5,0.75])

mydata.quantile(np.arange(0,1,0.1))
mydata.describe()
