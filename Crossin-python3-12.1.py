import requests
while True:
    # 找成绩记录文件并提取数据
    try:
        with open('game_scores.txt','r+',encoding='utf-8') as f:
            raw_data = f.readlines()
    except:
        with open('game_scores.txt','w+',encoding='utf-8') as f:
            raw_data=f.readlines()
    # 建立dict，并提示即将开始game
    result={}
    for i in raw_data:
        a=i.split()
        result[a[0]]=a[1:]
    print(result)
    name=input('请输入你的名字：')
    record=[int(i) for i in result.get(name)]
    if not record:
        record=[0,0,0]
        avg=0.00
    else:
        avg=record[2] / record[0]
    print('%s，你已经玩了%s次，最少%s轮猜出答案，平均%.2f轮猜出答案，开始游戏！' % (name, record[0],record[1],avg))
    # game过程
    req=requests.get('https://python666.cn/cls/number/guess/')
    num_computer=int(req.text)
    print(num_computer)
    bingo=True
    rounds=0
    while bingo:
        try:
            num_player=int(input('请猜一个1-100的数字：'))
            rounds+=1
            if num_player > num_computer:
                print('猜大了，再试试')
            elif num_player < num_computer:
                print('猜小了，再试试')
            else:
                print('猜对了，你一共猜了%d轮' % rounds)
                bingo=False
                # 清算本轮游戏数据
                record[0]+=1
                record[2]+=rounds
                if record[1]==0:
                    record[1]=rounds
                elif record[1]>=rounds:
                    record[1]=rounds
                rounds=0
                choice = input('是否继续游戏？（输入y继续，其他退出）')
                if choice == 'y':
                    bingo = True
                else:
                    print('退出游戏，欢迎下次再来！\n')
        except Exception as e:
            print(e)
            print('输入错误，请输入有效值')
    # 写入成绩
    record_str=[str(i) for i in record]
    result[name]=record_str
    li_result=[' '.join([i]+j) +'\n' for i, j in result.items()]
    print(li_result)
    with open('game_scores.txt','w',encoding='utf-8') as f:
        f.writelines(li_result)



















































