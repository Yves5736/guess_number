import pathlib
import re

def play(name,cishu,min_round,sum_round,pj):
    s = 'y'
    while s == 'y':
        cishu += 1
        import requests
        url = 'https://python666.cn/cls/number/guess/'
        r = requests.get(url) #获得数字
        num = int(r.text)
        guess_0 = input('请猜一个1 - 100的整数：')
        try:
            guess = int(guess_0)
        except:
            go = False
            while go == False:
                guess_0 = input('输入有误，请重新输入：')
                try:
                    guess = int(guess_0)
                    go = True
                except:
                    go == False
        
        times = 1
        while guess != num:
            if guess > num:
                print('猜大了，再试试')
                guess = int(input('请猜一个1 - 100的数字：'))
                times += 1
            elif guess < num:
                print('猜小了，再试试')
                guess = int(input('请猜一个1 - 100的数字：'))
                times += 1
        if min_round > times:
            min_round = times
        pj = (pj * (cishu - 1) + times)/cishu
        sum_round += times
        print ('猜对了，你一共猜了%d轮'%times)
        print ('%s，你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案'%(name,cishu,min_round,pj))    
        s = input('是否继续游戏？（输入y继续，其他退出）')
    print('退出游戏，欢迎下次再来！')
    return(name, cishu, min_round, sum_round, pj)

name = input('请输入你的名字：')
while ' ' in name or name == '':
    name = input('输入有误，请重新输入：')

#如果没有文件就创建一个
try:
    f = open(r'/Users/apple/OneDrive - 洁云网络E3/python/小练习/猜数字/game_many_user.txt', encoding='utf-8')
except:
    file_name =r'/Users/apple/OneDrive - 洁云网络E3/python/小练习/猜数字/game_many_user.txt'
    pathlib.Path(file_name).touch()
    f = open(r'/Users/apple/OneDrive - 洁云网络E3/python/小练习/猜数字/game_many_user.txt', encoding='utf-8')

lines = f.readlines()
f.close()
dic_a = {}
for i in lines:
    data = i.strip(' ').split()
    dic_a[data[0]] = data[1:]
    
record = dic_a.get(name)

if record == None:
    record = ['0','10000','0']
    print('%s，你已经玩了0次，最少0轮猜出答案，平均0.00轮猜出答案，开始游戏!'%(name))
    sum_round = 0
    min_round = 10000
    cishu = 0
    pj = 0
else:
    sum_round = int(record[2])
    min_round = int(record[1])
    cishu = int(record[0])
    pj = sum_round/cishu
    print('%s，你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案，开始游戏!'%(name,int(record[0]),int(record[1]),pj))

name, cishu, min_round, sum_round, pj = play(name,cishu,min_round,sum_round,pj)

record_2 = [str(cishu),str(min_round),str(sum_round)]
dic_a[name] = record_2

output = ''
for j in dic_a:
    output_2 = j + ' ' +  ' '.join(dic_a[j]) + '\n'
    output += output_2

#在原文件中记录结果
f = open(r'/Users/apple/OneDrive - 洁云网络E3/python/小练习/猜数字/game_many_user.txt','w',encoding='utf-8')
f.write(output)
f.close()