def rug (n):
    emoji = ['🎯','⚽','🟠','🥎','🏀','⚽','🥎','🔴','🏀','⚽','🟠','🥎','🏀','⚽','🥎','🔴','🏀']
    cnt=0
    x = int(n /2) 
    if n % 2 != 0:
        for i in range (0,n):
            for j in range (0,n):
                if (j >= cnt and j <n-cnt):
                    print(emoji[x-cnt],end=" ")
                elif ( j < cnt ):
                    print(emoji[x-j],end=" ")
                elif( j >= n-cnt):
                    print(emoji[x-(n-(j+1))],end=" ")
            print()
            if(i<int(n/2)):
                cnt += 1
            elif (i>=int(n/2)):
                cnt -= 1
    else:
        print("enter odd numbers not even ")
rug (int(input("enter n : ")))