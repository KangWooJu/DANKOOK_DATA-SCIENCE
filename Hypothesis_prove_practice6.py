# 피셔 정확 검정 

from scipy import stats 

Group_A = [7,3]
Group_B = [2,9]

# 기대빈도 
stats.chi2_contingency([Group_A,Group_B])[3]

# 피셔 정확 검정 
stats.fisher_exact([Group_A,Group_B])
