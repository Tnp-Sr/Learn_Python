file_read = open('group_scores.txt')
file_write = open('test.txt','w') # ใส่ทื่อไฟล์ไม่มีได้ เด๋ยวคอมจัดการเอง

#file.write('Young Forever!\n')
#file.write('Now Together')

for group_scores in file_read :
    sum_score=0
    g_scores_list = group_scores.split(' ') # group_scores - n1 n2 n3...
    for score in g_scores_list:
        score_int = int(score)
        sum_score += score_int
        avg_score = sum_score/len(g_scores_list)
    file_write.write(str(avg_score)+'\n')


file_read.close()
file_write.close()