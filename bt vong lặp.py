#bài tập viết số hoàn hảo từ 1-1000
for number in range(1,1001,1):
    s=0
    for i in range(1,number,1):
        if number%i==0:
            s=s+i
    if s==number:
            print(s)