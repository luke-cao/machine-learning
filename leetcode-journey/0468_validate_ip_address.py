import re

class Solution:
    def validIPAddress(self, IP: str) -> str:
        pattern_ipv4 = re.compile(r'((([0-9]|[1]\d{0,2})|(2[0-4]\d)|(25[0-5]))\.){3}(([0-9]|[1]\d{0,2})|(2[0-4]\d)|(25[0-5]))')
        if len(IP) < 7 or len(IP) > 39:
            return 'Neither'
        if pattern_ipv4.fullmatch(IP):
            return 'IPv4'
        elif re.fullmatch(r'([0-9a-fA-F]{1,4}\:){7}([0-9a-fA-F]{1,4})', IP):
            return 'IPv6'
        return 'Neither'


print(Solution().validIPAddress('01.01.01.01'))
print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))