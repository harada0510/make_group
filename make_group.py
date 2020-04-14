#coding:utf-8
#色付け関係
GREEN = '\033[92m'
ENDC = '\033[0m'

#必要なモジュールのインポート
import random #ランダムシャッフルに必要なモジュール

# メンバーリスト（配列）の作成
#aという名前のオブジェクトとして下記のファイルを読み込む．
a = open("members.txt","r")
#メンバーリスト（配列）の定義
members = []
#１行１行上から読み込みます．iには各１行が都度入ってく
for i in a:
    #配列オブジェクト.append(追加したいオブジェクト)で配列の最後尾にオブジェクトを追加できる．
    #オブジェクト.rstrip()で改行文字(\n)を取り除く．
    members.append(i.rstrip())
#開いたファイルは閉じましょう．
a.close()

# 要素の順番を入れ替える（同じグループ数を入力されちゃうと毎回同じグループメンバーになるのを防ぐ．）
random.shuffle(members)

# ユーザにいくつのグループに分けるか入力させよう！
#while(条件式):で，条件式を満たす間内側の処理が繰り返し実行される．
while (True):
    #Try文を使うことでTryの中身でエラーになったとき，エラー内容を吐いてプログラムがその箇所で停止する代りにexceptの中身が実行される．（こういうのを例外処理と呼ぶ）
    try:
        #input("何かしらの文字列")でコマンドラインからの入力を行う．
        #int(オブジェクト)で入力された数値（str型）を数値（int型）に変換したものを返す．
        splitNum = int(input("how many groups you want?: "))
    except ValueError:
        print ("the input contains characters not only number. try again...")
        #whileのループの先頭に戻る
        continue
    #メンバーの人数よりも多くグループ分けはできない
    if splitNum <= len(members):
        #whileのループから脱出
        break
    else:
        print ("the split number is more than members. try again...")
        #whileのループの先頭に戻る
        continue



#グループ分けを行う
#今何ループ目なのかをはかるカウンタを定義
gnum = 0
#(グループ番号,メンバー）となる辞書型を定義
gnum_member = {}

#メンバーリスト（配列）で回す（psnには前から順番に一つ一つ要素が格納されてく）
for psn in members:
    #カウンタを更新
    gnum += 1
    #カウンタをkey, psnに格納されたメンバーをValuerとして辞書型に追加．
    #ここで，keyに対するvalueは一つしか定義できないのでvalueの型を配列にすることでkeyに対して複数のvalueを設定できる．
    gnum_member.setdefault(gnum, []).append(psn)
    #っでカウンタが入力された数以上になったらカウンタをリセットする．
    if gnum >= splitNum:
        gnum = 0

# 各グループメンバーの表示
#作成したgnum_memberで回す．
#psnには辞書型gnum_memberのkey（グループ番号）が都度格納される．
for psn in gnum_member:
    #色付けは[色]色付けしたい文字列[ENDC]でできる．
    #Valueの指定は辞書型[対応するkey]で行う．（例えばグループ"1"に振り分けられたメンバーを表示したいお場合は，gnum_member[1]）
    print(GREEN, psn, ENDC, gnum_member[psn])
