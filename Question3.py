# modify this function, and create other functions below as you wish
def question03(scores, alice):
    sortedUniqueScores = sorted(set(scores + [0]), reverse = True)   # Arranging the unique scores in descending order
    ranks = []
    for i in alice:
        for j in range(0, len(sortedUniqueScores)):
            if i >= sortedUniqueScores[j]:
                ranks.append(j+1)
                break
    
    answer = Counter(ranks).most_common()       #finding the mode
    return max(answer, key = lambda x: x[1])[0]     # returning the mode with the maximum value
