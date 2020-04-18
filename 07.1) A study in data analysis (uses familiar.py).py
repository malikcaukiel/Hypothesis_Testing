import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

#1 import familiar

#2 Lifespans of Vein Pack users
vein_pack_lifespans = familiar.lifespans('vein')
print(vein_pack_lifespans)
############################

#3,4. We’d like to find out if the average lifespan of a Vein Pack subscriber is significantly different from the average life expectancy of 71 years.
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
############################

#5 Let’s check if the results are significant!
print(vein_pack_test.pvalue)

############################

#6 If the test’s p-value is less than 0.05, print “The Vein Pack Is Proven To Make You Live Longer!”. Otherwise print “The Vein Pack Is Probably Good For You Somehow!”
if vein_pack_test.pvalue < 0.05:
    print("The Vein Pack is proven to Make You Live Longer!")
else:
    print("The Vein Pack is Probably Goof for You Somehow!")
############################

#7 In order to differentiate Familiar’s different product lines, we’d like to compare this lifespan data between our different packages.
artery_pack_lifespans = familiar.lifespans('artery')
print(artery_pack_lifespans)
############################

#8,9 2-Sample test!
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(package_comparison_results)
############################

# 10 If the p-value from our experiment is less than 0.05, the results are significant. 
if package_comparison_results.pvalue < 0.05:
    print("The Artery Package guarantees even stronger Results!")
else:
    print("The Artery Package is also a great Product!")
############################

# 11 Contingency table!
iron_contingency_table = familiar.iron_counts_for_package()
print(iron_contingency_table)
#############################

# 12, 13 Chi-Squared test. 
_,iron_pvalue,_,_ = chi2_contingency(iron_contingency_table)
#chi2, pval, dof, expected = chi2_contingency(iron_contingency_table)
#############################

#  14 pvalue is less than 0.05 or not
if iron_pvalue < 0.05:
    print("The Artery Package is Proven to Make You Healthier!")
else:
    print("While We Can't Say The Artery Package will Help You, I Bet It's Nice!")
#######################################################################################################










