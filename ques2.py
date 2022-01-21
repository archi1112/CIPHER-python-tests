
def findFirstMissing(array, start, end):

	if (start > end):
		return end + 1

	if (start != array[start]):
		return start;

	mid = int((start + end) / 2)
	if (array[mid] == mid):
		return findFirstMissing(array,
						mid+1, end)

	return findFirstMissing(array,
						start, mid)

arr = [int (ele) for ele in input().split(' ')]
n = len(arr)
print("Smallest missing element is",
	findFirstMissing(arr, 0, n-1))