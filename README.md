# hxmt_pipeline

## 概览

HXMT 批处理Python程序。使用该程序，你可以产生一个shell脚本，该脚本中包含了完成HXMT数据处理所需要的所有命令。

## 获得该脚本

该脚本托管在高能所GitLab的仓库 http://code.ihep.ac.cn/hxmthsdc/hxmt_pipeline
你可以通过 ```git clone git@code.ihep.ac.cn:hxmthsdc/hxmt_pipeline.git``` 下载，并使用```git pull```更新。

## 使用该脚本

运行 ``` python hpipeline.py -h ``` 查看使用说明，运行结果如下:

```
usage: hpipeline.py [-h] [-i INPUT] [-I INPUTLIST] [-o OUTPUT] [-O OUTPUTLIST]
                    [-b BASH] [--hxbary] [-r RA] [-d DEC] [-v VERSION]
                    [--LE_LC_EMIN LE_LC_EMIN] [--LE_LC_EMAX LE_LC_EMAX]
                    [--ME_LC_EMIN ME_LC_EMIN] [--ME_LC_EMAX ME_LC_EMAX]
                    [--HE_LC_EMIN HE_LC_EMIN] [--HE_LC_EMAX HE_LC_EMAX]

    -------------------------------
    Notice :
        HXMTsoft pipeline. Using this program, you can generate a shell script that
        contains all the commands you need to complete the HXMT data processing.

	<span style="color: green"> !!! The software is currently used to process hxmtsoft version 2.04,
        if you need to process version 2.02 of hxmtsoft, use the --version parameter
        use -h parameter to see detail!!! </span>
    -------------------------------

    Example: hpipeline -i /DATA_PATH/ExpID/ -o /OUTPUT_PATH/ --hxbary -r 83.63322083 -d 22.014461 -b bash-script-name.sh

basic arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        data archived path
  -I INPUTLIST, --inputlist INPUTLIST
                        data archived path in list
  -o OUTPUT, --output OUTPUT
                        products archived path
  -O OUTPUTLIST, --outputlist OUTPUTLIST
                        products archived path in list
  -b BASH, --bash BASH  produce a bash script file
  --hxbary              carry out Barycentric correction

optional arguments:
  -r RA, --ra RA        right ascension of barycentering correction
  -d DEC, --dec DEC     declination of barycentering correction
  -v VERSION, --version VERSION
                        the pipeline is compatible with HXMTsoft version 2.04
                        (default), if --version 2.02 , the pipeline is
                        compatible with HXMTsoft v2.02
  --LE_LC_EMIN LE_LC_EMIN
                        lower limits for LE lightcurve
  --LE_LC_EMAX LE_LC_EMAX
                        upper limits for LE lightcurve
  --ME_LC_EMIN ME_LC_EMIN
                        lower limits for ME lightcurve
  --ME_LC_EMAX ME_LC_EMAX
                        upper limits for ME lightcurve
  --HE_LC_EMIN HE_LC_EMIN
                        lower limits for HE lightcurve
  --HE_LC_EMAX HE_LC_EMAX
                        upper limits for HE lightcurve

    Example for selecting LC energy range:
    	hpipeline -i /DATA_PATH/ExpID/ -o /OUTPUT_PATH/ --hxbary -r 83.63322083 -d 22.014461 -b bash-script-name.sh --LE_LC_EMIN=2 --LE_LC_EMAX=7 --ME_LC_EMIN 11 --ME_LC_EMAX 28 --HE_LC_EMIN 30 --HE_LC_EMAX 100 --version=2.04

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
- ```-v```: (optional) 选择 hpipeline 所 适配的 HXMTsoft 版本(默认为v2.04)
- ```--LE_LC_EMIN```: (optional) 选择 LE 光变曲线的能段下限(keV)
- ```--LE_LC_EMAX```: (optional) 选择 LE 光变曲线的能段上限(keV)
- ```--ME_LC_EMIN```: (optional) 选择 ME 光变曲线的能段下限(keV)
- ```--ME_LC_EMAX```: (optional) 选择 ME 光变曲线的能段上限(keV)
- ```--HE_LC_EMIN```: (optional) 选择 HE 光变曲线的能段下限(keV)
- ```--HE_LC_EMAX```: (optional) 选择 HE 光变曲线的能段上限(keV)
- ```--HE_LC_BINSIZE```: (optional) 设置 HE 光变曲线的时间 bin (s)
- ```--ME_LC_BINSIZE```: (optional) 设置 ME 光变曲线的时间 bin (s)
- ```--LE_LC_BINSIZE```: (optional) 设置 LE 光变曲线的时间 bin (s)
- ```--clean```: (optional) 清除中间过程产生的事例文件(*pi*, *recon*, *grade*)
- ```--parallel```: (optional) 设置脚本并行的环境变量
