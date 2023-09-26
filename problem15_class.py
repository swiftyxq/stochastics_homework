import problem15_utils as utils

class problems():
    def __init__(self, n, p, experiment_num):
        self.n = n
        self.p = p
        self.experiment_num = experiment_num
    
    
    #第一题
    def subproblem1(self, problem_number):
        n_arr, self.T_arr, frequency = utils.experiment(datanum = self.n, p = self.p)    #1000次实验，概率p=0.3
        f_arr, f_final = utils.statistics(self.T_arr)                    #分析实验数据，输出相对频率数组和最终的相对频率
        utils.result_plot(x_arr = n_arr, y_arr = f_arr, kind = "scatterplot", problem_num = problem_number,)              #绘制散点图
    #第二题
    def subproblem2(self, problem_number):
        self.f_final_arr, self.frequency_arr = utils.experiment_again(experiment_num = self.experiment_num, datanum = self.n, p = self.p)   #重复试验100次
        utils.result_plot(x_arr = [], y_arr = self.f_final_arr, bins = 10, kind = "histogram", problem_num = problem_number)  #作出十个块块的直方图

    #第三题
    def subproblem3(self, problem_number):
        headnum_average = utils.average(self.frequency_arr)
        #print(self.frequency_arr)
        #print(np_calculate)
        delta_np = (headnum_average - self.n*self.p) / (self.n*self.p) #计算实际值和理论值的相对偏差
        print("for problem{}, n = {}, p = {}".format(problem_number, self.n, self.p))
        print("for problem{}, Delta_np = (np_calculate - n*p)/(n*p) = {}".format(problem_number, delta_np))
