# 姐妹种查找器
## SearchSisterSeeds

---

# 介绍
## Introduction
这个程序可以帮你快速在一个txt文件中找到一个种子的姐妹种
但是由于这个程序目前只能单线程运行，所以在读取较大的文件(大于约500M)时运行速度会很慢

This program can help you quickly find sisters of a seed in a txt file.
But since this program can only run in a single thread at present.
So reading larger files (more than 500M or so) will be very slow.

---

# 如何使用
## How to use
在option.ini中的input_file中填写种子库(文件内容形如项目文件中的example.txt，只包含种子码)的路径，
output_file中写输出文件(也就是查找到的姐妹种)的位置。
文件最好用相对路径。

Fill in the path of the seed library (the file content is like example.txt in the project file, only contains the seed code) in the input_file in option.ini,
The location where the output file (that is, the found sister species) is written in output_file.
It is best to use relative paths for files.

---

# 原理
## Principle
**如果你想写一个类似的程序，请不要模仿我的，因为我这样对字符串进行处理的方式很蠢**

**If you want to make a similar program, please don't imitate mine because the way I handle strings like this is stupid**

*如果你能看懂代码的话，读注释或许更有帮助*

*If you can realize the code, it might be more helpful to read the comments*

这涉及到Minecraft对种子码的处理。
简单来说就是，
将一串种子码转化为十六进制数，它的前4位数字决定世界地形的生成，后12位数字决定世界结构的生成。
这样，我们只要筛选后12位数字相同的种子，就可以轻松的找出姐妹种了。

This involves Minecraft's handling of seed codes.
Simply put,
Convert a string of seed codes into hexadecimal numbers, the first 4 digits of which determine the generation of the world terrain, and the last 12 digits to determine the generation of the world structure.
In this way, as long as we filter the seeds with the same last 12 digits, we can easily find the sister seeds.
