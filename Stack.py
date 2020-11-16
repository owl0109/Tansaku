import os

# ベースとなるパスとパスを入れておくリスト
basePath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Sample')
baseDir = os.listdir(path=basePath)
#検索対象のファイル
target = "あああ"
#スタック(スタックにはpathを保存する)
stack = []

# 最初に取得できるフォルダをスタックに保存する
for i in baseDir:
    path = basePath + '\\' + i
    stack.append(path)

print('検索対象のファイル名：', target)


# フォルダ取得
def searchDir(path):
    try:
        # 子があるとき
        # 取得したフォルダ(複数)を
        matchDirs = os.listdir(path=path)
        for i in matchDirs:
            # スタックにpathを入れる
            newPath = path + '\\' + i
            stack.append(newPath)
    except:
        # 子がないとき
        return None


while stack:
    targetPath = stack.pop()
    print('検索対象：', targetPath)

    if (targetPath.count(target) == 0):
        searchDir(targetPath)
    else:
        print("見つかりました")
        print("答え：", targetPath)
        break

if not stack:
    print("見つかりませんでした")
