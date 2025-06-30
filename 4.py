# решение подсмотрел тут: https://itfy.org/threads/zadacha-na-ogranichenie-chisla-operacij.3087/post-15397

n, k = map(int, input().split())
nums = sorted(map(int, input().split()), reverse=True)


gains = list()

for num in nums:
	curr_n = num
	weight = 1

	while (curr_n > 0):
		digit = curr_n % 10
		gains.append((9 - digit) * weight)
		weight *= 10
		curr_n //= 10


gains.sort(reverse=True)
print(sum(gains[:k]))