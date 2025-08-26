print("=== for文の練習 ===")

# 基本的なfor文

print('1. 数字の繰り返し')
for i in range(5):
    print(f'カウント:{i}')

print('\n2. リストの要素を繰り返し')
fruits = ['りんご', 'バナナ', 'オレンジ']
for fruit in fruits:
    print(f'果物:{fruit}')

print('\n3. 九九の表（一部）')
for i in range(1,10):
    for j in range(1,10):
        print(f'{i}*{j}={i*j}')
    print()

print('=== while文の練習')

# 基本的なwhile文
print('4. カウントダウン')
count = 5
while count > 0:
    print(f'残り:{count}秒')
    count -= 1
print('発射!')

# 条件を満たすまで繰り返し
print('\n5. 合計が100を超えるまで')
total = 1
number = 1
while total < 100:
    total += number
    print(f'{number}を追加: 合計 = {total}')
    number += 1

# リストと辞書の練習

print('=== リスト(List)の練習 ===')

# リストの作成と基本操作
numbers = [1, 2, 3, 4, 5]
print(f'リスト: {numbers}')
print(f'最初の要素：{numbers[0]}')
print(f'最後の要素：{numbers[-1]}')

# リストに要素を追加
numbers.append(6)
print(f'6を追加後: {numbers}')

# リストから要素を削除
numbers.remove(3)
print(f'3を削除後: {numbers}')

# リストの長さ
print(f'リストの長さ: {len(numbers)}')

print('\n=== 辞書(Dictionary)の練習 ===')

# 辞書の作成
student = {
    '名前': '田中太郎',
    '年齢': 20,
    '学年': 2,
    '専攻': '情報科学'
}

print(f'学生情報: {student}')
print(f'名前: {student['名前']}')
print(f'名前: {student['年齢']}')

# 辞書に新しいキーを追加
student['成績'] = 'A'

# 辞書のキー一覧
print(f'成績追加後: {list(student.keys())}')

print('\n=== 実践練習 ===')

# 学生リスト（辞書のリスト）
students = [
    {'名前': '佐藤花子', '数学': 85, '英語': 92},
    {'名前': '鈴木一郎', '数学': 78, '英語': 88},
    {'名前': '田中美咲', '数学': 95, '英語': 76}
]

print('学生の成績一覧:')
for student in students:
    avg = (student['数学'] + student['英語']) / 2
    print(f'{student['名前']}: 平均点{avg:.1f}')