import os,time,datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

# 选择合适的中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']
os.chdir('C:\\Users\\ASUS\\Desktop\\泰迪杯\\第七届泰迪杯赛题C题-全部数据\\附件1-全部数据-450辆车')

def Imp_Data():
    data1 = pd.read_csv('AA00002.csv',encoding='gbk').drop_duplicates()
    data2 = pd.read_csv('AB00006.csv',encoding='gbk').drop_duplicates()
    data3 = pd.read_csv('AD00003.csv',encoding='gbk').drop_duplicates()
    data4 = pd.read_csv('AD00013.csv',encoding='gbk').drop_duplicates()
    data5 = pd.read_csv('AD00053.csv',encoding='gbk').drop_duplicates()
    data6 = pd.read_csv('AD00083.csv',encoding='gbk').drop_duplicates()
    data7 = pd.read_csv('AD00419.csv',encoding='gbk').drop_duplicates()
    data8 = pd.read_csv('AF00098.csv',encoding='gbk').drop_duplicates()
    data9 = pd.read_csv('AF00131.csv',encoding='gbk').drop_duplicates()
    data10 = pd.read_csv('AF00373.csv',encoding='gbk').drop_duplicates()

    data1 = data1.loc[:, ['gps_speed', 'location_time']]
    data2 = data2.loc[:, ['gps_speed', 'location_time']]
    data3 = data3.loc[:, ['gps_speed', 'location_time']]
    data4 = data4.loc[:, ['gps_speed', 'location_time']]
    data5 = data5.loc[:, ['gps_speed', 'location_time']]
    data6 = data6.loc[:, ['gps_speed', 'location_time']]
    data7 = data7.loc[:, ['gps_speed', 'location_time']]
    data8 = data8.loc[:, ['gps_speed', 'location_time']]
    data9 = data9.loc[:, ['gps_speed', 'location_time']]
    data10 = data10.loc[:, ['gps_speed', 'location_time']]
    # 每辆车的数据列表
    data_list = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]
    return data_list

# 计算每辆车的加速度
def Acceleration(data_list):
    # 取出指定的速度列
    column_data = []
    for data in data_list:
        # 取出指定的列
        col_data = data['gps_speed']
        # 将数据存放在列表中
        column_data.append(col_data)

    # 计算每辆车的平均速度存放在列表中
    A_list = []
    for dat in column_data:
        a_list = []
        for i in range(len(dat)-2):
            v1 = (dat.values[i + 1] / 3.6 - dat.values[i] / 3.6) / 3
            v2 = (dat.values[i + 2] / 3.6 - dat.values[i + 1] / 3.6) / 3
            a = (v1 + v2) / 2
            # 保留两位小数点后保存在列表中
            a_list.append(np.round(a, 2))
        A_list.append(a_list)
    return A_list


def DateTime(date_list):
    # 取出指定的日期列
    date_data = []
    for data in date_list:
        # 取出指定的列
        col_data = data['location_time']
        # 将数据存放在列表中
        date_data.append(col_data)
    return date_data


def Acceleration_plot(data, date, lab):
    plt.rcParams['axes.unicode_minus'] = False

    x = pd.to_datetime(date.values)
    x = pd.date_range(start=x.min(), end=x.max(), periods=len(data))
    # 设置figure_size尺寸
    plt.figure(figsize=(13, 6))
    # 多种颜色
    plt.plot(x, data, 'b*-',linewidth=2)
    # y轴取值范围
    plt.ylim(-np.max(data), np.max(data))
    plt.ylabel("加速度（m·s-2）")
    plt.xlabel("日期时间")
    title = "（" + str(lab) + "）" + "加速度变化图"
    plt.title(title)
    # plt.show()
    # 保存图形
    file = "C:/Users/ASUS/Desktop/泰迪杯/第七届泰迪杯数据与题目/图像/" + str(lab) + ".jpg"
    plt.savefig(file)


def Main():
    # 导入数据
    data_list = Imp_Data()
    # 计算加速度
    A_list = Acceleration(data_list=data_list)
    # 日期转换处理
    date_data = DateTime(date_list=data_list)

    label_list = [
                    'AA00002', 'AB00006', 'AD00003', 'AD00013', 'AD00053',
                    'AD00083', 'AD00419', 'AF00098', 'AF00131', 'AF00373'
                 ]
    # 绘制每辆车的平均速度图
    for i in range(len(A_list)):
        print("正在绘制车牌号为 %s 车辆的加速度变化图！" % (label_list[i]))
        Acceleration_plot(data=A_list[i], date=date_data[i], lab=label_list[i])

if __name__ == '__main__':
    print("开始运行程序，请等待！")
    Main()
    print("程序运行结束！")