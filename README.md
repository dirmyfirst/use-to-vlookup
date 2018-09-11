# use-to-vlookup
    python3界面化实现快速vloopup功能，需安装以下模块：
pip install pandas<br>
pip install wxpython<br>

    使用数据格式如下：
* 表1:<br>
id  value<br>
aa  a<br>
bb  b<br>
cc  c<br>

* 表2:<br>
id  value<br>
aa  11<br>
bb  22<br>


    合并后输出于当前路径，格式为csv：
* 合并后的表:<br>
id	b_x	b_y<br>
aa	a	  11<br>
bb	b	  22<br>
cc	c	  nan<br>
