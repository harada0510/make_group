#coding:utf-8
GREEN = '\033[92m'
ENDC = '\033[0m'

import random

# メンバーリスト（配列）の作成
a = open("members.txt","r")
members = []
for i in a:
    members.append(i.rstrip())
a.close()
random.shuffle(members)

while (True):
    try:
        splitNum = int(input("how many groups you want?: "))
    except ValueError:
        print ("the input contains characters not only number. try again...")
        continue
    if splitNum <= len(members):
        break
    else:
        print ("the split number is more than members. try again...")
        continue



#グループ分けを行う
gnum = 0
gnum_member = {}

for psn in members:
    gnum += 1
    gnum_member.setdefault(gnum, []).append(psn)
    if gnum >= splitNum:
        gnum = 0

for psn in gnum_member:
    print(GREEN, psn, ENDC, gnum_member[psn])
