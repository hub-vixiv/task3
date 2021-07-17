import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(filename, word, filepath):
    # 検索対象取得
    df=pd.read_csv("./" + filename)
    source = list(df["name"])

    # 検索
    if word in source:
        print("yes")
        print("『{}』はあります".format(word))
        # return "『{}』はあります".format(word)
        return f"『{word}』はあります。"

    else:
        print("no")
        # 追加
        # add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        # if add_flg=="1":
        # リストに保存するか確認ダイアログ表示
        source.append(word)
        print(source)
        df=pd.DataFrame(source,columns=["name"])
        # CSV書き込み
        df.to_csv(f"{filepath}/source.csv",encoding="utf_8-sig")

        return "『{}』はありません".format(word)