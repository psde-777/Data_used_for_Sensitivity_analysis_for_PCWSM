import os

def find_closest_timepoint(timepoints, target):
    closest = min(timepoints, key=lambda x: abs(x-target))
    return closest
target_time = 8.4
threshold = 50.2
N = 21504

for i in range(1,N):
    folder_path = 'family_1/Generation_1/Run_%d/Output/saccharification/' % i
    input_file = 'saccharification_high_1.txt'
    input_path = os.path.join(folder_path, input_file)

    timepoints = []
    values = []
    with open(input_path, 'r') as file:
        for line in file:
            columns = line.split()
            timepoints.append(float(columns[0]))
            values.append(float(columns[1]))

    closest_time = find_closest_timepoint(timepoints, target_time)
    index = timepoints.index (closest_time)
    closest_value = values[index]
#    print(index)

    if closest_value > threshold:
        output_value = '1'
    else:
        output_value = '0'

#    print(output_value)
    with open('above_or_below.txt', 'a') as file2:
        file2.write(str(output_value + '\n'))
