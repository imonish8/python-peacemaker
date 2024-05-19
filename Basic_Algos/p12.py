n = int(input())
arr = list(map(int, input().split()))

unique_scores = list(set(arr))

unique_scores.sort()

# now print the second last high scxore to get the runner up of the match,

print(unique_scores[-2])