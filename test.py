###基本###

print("Hello World!")

print("海賊王に俺はなる")

print("モテたい")

# プログラム実行時、「cd [ディレクト名]」で実行場所を指定したのち、「python [ファイル名]」で実行。
# 1回打った命令は矢印キー（上下）で戻れる。
# 命令は上から順に実行される。





###演算###

print(1+1)
print(1-1)
print(2*2)
print(10/2)
print(5%3)  #あまりを出す





###変数###
# 複雑な文字列に対して使うことで、簡単にすることができる。

peach = "l_size"
login_id = "asiek2$0askls"
peach_length = 5
peach_times = 5.5

print(peach_times)

# 「[変数] = ["文字列"]」で箱を作ることができる。
# 変数名は、分かりやすいものを。Python上に既にある単語は指定不可。例えば、print, typeなど。


print(type(peach))
print(type(peach_length))
print(type(peach_times))

# 変数にはタイプあり。
# str   = 文字列/string
# int   = 整数/integer
# float = 不動小数点/floating point number


print(peach + peach_length)
print(peach_times + peach_length)

# 同じ型同士でないと結合不可。特にstr型とint,float型。


peach_tabetai = True

# TrueかFalseで条件分岐可。





###条件分岐###

if peach == "l_size":
    print("dekai!")

if peach == "s_size":
    print("dekai!")

# ==　：だったら


if peach != "l_size":
    print("dekai!")

if peach != "s_size":
    print("dekai!")

# !=　：でなければ


if peach_length < 3:
    print("sukunai")

if peach_length > 3:
    print("ooi")

# < , > , <= , >=


if peach_length > 3:
    print("ooi")
elif peach_length == 0:
    print("tabetyatta!")
else:
    print("sukunai")

# if ~:     ：条件1つ目
# elif ~:   ：条件2つ目
# else:　   ：それ以外


# 1行目で”比較”、コロン＆ネスト（Tabまたは半角スペース）した上で、2行目の作業を実行。





###関数###
# 命令のまとまり。同じ命令を使いまわすことができる。

def peach_taberu():
    peach_status = 5

    if (peach_status < 10):
        return "mada daijobu"
    else:
        return "onakasuita!"

print(peach_taberu())


def peach_taberu(arg):
    peach_status = arg

    if (peach_status < 10):
        return "mada daijobu"
    else:
        return "onakasuita"

print(peach_taberu(12))

# 引数(arg)を設定することで、毎度毎度そこの値のみ調整して使用することが可能に。





###リスト###
# リストは変数を複数持つことができる。

peach_list = ["peach_small", "peach_medium", "peach_large"]
print(peach_list[1])

# Pythonでは最初が0番目。





###for文"""
# ループ文で綺麗にまとめることができる。

for index in range(11):
    print(peach_taberu(5))
    print(index)
    print(peach_taberu(index))

# for [変数] in range([指定範囲])
# 数字には、index, i, countといった変数名をつけるのが一般的。


for item in peach_list:
    print(item)

# リスト内のものがループで入る。
# リストと組み合わせて使うときは、item変数が一般的。





###withとopen()###

with open("./peach.txt","r") as file:
    print(file.name)    #ファイル名
    print(file.mode)    #モード
    print(file.read())  #中身

# 開始から終了までの一連の流れをやってくれる。
# 基本は、自分で終了まで指示しなければならない。

# open関数において、
# 引数1つ目 = 読み込ませたいファイルのパス
# 引数2つ目 = モード

# モードについて
# "w"   = 書き足す
# "r"   = 読み込む





###class###
# class     = テンプレート。共通点のある機能を効率よく実装するために変数や関数をまとめて型にはめたもの。
# instance  = テンプレのクラスを元に出力したユニーク（固有）のもの。

class Card:
    def __init__(self, date, user_name):
        self.date = date
        self.user_name = user_name
    def message(self):
        return "この投稿は" + self.user_name + "さんが" + self.date + "に投稿しました"

date_a = "2020-01-01"
user_name_a = "Taro"
card_a = Card(date_a, user_name_a)
# card_a = Card("2020-01-01", "Taro")でもOK。

date_b = "2020-01-03"
user_name_b = "Hanako"
card_b = Card(date_b, user_name_b)

print(card_b.date)
print(card_b.user_name)
print(card_b.message())

# クラス名は、大文字スタート。

# コンストラクタ（__init__）= 初期化のような意味。インスタンス生成時だけ呼ばれる特殊な関数。
# self（引数）  = インスタンスが入る。勝手に入るので、設定不要。

# 独立していない、クラス内で使用されるものは特殊な言い方がある。
# プロパティ    ：クラスの中で定義されている変数。
# メソッド      ：クラスの中で定義されている関数。





###インポート###
# モジュール　：変数・関数・クラスなどを汎用的に使えるようまとめたコード群。
# 使いたい変数などがあれば、モジュールをimportするだけで使える。
# mathモジュール内にpiという変数がある。これを使える。


# デフォルトのモジュール　：import [モジュール名]
import math
print(math.pi)


# 外部のモジュール（NumPy, Pandas, Flask, Djangoなど）
import numpy

numpy_list = [3, 1, 5, 10, 2093, 304, 123]
numpy.sum(numpy_list)

# google　→Pypi（公開しているPythonのモジュール）　→コマンドをコピペ(例「pip install numpy])
# pipは、インストールしたりダウンロードしたりアップデートしたりできる。