#day2
#question4
#question link=https://leetcode.com/problems/defanging-an-ip-address/
#for more such solutions go to:-    https://github.com/prakash079


---------------------------------------

#solution
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address=address.replace('.',"[.]")
        return address 
      
