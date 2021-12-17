### Usage


``` shell
git clone https://github.com/yangguang8112/generate_html.git
pip install -r requeriments.txt

cd generate_html
python main.py [result path]
```
只需要一个参数，分析任务生成的结果文件路径。报告会默认生成到result目录下，名字默认为report。如果指定第二个参数，则指定report的生成位置

该脚本会根据result目录中内容的缺失情况生成对应的html报告内容，无需手动指定生成哪一部分。如果需要手动调整可以到config.py中修改check_sec对应部分为0值。



#### TODO
生成PDF报告