import numpy as np
import matplotlib.pyplot as plt
import random


def experiment(datanum, p):
    # 创建次数数组，作为作图的横坐标
    n_arr = []

    # 结果数组，用以记录结果
    T_arr = []

    for i in range(datanum):  #进行试验
        
        # 生成一个0到1之间的随机浮点数
        random_float = random.random()

        # 判断是否正面朝上。正面朝上则T=1
        if random_float > p:
            T = 0
        elif random_float <= p:
            T = 1
        T_arr.append(T) #每次试验后记录结果
        n_arr.append(i) #记录试验次数

    frequency = sum(T_arr)
    return n_arr, T_arr, frequency

def statistics(T_arr):  #结果解释的函数

    # 相对频率数组，作为作图的纵坐标
    f_arr = []

    n_f = 0   #创建计数菌
    for i, T in enumerate(T_arr):
        if T == 1:
            n_f += 1    #记录事件出现的总次数
        elif T == 0:
            n_f = n_f   #不计数
        f = n_f/(i+1)   #第i次试验的相对频率
        f_arr.append(f) #加入相对频率的数组

    f_final = f_arr[len(T_arr) - 1] #最后一次的相对频率就是整个实验的相对频率
    return f_arr, f_final


def experiment_again(experiment_num, datanum, p):
    frequency_arr = []
    f_final_arr = []    #创建每次实验相对频率的结果数组
    for i in range(experiment_num):
        n_arr, T_arr, frequency = experiment(datanum = datanum, p = p)
        f_arr, f_final = statistics(T_arr)
        f_final_arr.append(f_final) #加入每次试验的结果
        frequency_arr.append(frequency)
    return f_final_arr, frequency_arr
    

def average(data_arr):
    sum = 0
    n = len(data_arr)
    for i, data in enumerate(data_arr):
        sum += data

    return sum/n

def sum(data_arr):
    sum = 0
    for i, data in enumerate(data_arr):
        sum += data

    return sum

def result_plot(x_arr, y_arr, bins = 20, kind = None, **kwargs): 
    if kind == "scatterplot":
        # 绘制散点图
        plt.scatter(x_arr, y_arr, label='Data Points', color='blue', marker='o')  # 设置标签、颜色和标记形状
        plt.xlabel(kwargs.get("xlabel","number of test"))       # x轴标签
        plt.ylabel(kwargs.get("ylabel","relative frequency"))   # y轴标签
        plt.title('{}plot of {}'.format(kwargs.get("kind", "Scatter"), kwargs.get("title", "relative frequency")))  # 图表标题
        plt.legend()  # 显示图例
        plt.grid(True)  # 显示网格
        plt.savefig('./results/problem{}_{}plot of {} wrt. {}.png'.format(kwargs.get("problem_num"), kwargs.get("kind", "Scatter"), kwargs.get("ylabel","relative frequency"), kwargs.get("xlabel","number of test")))
        plt.show()
    
    elif kind == "histogram":
        # 绘制直方图
        plt.hist(y_arr, bins = bins, edgecolor='black')  # bins指定柱状图的数量，edgecolor指定柱子边缘的颜色
        plt.xlabel(kwargs.get("xlabel","number of test"))       # x轴标签
        plt.ylabel(kwargs.get("ylabel","number of heads"))   # y轴标签
        plt.title('{} Plot of {}'.format(kwargs.get("kind", "Histogram"), kwargs.get("title", "number of heads")))  # 图表标题
        plt.savefig('./results/problem{}_{}plot of {} with bins = {}.png'.format(kwargs.get("problem_num"), kwargs.get("kind", "Histogram"), kwargs.get("ylabel","number of heads"), bins))
        plt.show()

    else:
        print("no plots")