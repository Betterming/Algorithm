class Solution:
    def permute(self, nums):
        res = []

        def backtrack(nums, track):
            print(nums, track)
            if len(nums) == len(track):
                res.append(track[:])  # 一定要用track[:] 而不能用track，因为track是引用，当后面改变track时，res对应当track也会改变，所以取当前track的副本放入res中，这时track再改变不会影响到这个副本
                print("res: %s" % res)
                return
            for item in nums:
                if item in track:
                    continue
                track.append(item)
                print(nums, track)
                backtrack(nums, track)
                track.remove(item)
        track = []
        backtrack(nums, track)
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.permute(nums))
