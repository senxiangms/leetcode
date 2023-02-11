class Solution:
    def ipToCIDR(self, ip: str, n: int) :
        def str2long(ip):
            arr = ip.split('.')
            s = 0
            for ss in arr:
                s = int(ss) + s * 256
            return s
        def long2ip(start, step):
            bits = 0
            while step:
                bits +=1
                step = step//2
            
            latter = str(32-bits+1)
            ips = []
            while start:
                po = start % 256
                start = start//256
                
                ips.append(str(po))
            return ".".join(ips[::-1]) + "/" + latter

        start = str2long(ip)
        print(start)
        end = start + n
        ret = []
        while start < end:
            step = start & -start
            while start + step > end: 
                step = step // 2
            ret.append(long2ip(start, step))
            start = start + step

        
        return ret


sol = Solution()
sol.ipToCIDR("0.171.255.5", 422)