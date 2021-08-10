file = open('group_scores.txt')


pass_count = 0
#for score in file :
#   score_int=int(score)
#    if score_int >= 50:
#        pass_count+=1

for group_scores in file : # group_scores - str แต่ละบรรทัด
    g_scores_list = group_scores.split(' ') # group_scores - n1 n2 n3...
    for score in g_scores_list:
        score_int = int(score)
        if score_int >= 50:
           pass_count+=1
print('Students pass : '+ str(pass_count))


file.close()