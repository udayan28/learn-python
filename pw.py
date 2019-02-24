#! python3
# pw.py - パスワード管理プログラム（脆弱性あり）

PASSWORDS = {
    'email': 'dfdsa943jgkflabhgtsjgfkl89o',
    'blog': 'fdsajk;fjdskaljfij3ieo23jkk54jekljfk',
    'luggage': '12345'
}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方：python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをクリップボードにコピーしました')
else:
    print(account + 'というアカウント名はありません')
    