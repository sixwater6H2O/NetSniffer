from scapy.all import *
from scapy.packet import Packet
from sniffer import *
import sniffer
import time
from globalVal import globalVal
import pyx



#### 设置
### 抓取上限
sniff_count = 0
### 控制台输出高亮
conf.color_theme = BrightTheme()

pkt_cnt=0

### 清空抓取列表
# 输入：无
# 输出：无
def clear_sniff():
    globalVal.sniff_pkts.clear()    ## 清空捕获包列表
    globalVal.pkts_info.clear()     ## 清空摘要列表
    globalVal.sniff_form.PktList.setRowCount(0)
    globalVal.sniff_form.PktList.clearContents()    ## 清空捕获包区域表单
    globalVal.stop_sniff_flag = False   ## 设置停止捕获标志
    pkt_cnt=0

### 保存抓取包
## 输入：保存地址save_path
## 输出：无
def save_sniff(save_path):
    try:
        wrpcap(save_path, globalVal.sniff_pkts,append=False)
    except Exception as e:
        print(e)
        sys.exit(6)



### 回调
## 输入：捕获的数据包packet
## 输出：无
def Callback(packet):
    info = packet.show(dump=True)
    ### 获取src和dst
    if packet.haslayer("IP"):
        src=packet[IP].src
        dst=packet[IP].dst
    elif packet.haslayer("IPv6"):
        src=packet[IPv6].src
        dst=packet[IPv6].dst
    else:
        src=packet.src
        dst=packet.dst

    globalVal.sniff_pkts.append(packet)
    globalVal.pkts_info.append(info)
    now_time = time.localtime()  # 获取本地时间
    t= time.strftime('%Y/%m/%d  %H:%M:%S', now_time)
    pkt_hex = hexdump(packet,dump=True) ## 获取原始内容
    globalVal.pkts_raw.append(pkt_hex)
    summary = packet.summary()          ## 获取摘要
    sniffer.insert_pkt(globalVal.sniff_form, str(t), str(src), str(dst), str(summary))  ## 插入表单


### 判断停止
def IsStop(x):
    return globalVal.stop_sniff_flag

### 开始嗅探
## 输入：过滤器filter，回调函数prn，抓取上限count，停止函数stop_filter
def StartSniff(filter,prn=Callback,count=0,stop_filter=IsStop):
    clear_sniff()
    try:
        QApplication.processEvents()
        sniff(filter=filter, prn=prn, count=count, stop_filter=stop_filter,store=0)
    except Exception as e:
        ### 错误
        print(e)
        sys.exit(-1)




