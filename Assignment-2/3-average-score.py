
sum_score = 0 
count = 0
while (1):
    score = input("enter score : ")

    if(score == "exit"):
        print("avg-score = ",sum_score/count)
        break
    else:
        sum_score += float(score)
        count += 1