sequences = {}

def add_new_sequences(new_sequences,count):
    global sequences
    for key,val in new_sequences.items():
        if val == count:
            sequences[key] = val
        else:
            sequences[key] = count - val


def colletz_cnt_from_int(n):
    global sequences
    cur = n
    count = 1
    new_sequence_cnts = {}
    while cur != 1:
        if cur in sequences:
            count += sequences[cur]
            break
        else:
            new_sequence_cnts[cur] = count
        if cur % 2 == 0:
            cur /= 2
        else:
            cur = (cur * 3) + 1 
        count += 1
    new_sequence_cnts[n] = count
    add_new_sequences(new_sequence_cnts, count)


for r in range(1,1000000):
    colletz_cnt_from_int(r)

max_value = max(sequences.values())

for key,val in sequences.items():
    if val == max_value:
        print(key)
        break


    
    
