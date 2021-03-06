# 1. 基本的shell指令

1. ps 查看进程 

   1. ps -ef ：
   2. ps -ef |grep ： 查看某个关键字匹配的进程
   3. ps -f :

2. top 查看进程（活动）

   1. -d： 设置刷新时间
   2. -q： 退出

3. kill 杀死进程

   1. kill 进程号
   2. killall 通过进程名杀死进程

4. top 从头部开始显示文件

   1. -n ： 设置显示行数

5. tail 从尾部显示文件

   1. -n： 设置显示行数

6. rm 删除文件和文件夹

   1. -i 提示是否删除

7. mv 移动文件

   1. -i 提示是否覆盖等

8. cp 拷贝文件

   1. -i: 提示是否覆盖等

9. tree 显示文件夹目录结构

10. ls 显示文件夹内容

    1. -l list显示

11. touch 创建新文件或文件夹(空)

12. mount 挂载可移动设备

13. umount 卸载可移动设备

14. df 查看所有已挂载设备的剩余空间

15. du 查看当前目录的磁盘使用情况

    1. -h 显示更为人性化

16. sort 对数据进行排序

    1. 默认情况下，sort会将内容识别为字符进行比较
    2. -n 按值排序
    3. -M 按月排序
    4. -t 指定字段分隔符
    5. -k 指定排序的字段
    6. -r 结果降序输出

17. grep 搜索

    1. 例如在file.txt中查看fire

       grep fire file.txt

    2. -v 反向搜索，搜出不匹配的记录

    3. -n 显示匹配记录所在的行数

    4. -c 显示匹配模式的行数

    5. -e 如果需要匹配多个模式，用-e分割模式

18. tar 压缩，解压缩

    1. -A 将一个已有tar归档文件追加到另外一个tar归档文件
    2. -c 创建一个新的tar归档文件
    3. -r 追加文件到已有tar归档文件的末尾
    4. -t 列举已有归档文件的的内容
    5. -x 提取归档文件中的内容
    6. -C 切换到指定目录
    7. -f 输出结果到文件
    8. -p 保留所有权限
    9. -v 处理文件时显示文件
    10. -z 将输出重定向到gzip命令来压缩文件
    11. tar -cvf test.tar 创建文件
    12. tar -tf test.tar 查看归档文件内容
    13. tar -xvf test.tar 提取内容

19. exit : 退出bash 获取退出交互式环境

20. sleep n : 睡眠n秒后返回交互式

21. jobs: 显示当前运行在后台模式中的所有用户的进程

    1. jobs -l 显示更多相关信息

22. coproc 进程名 { ... } : 创建一个子进程，实行指令

23. type: 查看命令

24. 内建命令是已经编译在bash shell中的命令，外建命令与之相反

25. alias：起别名

26. history： 获取历史输入的命令

27. env/printenv: 查看环境变量

28. echo $变量名 ：打印变量

29. export：定义了一个变量之后，可以用export指令使其成为全局变量

30. unset：删除全局变量

31. chmod：修改文件的权限

    1. r 可读

    2. w 可写

    3. x 可执行

    4. u：当前用户，g：用户组，o：其他用户

       ```shell
       chmod u-rwx shell1.sh #当前用户去除读写可执行权限
       ```

32. 







# 2. Linux和Shell相关知识点

1. 环境变量

2. 数组

   ```shell
   array=(1 2 3 4 5) # 数组用空格分隔 
   
   echo $array # 打印整个数组
   
   echo ${array[2]} # 打印某个下标的元素
   
   echo ${array[*]} # 遍历数组
   
   unset array[1] # 删除指定数组下标的元素
   
   unset array # 删除整个数组
   ```

3. 声明变量时不能有空格

   ```shell
   my_variable=hello
   
   my_variable='hello world' # 有空格则需要用引号括起来
   ```

   

4. 文件的访问权限
   1. r 可读
   2. w 可写
   3. x 可执行
5. 