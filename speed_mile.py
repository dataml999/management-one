import os
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

    data1 = data1.loc[:, ['gps_speed', 'mileage']]
    data2 = data2.loc[:, ['gps_speed', 'mileage']]
    data3 = data3.loc[:, ['gps_speed', 'mileage']]
    data4 = data4.loc[:, ['gps_speed', 'mileage']]
    data5 = data5.loc[:, ['gps_speed', 'mileage']]
    data6 = data6.loc[:, ['gps_speed', 'mileage']]
    data7 = data7.loc[:, ['gps_speed', 'mileage']]
    data8 = data8.loc[:, ['gps_speed', 'mileage']]
    data9 = data9.loc[:, ['gps_speed', 'mileage']]
    data10 = data10.loc[:, ['gps_speed', 'mileage']]
    # 每辆车的数据列表
    data_list = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]

    return data_list

# 计算每辆车的里程和平均速度函数
def Gps_speed(data_list):
    # 取出指定的速度列
    column_data = []
    for data in data_list:
        # 取出指定的列
        col_data = data['gps_speed']
        # 将数据存放在列表中
        column_data.append(col_data)

    # 计算每辆车的平均速度存放在列表中
    mean_speed_list = []
    for dat in column_data:
        mean = np.mean(list(dat.values))
        # 保留两位小数点后保存在列表中
        mean_speed_list.append(round(mean, 2))
    return mean_speed_list

def Mile(data_list):
    # 取出指定的里程列
    mile_data = []
    for data in data_list:
        # 取出指定的列
        col_data = data['mileage']
        # 将数据存放在列表中
        mile_data.append(col_data)

    # 计算每辆车的里程数存放在列表中
    mile_list = []
    for ml in mile_data:
        mile_list.append(ml.values.max() - ml.values.min())
    return mile_list

def Speed_Bar_plot(data):
    print("正在绘制车辆平均速度图！")
    label_list = ['AA00002','AB00006','AD00003','AD00013','AD00053','AD00083','AD00419','AF00098','AF00131','AF00373']
    x = range(len(data))
    # 设置figure_size尺寸
    plt.figure(figsize=(10, 5))
    # 多种颜色
    rects = plt.bar(x=x, height=data, width=0.7, alpha=0.8, color='rgy')
    # 给条形图贴上数据标签
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height) + 'km/h', ha="center", va="bottom")

    # 给X轴贴上标签
    plt.xticks([index for index in x], label_list)
    # y轴取值范围
    plt.ylim(0, np.max(data)+10)
    plt.ylabel("平均速度（km/h）")
    plt.xlabel("车辆")
    plt.title("车辆平均速度图")
    # plt.show()
    file = "C:/Users/ASUS/Desktop/泰迪杯/第七届泰迪杯数据与题目/图像/mean_speed.jpg"
    # 保存图形
    plt.savefig(file)

def Mile_Bar_plot(data):
    print("正在绘制车辆里程图！")
    label_list = ['AA00002','AB00006','AD00003','AD00013','AD00053','AD00083','AD00419','AF00098','AF00131','AF00373']
    x = range(len(data))
    # 设置figure_size尺寸
    plt.figure(figsize=(10, 5))
    # 多种颜色
    rects = plt.bar(x=x, height=data, width=0.7, alpha=0.8, color='rgy')
    # 给条形图贴上数据标签
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height) + 'km', ha="center", va="bottom")

    # 给X轴贴上标签
    plt.xticks([index for index in x], label_list)
    # y轴取值范围
    plt.ylim(0, np.max(data)+1000)
    plt.ylabel("里程（km）")
    plt.xlabel("车辆")
    plt.title("车辆里程图")
    # plt.show()
    file = "C:/Users/ASUS/Desktop/泰迪杯/第七届泰迪杯数据与题目/图像/total_mile.jpg"
    # 保存图形
    plt.savefig(file)


def Main():
    print("开始运行程序，请等待！")
    # 导入数据
    data_list = Imp_Data()
    # 计算平均速度
    speed_mean = Gps_speed(data_list)
    # 计算总里程
    mile_total = Mile(data_list)
    # 绘制每辆车的平均速度图
    Speed_Bar_plot(speed_mean)
    # 绘制每辆车的总里程图
    Mile_Bar_plot(mile_total)
    print("程序运行结束！")

if __name__ == '__main__':
    Main()