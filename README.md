# hxmt_pipeline

## 概览

HXMT 批处理Python程序。使用该程序，你可以产生一个shell脚本，该脚本中包含了完成HXMT数据处理所需要的所有命令。

## 获得该脚本

该脚本托管在高能所GitLab的仓库 http://code.ihep.ac.cn/tuoyl/hxmt_pipeline.git
你可以通过 ```git clone http://code.ihep.ac.cn/tuoyl/hxmt_pipeline.git``` 下载，并使用```git pull```更新。

## 使用该脚本

运行 ``` python hpipeline.py -h ``` 查看使用说明，运行结果如下:

```
usage: hpipeline.py [-h] [-i INPUT] [-I INPUTLIST] [-o OUTPUT]
                            [-O OUTPUTLIST] [-b BASH_SCRIPT] [--hxbary] [-r R]
                            [-d DEC]
                            

Example: python hpipeline.py -i /DATA_PATH/ExpID/ -o /OUTPUT_PATH/ExpID/ -b bash-script-name.sh --hxbary -r 83.63322083 -d 22.014461

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        data archived path
  -I INPUTLIST, --inputlist INPUTLIST
                        data archived path in list
  -o OUTPUT, --output OUTPUT
                        products archived path
  -O OUTPUTLIST, --outputlist OUTPUTLIST
                        products archived path in list
  -b BASH_SCRIPT, --bash-script BASH_SCRIPT
                        produce a bash script file
  --hxbary              carry out Barycentric correction
  -r RA, --ra RA        right ascension of barycentering correction
  -d DEC, --dec DEC     declination of barycentering correction
```
说明：使用脚本```hpipeline```的过程中，有这么几个参数
- ```-i```: 原始数据的绝对路径（到曝光号，例如Crab的数据为 ```/directory/something/P0101299/P0101299001/P010129900101-20170827-01-01/```，最后```P010129900101-20170827-01-01/```就是曝光号）
- ```-o```：输出文件的保存路径
- ```-I```：你的输入可以是多个曝光号，将这些曝光号的绝对路径存放在一个文本文件中（每个曝光号占一行），使用```-I```输入该文本文件的文件名
- ```-O```：如果你使用```-I```输入，则输出也需要是多个路径，存放在文本文件中
- ```-b```：产生的shell文件的文件名
- ```--hxbary```：(optional) 若使用该参数，则对数据做太阳系质心修正
- ```-r```：(optional) 质心修正中使用的天体源的赤经值
- ```-d```：(optional) 质心修正中使用的天体源的赤纬值


  


