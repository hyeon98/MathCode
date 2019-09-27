
class Fibonacci:    # 클래스
    def Cal(self, num):
        n0 = 0
        n1 = 1
        prevR = 0
        pPrevR = 0
        result = 0

        for i in range(0, num):
            if(i == 0):
                result = n0 + n1
                prevR = result
            else:
                result = prevR + pPrevR
                pPrevR = prevR
                prevR = result        

        return result

# def Cal(num):
#     if(num <= 1):
#         return num
#     else:
#         return Cal(num-1) + Cal(num-2)        

if __name__ == "__main__":
    resultCal = Fibonacci().Cal(20)
    print(resultCal)
    