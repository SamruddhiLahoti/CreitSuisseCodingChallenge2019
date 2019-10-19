# modify this function, and create other functions below as you wish
def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    repaymentAmount = 0.1*initialLevelOfDebt
    newDebt = initialLevelOfDebt
    cnt = 0
    while newDebt >= 50:
        newDebt += (interestPercentage*newDebt)/100 - repaymentAmount
        cnt += 1
    answer = int(newDebt) + cnt*repaymentAmount + repaymentAmount
    return answer
