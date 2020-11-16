import os
import queue

# ベースとなるパスとパスを入れておくリスト
basePath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Sample')
baseDir = os.listdir(path=basePath)
#検索対象のファイル
target = "ロース"
#キュー(キューにはpathを保存する)
que = queue.Queue()

# 最初に取得できるフォルダをスタックに保存する
for i in baseDir:
    path = basePath + '\\' + i
    que.put(path)

print('検索対象のファイル名：', target)


# フォルダ取得
def searchDir(path):
    try:
        # 子があるとき
        # 取得したフォルダ(複数)を
        matchDirs = os.listdir(path=path)
        for i in matchDirs:
            # キューにpathを入れる
            newPath = path + '\\' + i
            que.put(newPath)
    except:
        # 子がないとき
        return None


while not que.empty():
    targetPath = que.get()
    print('検索対象：', targetPath)

    if (targetPath.count(target) == 0):
        searchDir(targetPath)
    else:
        print("見つかりました")
        print("答え：", targetPath)
        break

if que.empty():
    print("見つかりませんでした")
