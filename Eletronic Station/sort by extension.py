from typing import List
import collections


def sort_by_ext(files: List[str]) -> List[str]:
    my_dict = dict()

    for item in files:
        num, ext = item.split('.')

        my_dict[ext] = num

    # my_dict = {my_dict[elem[0]]:elem[1] for elem in sorted(my_dict.items())}

    return my_dict


if __name__ == '__main__':
    # print("Example:")
    # print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))