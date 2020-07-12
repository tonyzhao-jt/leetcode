class Solution:
    def maximumSwap(self, num: int) -> int:
        str_num = str(num)
        str_num_list = list(str_num)

        map_index = [0] * 10
        for idx, num in enumerate(str_num_list):
            map_index[int(num)] = idx
        for idx, num in enumerate(str_num_list):
            for j in range(9, int(num), -1):
                j_idx = map_index[j]
                if j_idx > idx:
                    str_num_list[idx], str_num_list[j_idx] = str_num_list[j_idx], str_num_list[idx]
                    return ''.join(str_num_list)
        return str_num