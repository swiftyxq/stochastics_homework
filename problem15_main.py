import problem15_class

def main():
    #第一题到第三题见class
    '''n_arr, T_arr = utils.experiment(datanum = 1000, p = 0.3)    #1000次实验概率p=0.3
    f_arr, f_final = utils.statistics(T_arr)                    #分析实验数据，输出相对频率数组和最终的相对频率
    utils.result_plot(x_arr = n_arr, y_arr = f_arr, args={"scatterplot",})              #绘制散点图

    #第二题
    f_final_arr = utils.experiment_again(experiment_num = 100, datanum = 1000, p = 0.3)   #重复试验100次
    utils.result_plot(x_arr = [], y_arr = f_final_arr, bins = 10, args={"histogram",})  #作出十个块块的直方图

    #第三题
    np_calculate = utils.average(f_final_arr)
    n = 1000    #实验次数
    p = 0.3     #概率
    delta_np = (np_calculate - n*p) / (n*p) #计算实际值和理论值的相对偏差'''
    subproblem123 = problem15_class.problems(n = 1000, p = 0.3, experiment_num = 100)
    subproblem123.subproblem1(15.1)
    subproblem123.subproblem2(15.2)
    subproblem123.subproblem3(15.3)
    #第四题
    subproblem4 = problem15_class.problems(n = 10000, p = 0.7, experiment_num = 1000) #第四题自己试验其他参数
    subproblem4.subproblem1(15.4)
    subproblem4.subproblem2(15.4)
    subproblem4.subproblem3(15.4)

    
    
if __name__ == '__main__':
    main()