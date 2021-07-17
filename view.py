import eel
from pandas.core import series
import desktop
import search
import search2
import pandas as pd

app_name="html"
end_point="index.html"    #確認なし
# end_point="index2.html"     #確認ありバージョン（ポップアップ）
size=(700,600)


# 検索処理呼び出し
@ eel.expose
def kimetsu_search(filename, word, filepath):
    return search.kimetsu_search(filename, word, filepath)
    
    
@ eel.expose
def kimetsu_search2(filename, word):
    search2.kimetsu_search(filename, word)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)