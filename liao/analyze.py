import matplotlib.pyplot as plt

chapter_name = ['Python教程', 'Python简介', '安装Python', 'Python解释器', '第一个Python程序', '使用文本编辑器', 'Python代码运行助手', '输入和输出', 'Python基础', '数据类型和变量', '字符串和编码', '使用list和tuple', '条件判断', '循环', '使用dict和set', '函数', '调用函数', '定义函数', '函数的参数', '递归函数', '高级特性', '切片', '迭代', '列表生成式', '生成器', '迭代器', '函数式编程', '高阶函数', 'map/reduce', 'filter', 'sorted', '返回函数', '匿名函数', '装饰器', '偏函数', '模块', '使用模块', '安装第三方模块', '面向对象编程', '类和实例', '访问限制', '继承和多态', '获取对象信息', '实例属性和类属性', '面向对象高级编程', '使用__slots__', '使用@property', '多重继承', '定制类', '使用枚举类', '使用元类', '错误、调试和测试', '错误处理', '调试', '单元测试', '文档测试', 'IO编程', '文件读写', 'StringIO和BytesIO', '操作文件和目录', '序列化', '进程和线程', '多进程', '多线程', 'ThreadLocal', '进程 vs. 线程', '分布式进程', '正则表达式', '常用内建模块', 'datetime', 'collections', 'base64', 'struct', 'hashlib', 'itertools', 'contextlib', 'XML', 'HTMLParser', 'urllib', '常用第三方模块', 'PIL', 'virtualenv', '图形界面', '网络编程', 'TCP/IP简介', 'TCP编程', 'UDP编程', '电子邮件', 'SMTP发送邮件', 'POP3收取邮件', '访问数据库', '使用SQLite', '使用MySQL', '使用SQLAlchemy', 'Web开发', 'HTTP协议简介', 'HTML简介', 'WSGI接口', '使用Web框架', '使用模板', '异步IO', '协程', 'asyncio', 'async/await', 'aiohttp', '实战', 'Day 1 - 搭建开发环境', 'Day 2 - 编写Web App骨架', 'Day 3 - 编写ORM', 'Day 4 - 编写Model', 'Day 5 - 编写Web框架', 'Day 6 - 编写配置文件', 'Day 7 - 编写MVC', 'Day 8 - 构建前端', 'Day 9 - 编写API', 'Day 10 - 用户注册和登录', 'Day 11 - 编写日志创建页', 'Day 12 - 编写日志列表页', 'Day 13 - 提升开发效率', 'Day 14 - 完成Web App', 'Day 15 - 部署Web App', 'Day 16 - 编写移动App', 'FAQ', '期末总结']
reads = [6062945, 2168593, 1129478, 893664, 906604, 1020312, 1066382, 920545, 640954, 1035435, 895455, 885729, 585503, 568245, 709940, 341383, 543800, 572882, 604998, 387342, 276236, 431577, 388256, 412892, 479150, 353501, 253617, 295225, 434809, 308864, 234537, 276655, 220893, 328556, 214525, 195442, 314968, 282204, 260485, 345341, 226342, 227761, 214833, 186246, 149179, 225434, 202616, 143525, 188167, 133526, 254175, 125747, 177257, 117164, 128980, 80197, 116454, 259374, 163016, 156253, 137260, 136153, 222005, 152011, 86863, 84741, 93527, 195769, 62927, 150996, 90197, 66157, 58179, 51312, 45956, 31618, 71006, 72118, 201903, 61110, 99795, 194935, 186651, 86464, 125244, 143328, 49189, 26666, 89487, 14444, 48179, 94642, 153020, 60810, 66462, 130192, 60400, 98478, 122617, 69593, 76964, 101708, 127565, 60805, 67671, 41815, 381985, 258767, 221299, 71713, 84137, 18688, 40808, 40100, 46060, 64240, 9901, 3942, 12830, 61714, 69796, 137466, 6063, 46360]

def list2dict(list_name): 
    return dict(zip(range(len(list_name)),list_name))


#use d.items() to get (keys,values),

#d.keys() -> a list only include keys
#d.values() -> a list only include values

#use dict_name(key) to get the relation about key and chapter_name/reads

chapter_name_dict = list2dict(chapter_name)
reads_dict = list2dict(reads)

#define trans = list[i+1]/list[i]

trans_rate_list = []

for i in range(len(reads)-1):
    trans_rate = reads[i+1] / reads[i]
    trans_rate = round(trans_rate,2)
    trans_rate_list.append(trans_rate)