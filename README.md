# MergeFiles
merge files with same type [txt, conf] into one file



+ 在 config.py 中填入相应信息

| SOURCE   | TARGET   | EXCLUDE  | ENCODING |
| -------- | -------- | -------- | -------- |
| 文件来源 | 写入文件 | 排除文件 | 编码方式 |

+ 文件来源 SOURCE
  + 列表，可以**同时**写文件夹路径或者文件路径
    + 写入文件夹路径会合并所有该文件夹子目录下的文件将其写入文件
    + 写入文件路径会被合并进写入文件
+ 示例
  + SOURCE = [r"D:\Data", r"D:\Data\Others\a.txt"] 将会将Data子目录下的文件以及Others中的a.txt一起合并进写入文件
  + SOURCE = [r"D:\Data\a.txt", r"D:\Data\b.txt"]将会合并a.txt, b.txt 写入合并文件
  + SOURCE = [r"D:\Data1", r"D:\Data2"]将合并Data1 和 Data2子目录下的所有文件
+ 写入文件 TARGET
  + 合并后文件的保存位置
+ 排除文件 EXCLUDE
  + 在此列表中的文件不受合并影响（优先级高）
+ 编码方式
  + 文件编码方式，默认 utf-8



# 使用方式

在config 文件中填入相应信息，cmd 运行

```shell
python main.py
```

即可。