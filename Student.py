from Hello import Hello
import inspect


class Student(object):
    # def init(self, name, score):
    #     self.name = name
    #     self.score = score

    def get_grade(self):
        if self.score >= 60 and self.score < 80:
            return 'B'
        if self.score >= 80 and self.score <= 100:
            return 'A'
        if self.score < 0 or self.score > 100:
            raise ValueError("错误的值")
        return "C"

    def fun(self, name,age):
        print(name)
        print("fun")

    def click_element(self,values):
        print(values)
        print("click")



if __name__ == '__main__':
    V_lsit = []
    action_values = "open|element|values"
    # 将action_values根据"|"切割
    action_list = action_values.split("|")
    action_list[1:]
    str_test = "zhang"
    age_test = 20
    print(action_list)
    key_values = {"open": "fun", "click": "click_element"}
    print(key_values.get(action_list[0]))
    # 判断自然语言是否可匹配到字典中的key
    if action_list[0] in key_values.keys():
        # 反射获取到相应的方法信息
        fun_values = getattr(Student, key_values.get(action_list[0]))
        print("fun_name", fun_values)

        # 获取到该函数的参数
        all_args = inspect.getfullargspec(fun_values)
        # 判断该函数参数若为空或参数只有一个self
        if len(all_args.args) <= 1 and "self" in all_args.args:
            fun_values(Student)

        # 若函数参数大于1个进入判断
        else:
            print(type(all_args.args))
            print(all_args)
            # 将self在方法的参数中剔除
            all_arg = all_args[1:]
            # 动态将action_List中的数据遍历到V_list集合中
            for i in all_args.args[1:]:
                V_lsit.append(i)
                V_lsit = action_list[1:]
            # 方法的输出参数应加判断
            if len(V_lsit) == 1:
                fun_values(Student, V_lsit[0])
            elif len(V_lsit) == 2:
                fun_values(Student, V_lsit[0], V_lsit[1])
