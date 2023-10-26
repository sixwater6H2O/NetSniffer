from sniffer import *
from sniff import *

class globalVal:
    def _init(self):
        global sniff_form   ##抓包列表
        global stop_sniff_flag  ##停止嗅探标志
        ##数据包列表、数据包摘要、数据包原始内容、过滤器
        global sniff_pkts,pkts_info,pkts_raw,sniff_filter
        sniff_form = Ui_Form()

        ### 停止抓取标志
        stop_sniff_flag = True
        sniff_pkts = scapy.plist.PacketList()
        pkts_info = []
        pkts_raw = []
        sniff_filter = ""

### 初始化函数
def init_globalVal():
    globalVal.stop_sniff_flag = True
    globalVal.sniff_pkts = scapy.plist.PacketList()
    globalVal.pkts_info = []
    globalVal.pkts_raw = []
    globalVal.sniff_filter = ""