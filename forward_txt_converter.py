import re
import sys

def forward_to_txt(in_path, out_path):
    curves = []
    data_started = False

    with open(in_path, 'r', encoding='utf-8', errors='ignore') as fin, \
         open(out_path, 'w', encoding='utf-8', newline='') as fout:

        for line in fin:
            s = line.strip()
            if not s:
                continue

            # 解析 CURVENAME = AC, ANHY, ...
            if s.startswith('CURVENAME'):
                m = re.match(r'CURVENAME\s*=\s*(.*)', s)
                if m:
                    curves = [c.strip() for c in m.group(1).split(',') if c.strip()]
                continue

            # 数据列名行，例如：#DEPTH  AC  ANHY ...
            if s.startswith('#DEPTH') or s.startswith('DEPTH'):
                parts = s.split()
                if parts[0].upper() in ('#DEPTH', 'DEPTH'):
                    header = ['DEPTH'] + parts[1:]
                else:
                    header = ['DEPTH'] + curves
                fout.write('\t'.join(header) + '\n')
                data_started = True
                continue

            # 数据区
            if data_started:
                if s.upper() == 'END':
                    continue
                vals = s.split()
                fout.write('\t'.join(vals) + '\n')


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        in_file = sys.argv[1]
        out_file = sys.argv[2]
    else:
        # 如果没传参数，就改这里
        in_file = 'C:/Users/Lenovo/Downloads/真604斜井测井成果曲线数据体 (2).txt'
        out_file = 'C:/Users/Lenovo/Downloads/真604斜井测井成果曲线_output.txt'

    forward_to_txt(in_file, out_file)
    print(f'转换完成：{in_file} -> {out_file}')
