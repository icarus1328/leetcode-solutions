class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n -= 1
                flowerbed[0] = 1
        else:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                n -= 1
                flowerbed[0] = 1
            i = 1
            while i < len(flowerbed) and n!=0:
                if i == len(flowerbed) - 1:
                    if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                        n -= 1
                        flowerbed[i] = 1
                        i +=1
                    i += 1
                else:
                    if flowerbed[i] != 0:
                        i += 1
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        n -= 1
                        flowerbed[i] = 1
                        i += 1
                    else:
                        i += 1
        return not(bool(n))