# a = [[1, 2], [3, 4]]
#
# print(sum(a, []))
#
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         c = 1000 - a - b
#         if a * a + b * b == c**2:
#             print(f"a:{a} b:{b} c:{c}")


a = [[1, 2, 3], [4, 5, 6, 6], [7, 8, 9]]

lt = []


for i in a:
    lt += i
print(lt)

[lt.append(i) for i in a]