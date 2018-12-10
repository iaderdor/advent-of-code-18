def get_frequency_changes(file):
    frequency_change = list()
    with open(file) as f:
        for line in f:
            frequency_change.append(int(line))
    return frequency_change

def calculate_total_frequency(frequency_change_list):
    frequency = 0
    for frequency_change in frequency_change_list:
        frequency += frequency_change
    return frequency

def get_first_twice_frequency(frequency_change_list):
    frequency_list = list()

    count = 0
    while ( True ):
        for idx_freq_chg, frequency_change in enumerate(frequency_change_list):
            if (count == 0 and idx_freq_chg == 0):
                frequency_list.append(frequency_change)
            else:
                frequency_list.append(frequency_list[-1] + frequency_change)

            if (len(frequency_list) > 1):
                for idx_freq, frequency in enumerate(frequency_list):
                    #print(f'Last freq: {frequency_list[-1]} freq:{frequency}')
                    if ( frequency_list[-1] == frequency and idx_freq != len(frequency_list) - 1):
                        return frequency_list
        count += 1
        print(count)

def get_first_twice_frequency_dict(frequency_change_list):
    frequency_list = dict()
    frequency = 0

    count = 0
    while ( True ):
        for frequency_change in frequency_change_list:
            frequency += frequency_change
            if ( not bool(frequency_list) ):
                frequency_list.update({frequency:1})
            elif ( frequency in frequency_list ):
                return frequency
            else:
                frequency_list.update({frequency:1})
print(get_first_twice_frequency_dict(get_frequency_changes('input.txt')))
