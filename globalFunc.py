import  re
from PyQt5.QtWidgets import *

### 数据包内容转html
def rawhtml(html):
    lst=html.split("\n")
    html_str = ""
    for line in lst:
        html_str+=re.sub(line[:4],"<strong>"+line[:4]+"</strong>",line)
        html_str+="\r"
    return html_str

### 数据包解析转html
def detailhtml(html):
    res=""
    lst = html.split("<br/>")
    for line in lst:
        html_str = re.sub(r"###\[",'###[<font color="#F26666">',line)
        html_str = re.sub(r"\]###", "</font>]###", html_str)
        html_str = re.sub(r"###", "<font color='#757575'>###</font>", html_str)
        #html_str = re.sub(r"((.+?)*) =", r'<font color="yellow">\1</font> =', html_str)
        html_str = re.sub(r"=&nbsp;", r"=&nbsp;<font color='#9277BF'>", html_str)
        res+=html_str+"</font><br/>"
    res = "<strong>"+res+"</strong>"
    return res


### str转Html
def str2html(original_string):
    html_str = re.sub(r"\t","&emsp;",original_string)
    html_str = re.sub(r" ", "&nbsp;", html_str)
    html_str = re.sub(r"[\n\r]", "<br/>", html_str)
    html_str = '<font face="Consolas">' + html_str + '</font>'
    return html_str


def insert_pkt(table,t,src,dst,info):
    row_count =table.PktList.rowCount()  # 返回当前行数(尾部)
    table.PktList.insertRow(row_count)  # 尾部插入一行
    table.PktList.setItem(row_count,0,QTableWidgetItem(t))
    table.PktList.setItem(row_count, 1 , QTableWidgetItem(src))
    table.PktList.setItem(row_count, 2, QTableWidgetItem(dst))
    table.PktList.setItem(row_count, 3, QTableWidgetItem(info))
    QApplication.processEvents()  # 刷新界面