def solution(marks):
    ### Enter your solution below this line
    ### Indent your entire code by one unit (4 spaces) to the right
# we are following the obvious sort
    sorted_marks = [ ]  # list to store the sorted marks
    while marks != [ ]:
        min_mark = marks[0]
        for mark in marks:
            if mark < min_mark:
                min_mark = mark
        marks.remove(min_mark)
        sorted_marks.append(min_mark)

    n = len(sorted_marks)
    # if n is odd, the middle element is the median
    if n % 2 != 0:
        mid = n // 2
        median = sorted_marks[mid]
    # if n is even, get the arithmetic mean of the two middle elements
    else:
        mid2 = n // 2
        mid1 = mid2 - 1
        median = (sorted_marks[mid1] + sorted_marks[mid2]) / 2
### Enter your solution above this line
    return median
marks_input = input()

# Extracting numeric values from the input string
marks = [float(mark.strip()) for mark in marks_input.split(',') if mark.strip().isdigit()]


result = solution(marks)
print(result)