#!/usr/bin/env python3
"""
merge.py
用法:
    python merge.py file1.txt file2.txt merged.txt
把 file1.txt 和 file2.txt 顺序合并到 merged.txt
"""
import argparse
import sys

def merge_txt(src1, src2, dst):
    """把两个文本文件顺序写入新文件"""
    try:
        with open(dst, 'w', encoding='utf-8') as out_f, \
             open(src1, 'r', encoding='utf-8') as f1, \
             open(src2, 'r', encoding='utf-8') as f2:
            out_f.write(f1.read())
            # 如果希望两个文件之间换行，可改成 out_f.write(f1.read() + '\n')
            out_f.write(f2.read())
        print(f"已合并: {src1} + {src2} -> {dst}")
    except FileNotFoundError as e:
        print(f"文件不存在: {e.filename}", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"文件操作失败: {e}", file=sys.stderr)
        sys.exit(2)

def main(argv=None):
    parser = argparse.ArgumentParser(description="合并两个 TXT 文件")
    parser.add_argument("file1", help="第一个 TXT 文件")
    parser.add_argument("file2", help="第二个 TXT 文件")
    parser.add_argument("output", help="输出 TXT 文件")
    args = parser.parse_args(argv)
    merge_txt(args.file1, args.file2, args.output)

if __name__ == "__main__":
    main()