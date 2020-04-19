# 1. Create a python program that reads apache log file - access_log and from that log file using regular expressions
# extracts and group following information:
# - IP address
# And based on that information:
# - show top 5 IP addresses based on the count of connections
import re
from collections import Counter


class AccessLog:
    def apacheLogConter(self):
        ipRegex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

        with open(self) as f:
            self = f.read()
            ipList = re.findall(ipRegex,self)
            ipCount = Counter(ipList)
            for k, v in ipCount.most_common(5):
                print("IP address:", str(k), " Count:", str(v))

    if __name__ == "__main__":
        apacheLogConter("exercise_07/access_log")