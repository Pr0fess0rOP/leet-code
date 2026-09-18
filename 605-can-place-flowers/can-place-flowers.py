class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        

        length = len(flowerbed)
        possiblePlants = 0

        if flowerbed[-length] == 0 and flowerbed[-length + 1] == 0:
            possiblePlants +=1
            flowerbed[0] = 1
    
        for i in range(1, length-1, 1):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                possiblePlants += 1
                flowerbed[i] = 1

        if flowerbed[length-1] == 0 and flowerbed[length-2] == 0:
            possiblePlants +=1
            flowerbed[length-1] = 1

        if possiblePlants >= n:
            return True
        else:
            return False