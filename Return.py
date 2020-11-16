import os

basePath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Sample')
baseDir = os.listdir(path = basePath)

def searchDir(dir,path,cnt):
    j = 1
    space = '  '
    while j <cnt :
        space +='   '
        j += 1

    for i in dir:
       # print(i)
        try:
            newPath = path + '//' + i
            newDir = os.listdir(path = newPath)
            #print(newDir)
            print(space + i)
            searchDir(newDir,newPath,cnt+1)
        except:
            #print(i)
            print(space + i)
            pass


#print(sample)
#print(baseDir)

searchDir(baseDir,basePath,1)