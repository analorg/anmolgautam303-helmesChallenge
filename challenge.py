import time, sys
start_time = time.time()
anagramList = []
with open('lemmad.txt', 'rb') as file:
    for value in enumerate(file):
        w = value[1].strip('\r\n')
        if(sorted(w) == sorted(sys.argv[1])):
            anagramList.append(w)
print('Output (duration,list,of,anagrams,found): ' + str((time.time() - start_time) * 1000000) + ',' + ",".join(map(str,anagramList)))
