class Phone:
    __current_voltage=0.2# 私有变量
    def __keep_single_core(self):# 私有方法
        print("CPU以单核模式运行")
    def call_by_5g(self):# 成员方法可以调用私有变量和方法
        if self.__current_voltage>=1:
            print("5g已开启")
        else:
            self.__keep_single_core()
            print("电量不足，已开启省电")

phone=Phone()
phone.call_by_5g()
