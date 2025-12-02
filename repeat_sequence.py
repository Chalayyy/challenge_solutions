"""
The problem: Find the sum of repeating patterns in ranges of values.
"""


def repeat_sequence(input):
    sets = input.split(',')
    sequence_sum = 0
    for set in sets:
        print("RANGE: ", set)
        start, end = set.split('-')
        # Only even-length digits can be composed of repeating sequences
        if len(start) % 2 == 1 and len(start) == len(end):
            continue
        # If the start is odd-length, we need to start at the next even-length number
        if len(start) % 2 == 1:
            start = "1"+"0"*len(start)
        # If the end is odd-length, we need to end at the previous even-length number
        if len(end) % 2 == 1:
            end = "9"*(len(end)-1)
        digit_length = len(start)
        starting_value = int(start[:digit_length//2])
        print("STARTING VALUE: ", starting_value)
        if starting_value < int(start[digit_length//2:]):
            starting_value += 1
        ending_value = int(end[:digit_length//2])
        if ending_value > int(end[digit_length//2:]):
            ending_value -= 1

        for i in range(starting_value, ending_value+1):
            print("ADDING: ", i * 10**(digit_length//2) + i)
            sequence_sum += i * 10**(digit_length//2) + i

    return sequence_sum

def repeat_sequence_2(input):
    sets = input.split(',')
    sequence_sum = 0

    sequences = []
    for set in sets:
        print("RANGE: ", set)
        start, end = set.split('-')
        for number in range(int(start), int(end)+1):
            if has_pattern(str(number)):
                sequences.append(number)
                sequence_sum += number
    return sequence_sum

def has_pattern(number):
    digit_length = len(number)
    if digit_length == 1:
        return False
    largest_segment = 1

    # find largest possible segment length
    for i in range(2, (digit_length//2) +1):
        if digit_length % i == 0:
            largest_segment = i

    # loop through number for each segment length
    for length in range(1, largest_segment + 1):
        if digit_length % length != 0:
            continue
        segment_count = digit_length//length
        segments = []
        for i in range(1, segment_count + 1):
            segments.append(number[(i-1)*length:i*length])
        if all(map(lambda x: x == number[:length], segments)):
            print("Segment Found: ", segments[0], number, digit_length, len(number))
            return True
    return False







print(repeat_sequence_2("3737332285-3737422568,5858547751-5858626020,166911-236630,15329757-15423690,753995-801224,1-20,2180484-2259220,24-47,73630108-73867501,4052222-4199117,9226851880-9226945212,7337-24735,555454-591466,7777695646-7777817695,1070-2489,81504542-81618752,2584-6199,8857860-8922218,979959461-980003045,49-128,109907-161935,53514821-53703445,362278-509285,151-286,625491-681593,7715704912-7715863357,29210-60779,3287787-3395869,501-921,979760-1021259"))
print(repeat_sequence_2("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"))
print(repeat_sequence_2("2121212118-2121212124"))