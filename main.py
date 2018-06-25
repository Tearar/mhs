import sys
from itertools import product


def return_observations_with_specific_sender(sender):
    for pair in observations:
        if sender in pair[0]:
            sender_observations.append(pair[1])


observations = []
sender_observations = []
sys.setrecursionlimit(20500)

data_file = open("observation_mix.txt", "r")
for line in data_file:
    removedcolon = line.replace(":", "").replace("  ", " ")
    value1, value2, value3, value4, value5, value6, value7, value8, value9 = removedcolon.split(" ")
    value1 = int(value1)
    value2 = int(value2)
    value3 = int(value3)
    value4 = int(value4)
    value5 = int(value5)
    value6 = int(value6)
    value7 = int(value7)
    value8 = int(value8)
    tuple1 = [value1, value2, value3, value4]
    tuple2 = [value5, value6, value7, value8]
    observation = (tuple1, tuple2)
    observations.append(observation)
data_file.close()

return_observations_with_specific_sender(1)
print(sender_observations)


def calculate_hitting_sets(tuples, sender_observations, counter, m):
    filtered_tuples = tuples
    new_tuples = []
    if counter < sender_observations.__len__():
        if filtered_tuples:
            for tuple1 in filtered_tuples:
                for value in sender_observations[counter]:
                    if value in tuple1:
                        new_tuples.append(tuple1)
            new_tuples = list(set(new_tuples))
            print(new_tuples)
            calculate_hitting_sets(new_tuples, sender_observations, counter + 1, m)

        else:
            print(m)
            test = []
            for i in range(m):
                filtered_tuples.append(sender_observations[i])
            filtered_tuples = [i for i in product(*filtered_tuples)]  # combines tupel dynamically
            #print(filtered_tuples)
            for i in filtered_tuples:
                i = sorted(i)
                i = tuple(i)
                test.append(i)
            #print(test)
            #print(list(set(test)))
            m = m + 1
            calculate_hitting_sets(test, sender_observations, counter, m)


calculate_hitting_sets([], sender_observations, 0, 1)
