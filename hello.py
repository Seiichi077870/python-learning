
print('Hello, Python!')
print('GitHubとPyCharmで学習開始!')

name = 'Python学習者'
print(f'こんにちは、{name}さん!')

a = 10
b = 5

print(f"{a} + {b} = {a + b}")
print(f'{a} * {b} = {a * b}')

age = 15
if age >= 18:
    print('成人です')
else:
    print('未成年です')

score = 90
if score >= 90:
    print('優秀！')
elif score >= 70:
    print('良好')
elif score >= 60:
    print('合格')
else:
    print('不合格')

print('\n--- 数当てゲーム ---')
secret_number = 7
guess = int(input('1から10の数字を入力してください: '))
if guess == secret_number:
    print('正解!')
elif guess < secret_number:
    print('もっと大きい数字です')
else:
    print('もっと小さい数字です')


