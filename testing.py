
def SumSeries(n):
    if n < 1:
        return 0
    return n + SumSeries(n-2)

print(SumSeries(6))