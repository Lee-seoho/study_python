# 1~15까지 출력
# for i in range(15):
#     print(i + 1)

# 30~1까지 출력
# for i in range(30):
#     print(30 - i)

#0 1 2 3 4
#1 3 5 7 9
# 1~100까지 중 홀수만 출력
# for i in range(50):
#     print(i * 2 + 1)

# 1~10까지 합 출력
# result = 0
# for i in range(10):
#     # result = result + i + 1
#     result += i + 1
#
# print(result)

# 1~n까지 합 출력
# message = "1~n까지의 합\nn: "
# end = int(input(message))
# result = 0
#
# for i in range(end):
#     result += i + 1
#
# print(result)

# 3 4 5 6 3 4 5 6 3 4 5 6 출력
for i in range(12):
    print(i % 4 + 3, end=' ')

result = 0
for i in range(10):
    result += i + 1
print(result)

message = "1 부터 n 까지 합\nn:"
end = int(input(message))
result = 0
for i in range(end):
    result += i + 1
print(result)

for i in range(12):
    result = i % 4 + 3
    print(result,end=" ")