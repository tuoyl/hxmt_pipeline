# hxmt_pipeline

``` python hpipeline_v2.01.py -h ```


```usage: hpipeline_v2.01.py [-h] [-i INPUT] [-I INPUTLIST] [-o OUTPUT]```
```                          [-O OUTPUTLIST] [-b BASH_SCRIPT] [--hxbary] [-r R]```
```                          [-d DEC]```

Example: python he_pipeline.py -i /DATA_PATH/ExpID/ -o /OUTPUT_PATH/ExpID/ --hxbary -r 83.63322083 -d 22.014461

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
  
  
 ```git clone https://github.com/tuoyl/hxmt_pipeline.git```
