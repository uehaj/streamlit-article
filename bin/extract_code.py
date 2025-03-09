#!env python3
#
# python3 ../bin/extract_code.py mokujian.md && for i in *.py; do diff -c $i src/$i; done

import re
import sys

def extract_python_blocks(md_file):
  with open(md_file, 'r', encoding='utf-8') as f:
    content = f.read()

  # Pythonコードブロックの正規表現
  pattern = re.compile(r'```python\n(.*?)\n```', re.DOTALL)

  matches = pattern.findall(content)

  for match in matches:
    lines = match.split('\n')
    if len(lines) < 2 or not lines[0].startswith('# '):
      line_number = content[:content.find(match)].count('\n') + 1
      context_lines = content.split('\n')[line_number - 2:line_number + 3]
      context = '\n'.join([f"{md_file}:{i+1}: {line}" for i,
                          line in enumerate(context_lines, start=line_number - 2)])
      print(
        f"\033[94m警告: コードブロックの最初の行に'# filename.py'の形式のコメントがありません。ファイル出力をスキップします。\033[0m")
      print(f"\033[93m{context}\033[0m")
      continue

    filename = lines[0][2:].strip()
    if not filename.endswith('.py'):
      print(
        f"\033[94m警告: '{filename}' は有効なPythonファイル名ではありません。ファイル出力をスキップします。\033[0m")
      continue

    code_to_write = '\n'.join(lines) + '\n'

    with open(filename, 'w', encoding='utf-8') as f:
      f.write(code_to_write)
    print(f"'{filename}' にコードを書き出しました。")

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("使用方法: python script.py input.md")
  else:
    extract_python_blocks(sys.argv[1])
