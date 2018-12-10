class NotSameLength(Exception):
    pass

def get_input(file):
    boxes = list()
    with open(file) as f:
        for line in f:
            boxes.append(line.replace('\n', ''))
    return boxes

def repetition_box_char(box):
    repetition_counter = dict()
    double_rep = False
    triple_rep = False

    for char in box:
        if (not bool(repetition_counter) or char not in repetition_counter):
            repetition_counter.update({char:int(1)})
        else:
            repetition_counter[char] += 1


    for char, value in repetition_counter.items():
        if ( value == 2 ):
            double_rep = True
        elif ( value == 3):
            triple_rep = True

    return [double_rep, triple_rep]

def checksum(boxes):
    repetition_counter = [0,0]

    for box in boxes:
        part_chksum = repetition_box_char(box)

        if part_chksum[0]:
            repetition_counter[0] += 1
        if part_chksum[1]:
            repetition_counter[1] += 1

    return repetition_counter[0] * repetition_counter[1]

def difference_string(str1, str2):
    count = 0
    if (len(str1) != len(str2)):
        raise(NotSameLength)
    for idx, char in enumerate(str1):
        if (str1[idx] != str2[idx]):
            count += 1

    if (count == 1):
        return True
    else:
        return False



def get_boxes(boxes):
    for idx, box in enumerate(boxes):
        for i in range(idx + 1,len(boxes)):
            if difference_string(box, boxes[i]):
                return [box, boxes[i]]

def common_letters(str1, str2):
    common = str()

    if (len(str1) != len(str2)):
        raise(NotSameLength)

    for idx, char in enumerate(str1):
        if (str1[idx] == str2[idx]):
            common += str1[idx]

    return common

def solving_the_day():
    str1, str2 = get_boxes(get_input('input.txt'))

    return common_letters(str1, str2)


print(solving_the_day())
