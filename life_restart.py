import random
import sys
import time


print('+------------------------------------+')
print('|                                    |')
print('|       花有重开日,人无再少年           |')
print('|                                    |')
print('|      欢迎来到,人生重开模拟器          |')
print('|                                    |')
print('+------------------------------------+')


# 设置初始属性，颜值，家境，体质，智商
# 每一个属性取值1~10，总和不能超过20
# 使用循环在玩家输入错误时可以重新输入
while True:
    print('请设置初始属性(可用点数总数为20)')
    face = int(input('请输入颜值(1-10): '))
    home = int(input('请输入家境(1-10): '))
    strong = int(input('请输入体质(1-10): '))
    iq = int(input('请输入智商(1-10): '))

    # 通过条件语句来纠正用户输入错误的情况
    if face < 1 or face > 10:
        print('颜值设置有误')
        continue
    if home < 1 or home > 10:
        print('家境设置有误')
        continue
    if strong < 1 or strong > 10:
        print('体质设置有误')
        continue
    if iq < 1 or iq > 10:
        print('智商设置有误')
        continue
    if face + home + strong + iq > 20:
        print('总属性超过20，设置有误')
        continue

    # 玩家操作合法时跳出循环
    print('初始属性设置成功！')
    print(f'颜值={face},家境={home},体质={strong},智商={iq}')
    break


# 生成角色性别
# 使用random.randint(beg,end),就能生成[beg,end]随机整数
point = random.randint(1, 10)
if point % 2 == 1:
    gender = 'boy'
    print('你是个男孩')
else:
    gender = 'girl'
    print('你是个女孩')


# 生成随机数，根据家境对所选的属性增删
point = random.randint(1, 3)
if home == 10:
    # 第一档
    print('你出生在帝都，父母是高官富商')
    home += 1
    face += 1
    iq += 1
elif 7 <= home <= 9:
    # 第二档
    if point == 1:
        print('你出生在大城市，你的父母是公务员')
        face += 2
    if point == 2:
        print('你出生在大城市，你的父母是企业高管')
        home += 2
    if point == 3:
        print('你出生在大城市，你的父母是大学教授')
        iq += 2
elif 4 <= home <= 6:
    # 第三档
    if point == 1:
        print('你出生在三线城市，你的父母是医生')
        strong += 1
    if point == 2:
        print('你出生在镇上，你的父母是老师')
        iq += 1
    if point == 3:
        print('你出生在镇上，你的父母是个体户')
        home += 1
else:
    # 第四档
    if point == 1:
        print('你出生在农村，父母是勤劳的农民')
        strong += 1
        face -= 2
    if point == 2:
        print('你出生在穷乡僻壤，父母是无业游民')
        home -= 1
    if point == 3:
        print('你出生在镇上，父母感情不和')
        strong -= 1


print(f'当前属性：颜值={face},体质={strong},家境={home},智商={iq}')


# 将模拟的人生分为几个阶段
# 幼年阶段[1-10]
# 青年阶段[11-20]
# 壮年阶段[21-50]
# 老年阶段[51+]

def clamp(value, min_value=0, max_value=15):
    return max(min_value, min(max_value, value))


def die(reason, age):
    print(f'\n{age}岁：{reason}')
    print('你的人生到此为止，模拟结束。')
    print(f'最终属性：颜值={face},体质={strong},家境={home},智商={iq}')
    sys.exit(0)


for age in range(1, 101):
    point = random.randint(1, 100)

    if 1 <= age <= 10:
        stage = '幼年'
        if point <= 25:
            event = '你爱上了读书，智商+1'
            iq += 1
        elif point <= 45:
            event = '你经常户外玩耍，体质+1'
            strong += 1
        elif point <= 60:
            event = '你挑食导致营养不良，体质-1'
            strong -= 1
        elif point <= 75:
            event = '家里添置了新房，家境+1'
            home += 1
        elif point <= 90:
            event = '一次高烧影响发育，智商-1'
            iq -= 1
        else:
            die('你因先天重疾不幸夭折。', age)
    elif 11 <= age <= 20:
        stage = '青年'
        if point <= 20:
            event = '你学习刻苦，考上重点学校，智商+1'
            iq += 1
        elif point <= 35:
            event = '你迷上健身，体质+1'
            strong += 1
        elif point <= 50:
            event = '你学会打扮，颜值+1'
            face += 1
        elif point <= 65:
            event = '家庭投资获利，家境+1'
            home += 1
        elif point <= 80:
            event = '你沉迷游戏，智商-1，体质-1'
            iq -= 1
            strong -= 1
        elif point <= 95:
            event = '考试失利，信心受挫，颜值-1'
            face -= 1
        else:
            die('你在一次意外中失去生命。', age)
    elif 21 <= age <= 50:
        stage = '壮年'
        if point <= 18:
            event = '你事业晋升，家境+2'
            home += 2
        elif point <= 33:
            event = '你持续学习，智商+1'
            iq += 1
        elif point <= 48:
            event = '你规律作息，体质+1'
            strong += 1
        elif point <= 63:
            event = '你压力过大，体质-1'
            strong -= 1
        elif point <= 78:
            event = '你投资失败，家境-2'
            home -= 2
        elif point <= 92:
            event = '你婚姻幸福，颜值+1，家境+1'
            face += 1
            home += 1
        else:
            die('你因突发疾病抢救无效。', age)
    else:
        stage = '老年'
        if point <= 25:
            event = '你坚持锻炼，体质+1'
            strong += 1
        elif point <= 45:
            event = '你含饴弄孙，心态年轻，颜值+1'
            face += 1
        elif point <= 65:
            event = '你记忆力下降，智商-1'
            iq -= 1
        elif point <= 82:
            event = '你慢性病加重，体质-2'
            strong -= 2
        elif point <= 95:
            event = '你安享晚年，平稳度过一年'
        else:
            die('你寿终正寝，走完了完整的一生。', age)

    face = clamp(face)
    home = clamp(home)
    strong = clamp(strong)
    iq = clamp(iq)

    if strong <= 0:
        die('你身体状况过差，没能挺过这一年。', age)

    print(f'{age}岁[{stage}]：{event}')
    print(f'    属性：颜值={face},体质={strong},家境={home},智商={iq}')
    time.sleep(2)


print('\n你活到了100岁，堪称人生赢家！')
print(f'最终属性：颜值={face},体质={strong},家境={home},智商={iq}')
