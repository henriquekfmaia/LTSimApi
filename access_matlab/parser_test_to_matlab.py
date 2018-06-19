import matlab.engine
import variable_parser as parser
import matlab_handler as mlh

int_mock = int(1)
float_mock = float(1.1)
list_mock_1 = [int(1), int(2), int(3), int(4), int(5)]
list_mock_2 = [float(1.1), float(2.1), float(3.1), float(4.1), float(5.1)]
list_mock_3 = [int(1), float(2.1), int(3), float(4.1), int(5)]
list_list_mock_1 = [[int(1), int(2), int(3), int(4), int(5)], [int(1), float(2.1), int(3), float(4.1), int(5)]]
list_list_mock_2 = [[int(1), int(2), int(3), int(4), int(5)], [[int(1), float(2.1), int(3), float(4.1), int(5)], [9, 8, 7, 6, 5]]]

list_list_mock_3 = [ [9, 8], [[1, 1, 2, 1], [2, 2, 3, 1], [3, 0, 1, 1], [4, 3, 0, 1]] ]

ciclor_mock_1 = [[1, 1, 2, 1], [2, 2, 3, 1], [3, 0, 1, 1], [4, 3, 0, 1]]
ciclor_mock_2 = [[1, 1, 2, 1], [2, 2, 3, 1], [3, 0, 1, 1], [4, 3, 0, 1], [5, 3, 2, 1], [5, 0, 2, 1]]

live_test = [[1, 2, [1, 2, 3]], [9, 8, [7, 7, 7], 6]]

def run_test_mock(mock):
    matlab_input = parser.convert_to_matlab_cells(mock)
    # print(matlab_input)
    matlab_result = mlh.run_test_code(matlab_input)
    # print(matlab_result)
    ret = parser.force_list(matlab_result)
    print(ret)

def run_test_ciclor_mock(ciclor_mock):
    matlab_input = parser.convert_to_matlab_mat(ciclor_mock)
    # print(matlab_input)
    matlab_result = mlh.run_ciclor(matlab_input)
    # print(matlab_result)
    ret = parser.force_list(matlab_result)
    print(ret)

# run_test_mock(int_mock)
# run_test_mock(float_mock)
# run_test_mock(list_mock_1)
# run_test_mock(list_mock_2)
# run_test_mock(list_mock_3)
# run_test_mock(list_list_mock_1)
# run_test_mock(list_list_mock_2)
# run_test_mock(list_list_mock_3)
run_test_mock(live_test)

# run_test_ciclor_mock(ciclor_mock_1)
# run_test_ciclor_mock(ciclor_mock_2)