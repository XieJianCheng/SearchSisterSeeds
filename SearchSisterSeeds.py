# coding: utf-8

# 读配置
with open('option.ini', 'r', encoding='utf-8') as fo_r_option:
    options = fo_r_option.readlines()
    input_file = options[0][11:-1]
    output_file = options[1][12:]


searching_int = int(input('enter primary seed:'))    # 输入原种子


def get_hex(primary_seed):  # 参数是int
    seed_bin = int(bin(primary_seed & 0xffffffffffffffff), 2)   # 补码对正数没有影响
    processing_hex = hex(seed_bin)[2:]        # 获得十六进制数
    excised_hex = processing_hex[-12:]      # 因为只有后12个数字影响结构所以
    return excised_hex


# 遍历文件，找到相同的结构码，因为没法通过遍历地形码筛
with open(input_file, 'r', encoding='utf-8') as fo_r:
    file_content_list = fo_r.readlines()

searching_hex = get_hex(searching_int)      # 要筛的原种
print(f"primary seed's structure:{searching_hex}")
# 遍历数据
searched_list = []
search_times = 0
for i in file_content_list:
    now_seed_str = i.split(' ')[0]
    now_seed_int = int(not_seed_str)
    seed_hex = get_hex(now_seed_int)
    if seed_hex == searching_hex:
        search_times += 1
        print(f'{search_times}:{now_seed_str} {seed_hex}')
        searched_list.append(now_seed_str)
print(f'number of seeds:{search_times}')

# 输出文件
searched_str = ''
for j in searched_list:
    searched_str += f'{j}\n'
with open(output_file, 'w+', encoding='utf-8') as fo_w:
    fo_w.write(searched_str)
    print('save file succeeded')
input('enter to exit.')
