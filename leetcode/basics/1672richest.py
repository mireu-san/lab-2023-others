class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for i in range(len(accounts)):
            totalWealth = sum(accounts[i])
            maxWealth = max(maxWealth, totalWealth)
        return maxWealth




# wrong answer
# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         maxWealthSoFar = 0;

#         for i in accounts:
#             currentCustomerWealth = 0;

#             for (bank : customer) {
#                 currentCustomerWealth += bank;
#             }
#             maxWealthSoFar = Math.max(maxWealthSoFar, currentCustomerWealth);
#         }
#         return maxWealthSoFar;
#     }

# }