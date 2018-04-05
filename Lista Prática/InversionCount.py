#Inversion Sort
#http://www.thehuxley.com/problem/2045?quizId=2687

def merge_and_count_inversions(seq, start, middle, end):
    assert 0 <= start < middle < end <= len(seq)
    inversions = 0
    temp = []
    i = start
    j = middle
    while i < middle and j < end:
        if seq[i] <= seq[j]:
            temp.append(seq[i])
            i += 1
        else:
            temp.append(seq[j])
            j += 1
            inversions += middle - i
    if j == end:
        temp.extend(seq[i:middle])
    else:
        pass
    seq[start:start+len(temp)] = temp
    return inversions

def sort_and_count_inversions(seq):

    def sort_and_count(seq, start, end):
        if end - start < 2:
            return 0
        middle = (start + end) // 2
        return (sort_and_count(seq, start, middle)
                + sort_and_count(seq, middle, end)
                + merge_and_count_inversions(seq, start, middle, end))
    return sort_and_count(seq, 0, len(seq))

def le_num():
  a = int(input())
  return a


arr = []

testes = int(input())
branco = input()

#print(branco,'<')

while testes != 0:
  tam_arr = int(input())
  while tam_arr != 0:
    arr.append(le_num())
    tam_arr = tam_arr - 1
  if(testes != 1):
    branco = input()


  resultado = sort_and_count_inversions(arr)
  print(resultado)
  arr = []
  testes = testes-1