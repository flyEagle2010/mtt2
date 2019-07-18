
import pandas as pd
import os
import shutil
import time


def CreateExcel(file):
    localtime = time.asctime(time.localtime(time.time()))
    print("本地时间为 :", localtime)
    print("time:", time.strftime("%Y%m%d", time.localtime()))
    shutil.copyfile(file, "./excel/"+time.strftime("%Y%m%d",
                                                   time.localtime())+"-"+file.split("/")[-1])


def CreateResult(file):
    df = pd.read_excel("./excel/"+file, sheet_name=0)
    print("df: ", df.dropna(axis=1, how='all'))
    # for i in range(len(df[0])):
    #     print("i:", i)
