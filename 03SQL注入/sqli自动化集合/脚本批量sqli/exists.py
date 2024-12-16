import os
import shutil
def get_exists(path,sum):
    sum=0
    for root,dirs,files in os.walk(path):
        log_path=os.path.join(root,"log")
        if os.path.isfile(log_path) and os.path.getsize(log_path)==0:
            shutil.rmtree(root)
        else:
            sum+=1
            print(root+"\t注入成功")
            continue
    return sum
if __name__ == '__main__':
    path=r"result"
    print("--------------------开启执行--------------------")
    sum=get_exists(path,sum)
    print("--------------------成功找到{}注入点--------------------".format(sum-1))