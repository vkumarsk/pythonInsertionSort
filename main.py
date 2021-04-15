# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
start = time.time()
def sorting(filename):
  infile = open('20k.txt')
  words = []
  for line in infile:
    temp = line.split()
    for i in temp:
      words.append(i)
  infile.close()

  def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

      key = arr[i]
      j = i - 1
      while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
      arr[j + 1] = key

  insertionSort(words)

  print("Sorted words list is:")
  for i in range(len(words)):
    print("%s" % words[i])

  outfile = open("result.txt", "w")
  for i in words:
    outfile.writelines(i)
    outfile.writelines("\n")
  outfile.close()
sorting("sample.txt")

end = time.time()
print("Execution time:", end-start)