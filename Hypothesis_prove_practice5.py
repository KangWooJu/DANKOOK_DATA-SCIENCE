# 카이제곱 검정  

from scipy import stats 

men = [10,10]
women = [15,65]

# 카이제곱 검정 
stats.chi2_contingency([men,women])

## Statistic : 검정 통계량 
## pvalue : p - value 
## expected_freq : 기대 빈도 