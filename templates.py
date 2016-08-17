#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Скрипт предварительной обработки текста для
# синтезатора речи RHVoice Ольги Яковлевой
# By Capricorn2001

from re import sub, findall

im_muzh = (
  (
    (
      (
        'нулевой',
        'тысячный',
        'двухтысячный',
        'трёхтысячный',
        'четырёхтысячный',
        'пятитысячный',
        'шеститысячный',
        'семитысячный',
        'восьмитысячный',
        'девятитысячный'
      ),
      'сотый',
      'двухсотый',
      'трёхсотый',
      'четырёхсотый',
      'пятисотый',
      'шестисотый',
      'семисотый',
      'восьмисотый',
      'девятисотый'
    ),
    'десятый',
    'двадцатый',
    'тридцатый',
    'сороковой',
    'пятидесятый',
    'шестидесятый',
    'семидесятый',
    'восьмидесятый', 
    'девяностый'
  ),
  ('первый', 'одиннадцатый'),
  ('второй', 'двенадцатый'),
  ('третий', 'тринадцатый'),
  ('четвёртый', 'четырнадцатый'),
  ('пятый', 'пятнадцатый'),
  ('шестой', 'шестнадцатый'),
  ('седьмой', 'семнадцатый'),
  ('восьмой', 'восемнадцатый'),
  ('девятый', 'девятнадцатый')
)
im_sred = (
  (
    (
      (
        'нулевое',
        'тысячное',
        'двухтысячное',
        'трёхтысячное',
        'четырёхтысячное',
        'пятитысячное',
        'шеститысячное',
        'семитысячное',
        'восьмитысячное',
        'девятитысячное'
      ),
      'сотое',
      'двухсотое',
      'трёхсотое',
      'четырёхсотое',
      'пятисотое',
      'шестисотое',
      'семисотое',
      'восьмисотое',
      'девятисотое'
    ),
    'десятое',
    'двадцатое',
    'тридцатое',
    'сороковой',
    'пятидесятое',
    'шестидесятое',
    'семидесятое',
    'восьмидесятое', 
    'девяностое'
  ),
  ('первое', 'одиннадцатое'),
  ('второе', 'двенадцатое'),
  ('третье', 'тринадцатое'),
  ('четвёртое', 'четырнадцатое'),
  ('пятое', 'пятнадцатое'),
  ('шестое', 'шестнадцатое'),
  ('седьмое', 'семнадцатое'),
  ('восьмое', 'восемнадцатое'),
  ('девятое', 'девятнадцатое')
)
im_zhen = (
  (
    (
      (
        'нулевая',
        'тысячная',
        'двухтысячная',
        'трёхтысячная',
        'четырёхтысячная',
        'пятитысячная',
        'шеститысячная',
        'семитысячная',
        'восьмитысячная',
        'девятитысячная'
      ),
      'сотая',
      'двухсотая',
      'трёхсотая',
      'четырёхсотая',
      'пятисотая',
      'шестисотая',
      'семисотая',
      'восьмисотая',
      'девятисотая'
    ),
    'десятая',
    'двадцатая',
    'тридцатая',
    'сороковой',
    'пятидесятая',
    'шестидесятая',
    'семидесятая',
    'восьмидесятая', 
    'девяностая'
  ),
  ('первая', 'одиннадцатая'),
  ('вторая', 'двенадцатая'),
  ('третья', 'тринадцатая'),
  ('четвёртая', 'четырнадцатая'),
  ('пятая', 'пятнадцатая'),
  ('шестая', 'шестнадцатая'),
  ('седьмая', 'семнадцатая'),
  ('восьмая', 'восемнадцатая'),
  ('девятая', 'девятнадцатая')
)
im_mnozh = (
  (
    (
      (
        'нулевые',
        'тысячные',
        'двухтысячные',
        'трёхтысячные',
        'четырёхтысячные',
        'пятитысячные',
        'шеститысячные',
        'семитысячные',
        'восьмитысячные',
        'девятитысячные'
      ),
      'сотые',
      'двухсотые',
      'трёхсотые',
      'четырёхсотые',
      'пятисотые',
      'шестисотые',
      'семисотые',
      'восьмисотые',
      'девятисотые'
    ),
    'десятые',
    'двадцатые',
    'тридцатые',
    'сороковые',
    'пятидесятые',
    'шестидесятые',
    'семидесятые',
    'восьмидесятые',
    'девяностые'
  ),
  ('первые', 'одиннадцатые'),
  ('вторые', 'двенадцатые'),
  ('третьи', 'тринадцатые'),
  ('сороковые', 'четырнадцатые'),
  ('пятые', 'пятнадцатые'),
  ('шестые', 'шестнадцатые'),
  ('седьмые', 'семнадцатые'),
  ('восьмые', 'восемнадцатые'),
  ('девятые' 'девятнадцаые')
)
ro_muzh = (
  (
    (
      (
        'нулевого',
        'тысячного',
        'двухтысячного',
        'трёхтысячного',
        'четырёхтысячного',
        'пятитысячного',
        'шеститысячного',
        'семитысячного',
        'восьмитысячного',
        'девятитысячного'
      ),
      'сотого',
      'двухсотого',
      'трёхсотого',
      'четырёхсотого',
      'пятисотого',
      'шестисотого',
      'семисотого',
      'восьмисотого',
      'девятисотого'
    ),
    'десятого',
    'двадцатого',
    'тридцатого',
    'сорокового',
    'пятидесятого',
    'шестидесятого',
    'семидесятого',
    'восьмидесятого', 
    'девяностого'
  ),
  ('первого', 'одиннадцатого'),
  ('второго', 'двенадцатого'),
  ('третьего', 'тринадцатого'),
  ('четвёртого', 'четырнадцатого'),
  ('пятого', 'пятнадцатого'),
  ('шестого', 'шестнадцатого'),
  ('седьмого', 'семнадцатого'),
  ('восьмого', 'восемнадцатого'),
  ('девятого', 'девятнадцатого')
)
ro_zhen = (
  (
    (
      (
        'нулевую',
        'тысячную',
        'двухтысячную',
        'трёхтысячную',
        'четырёхтысячную',
        'пятитысячную',
        'шеститысячную',
        'семитысячную',
        'восьмитысячную',
        'девятитысячную'
      ),
      'сотую',
      'двухсотую',
      'трёхсотую',
      'четырёхсотую',
      'пятисотую',
      'шестисотую',
      'семисотую',
      'восьмисотую',
      'девятисотую'
    ),
    'десятую',
    'двадцатую',
    'тридцатую',
    'сороковую',
    'пятидесятую',
    'шестидесятую',
    'семидесятую',
    'восьмидесятую', 
    'девяностую'
  ),
  ('первую', 'одиннадцатую'),
  ('вторую', 'двенадцатую'),
  ('третью', 'тринадцатую'),
  ('четвёртую', 'четырнадцатую'),
  ('пятую', 'пятнадцатую'),
  ('шестую', 'шестнадцатую'),
  ('седьмую', 'семнадцатую'),
  ('восьмую', 'восемнадцатую'),
  ('девятую', 'девятнадцатую')
)
ro_mnozh = (
  (
    (
      (
        'нулевых',
        'тысячных',
        'двухтысячных',
        'трёхтысячных',
        'четырёхтысячных',
        'пятитысячных',
        'шеститысячных',
        'семитысячных',
        'восьмитысячных',
        'девятитысячных'
      ),
      'сотых',
      'двухсотых',
      'трёхсотых',
      'четырёхсотых',
      'пятисотых',
      'шестисотых',
      'семисотых',
      'восьмисотых',
      'девятисотых'
    ),
    'десятых',
    'двадцатых',
    'тридцатых',
    'сороковых',
    'пятидесятых',
    'шестидесятых',
    'семидесятых',
    'восьмидесятых',
    'девяностых'
  ),
  ('первых', 'одиннадцатых'),
  ('вторых', 'двенадцатых'),
  ('третьих', 'тринадцатых'),
  ('сороковых', 'четырнадцатых'),
  ('пятых', 'пятнадцатых'),
  ('шестых', 'шестнадцатых'),
  ('седьмых', 'семнадцатых'),
  ('восьмых', 'восемнадцатых'),
  ('девятых' 'девятнадцатых')
)
da_muzh = (
  (
    (
      (
        'нулевому',
        'тысячному',
        'двухтысячному',
        'трёхтысячному',
        'четырёхтысячному',
        'пятитысячному',
        'шеститысячному',
        'семитысячному',
        'восьмитысячному',
        'девятитысячному'
      ),
      'сотому',
      'двухсотому',
      'трёхсотому',
      'четырёхсотому',
      'пятисотому',
      'шестисотому',
      'семисотому',
      'восьмисотому',
      'девятисотому'
    ),
    'десятому',
    'двадцатому',
    'тридцатому',
    'сороковому',
    'пятидесятому',
    'шестидесятому',
    'семидесятому',
    'восьмидесятому', 
    'девяностому'
  ),
  ('первому', 'одиннадцатому'),
  ('второму', 'двенадцатому'),
  ('третьему', 'тринадцатому'),
  ('четвёртому', 'четырнадцатому'),
  ('пятому', 'пятнадцатому'),
  ('шестому', 'шестнадцатому'),
  ('седьмому', 'семнадцатому'),
  ('восьмому', 'восемнадцатому'),
  ('девятому', 'девятнадцатому')
)
da_zhen = (
  (
    (
      (
      'нулевой',
      'тысячной',
      'двухтысячной',
      'трёхтысячной',
      'четырёхтысячной',
      'пятитысячной',
      'шеститысячной',
      'семитысячной',
      'восьмитысячной',
      'девятитысячной'
      ),
      'сотой',
      'двухсотой',
      'трёхсотой',
      'четырёхсотой',
      'пятисотой',
      'шестисотой',
      'семисотой',
      'восьмисотой',
      'девятисотой'
    ),
    'десятой',
    'двадцатой',
    'тридцатой',
    'сороковой',
    'пятидесятой',
    'шестидесятой',
    'семидесятой',
    'восьмидесятой', 
    'девяностой'
  ),
  ('первой', 'одиннадцатой'),
  ('второй', 'двенадцатой'),
  ('третью', 'тринадцатой'),
  ('четвёртой', 'четырнадцатой'),
  ('пятой', 'пятнадцатой'),
  ('шестой', 'шестнадцатой'),
  ('седьмой', 'семнадцатой'),
  ('восьмой', 'восемнадцатой'),
  ('девятой', 'девятнадцатой')
)
tv_muzh = (
  (
    (
      (
        'нулевым',
        'тысячным',
        'двухтысячным',
        'трёхтысячным',
        'четырёхтысячным',
        'пятитысячным',
        'шеститысячным',
        'семитысячным',
        'восьмитысячным',
        'девятитысячным'
      ),
      'сотым',
      'двухсотым',
      'трёхсотым',
      'четырёхсотым',
      'пятисотым',
      'шестисотым',
      'семисотым',
      'восьмисотым',
      'девятисотым'
    ),
    'десятым',
    'двадцатым',
    'тридцатым',
    'сороковым',
    'пятидесятым',
    'шестидесятым',
    'семидесятым',
    'восьмидесятым', 
    'девяностым'
  ),
  ('первым', 'одиннадцатым'),
  ('вторым', 'двенадцатым'),
  ('третьим', 'тринадцатым'),
  ('четвёртым', 'четырнадцатым'),
  ('пятым', 'пятнадцатым'),
  ('шестым', 'шестнадцатым'),
  ('седьмым', 'семнадцатым'),
  ('восьмым', 'восемнадцатым'),
  ('девятым', 'девятнадцатым')
)
tv_mnozh = (
  (
    (
      (
        'нулевыми',
        'тысячными',
        'двухтысячными',
        'трёхтысячными',
        'четырёхтысячными',
        'пятитысячными',
        'шеститысячными',
        'семитысячными',
        'восьмитысячными',
        'девятитысячными'
      ),
      'сотыми',
      'двухсотыми',
      'трёхсотыми',
      'четырёхсотыми',
      'пятисотыми',
      'шестисотыми',
      'семисотыми',
      'восьмисотыми',
      'девятисотыми'
    ),
    'десятыми',
    'двадцатыми',
    'тридцатыми',
    'сороковыми',
    'пятидесятыми',
    'шестидесятыми',
    'семидесятыми',
    'восьмидесятыми',
    'девяностыми'
  ),
  ('первыми', 'одиннадцатым'),
  ('вторыми', 'двенадцатым'),
  ('третьими', 'тринадцатым'),
  ('сороковыми', 'четырнадцатым'),
  ('пятыми', 'пятнадцатым'),
  ('шестыми', 'шестнадцатым'),
  ('седьмым', 'семнадцатым'),
  ('восьмыми', 'восемнадцатым'),
  ('девятыми' 'девятнадцатым')
)
pr_muzh = (
  (
    (
      (
        'нулевом',
        'тысячном',
        'двухтысячном',
        'трёхтысячном',
        'четырёхтысячном',
        'пятитысячном',
        'шеститысячном',
        'семитысячном',
        'восьмитысячном',
        'девятитысячном'
      ),
      'сотом',
      'двухсотом',
      'трёхсотом',
      'четырёхсотом',
      'пятисотом',
      'шестисотом',
      'семисотом',
      'восьмисотом',
      'девятисотом'
    ),
    'десятом',
    'двадцатом',
    'тридцатом',
    'сороковом',
    'пятидесятом',
    'шестидесятом',
    'семидесятом',
    'восьмидесятом', 
    'девяностом'
  ),
  ('первом', 'одиннадцатом'),
  ('втором', 'двенадцатом'),
  ('третьем', 'тринадцатом'),
  ('четвёртом', 'четырнадцатом'),
  ('пятом', 'пятнадцатом'),
  ('шестом', 'шестнадцатом'),
  ('седьмом', 'семнадцатом'),
  ('восьмом', 'восемнадцатом'),
  ('девятом', 'девятнадцатом')
)
ro_sred = ro_muzh
da_sred = da_muzh
da_mnozh = tv_muzh
vi_muzh = None
vi_sred = None
vi_zhen = ro_zhen
vi_mnozh = None
tv_sred = tv_muzh
tv_zhen = ro_zhen
pr_sred = pr_muzh
pr_zhen = ro_zhen
pr_mnozh = ro_mnozh
ordinales = (
    (im_muzh, im_sred, im_zhen, im_mnozh),
    (ro_muzh, ro_sred, ro_zhen, ro_mnozh),
    (da_muzh, da_sred, da_zhen, da_mnozh),
    (tv_muzh, tv_sred, tv_zhen, tv_mnozh),
    (vi_muzh, vi_sred, vi_zhen, vi_mnozh),
    (pr_muzh, pr_sred, pr_zhen, pr_mnozh)
)

def ordinal(num, casus, genum):
    if num[-1] == '0':
        try:
            if num[-2] == '0':
                if num[-3] == '0':
                    prenum = ''
                    number = ordinales[casus][genum][0][0][0][int(num[-4])]
                else:
                    if len(num) == 3:
                        prenum = ''
                    else:
                        prenum = num[:-3] + '000 '
                    number = ordinales[casus][genum][0][0][int(num[-3])]
            else:
                if len(num) == 2:
                    prenum = ''
                else:
                    prenum = num[:-2]
                    if int(prenum) == 0:
                        prenum += ' '
                    else:
                        prenum += '00 '
                number = ordinales[casus][genum][0][int(num[-2])]
        except:
            prenum = ''
            number = ordinales[casus][genum][0][0][0][0]
    else:
        if len(num) == 1:
            prenum = ''
            dec = 0
        else:
            if num[-2] == '1':
                dec = 1
                if len(num) == 2:
                    prenum = ''
                else:
                    prenum = num[:-2]
                    if int(prenum) == 0:
                        prenum += ' '
                    else:
                        prenum += '00 '
            else:
                prenum = num[:-1]
                if int(prenum) == 0:
                    prenum += ' '
                else:
                    prenum += '0 '
                dec = 0
        number = ordinales[casus][genum][int(num[-1])][dec]
    return prenum + number

# Код заимствован (с изменениями) у Jeff Wheeler
values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
def roman2arabic(value):
    total = 0
    prevValue = 0
    value = value[::-1]
    for char in value:
        if values[char] >= prevValue:
            total += values[char]
        else:
            total -= values[char]
        prevValue = values[char]
    total = str(total)
    return total

forms = {
    '%': ('процент', 'процента', 'процентов', 'процента'),
    '°': ('градус', 'градуса', 'градусов', 'градуса'),
    '℃': ('градус Цельсия', 'градуса Цельсия', 'градусов Цельсия', 'градуса Цельсия'),
    '$': ('доллар', 'доллара', 'долларов', 'доллара'),
    'кг': ('килограмм', 'килограмма', 'килограммов', 'килограмма'),
    'км': ('километр', 'километра', 'километров', 'километра'),
    'мг': ('миллиграмм', 'миллиграмма', 'миллиграммов', 'миллиграмма'),
    'мм': ('миллиметр', 'миллиметра', 'миллиметров', 'миллиметра'),
    'см': ('сантиметр', 'сантиметра', 'сантиметров', 'сантиметра'),
    'м': ('метр', 'метра', 'метров', 'метра'),
    'т': ('тонна', 'тонны', 'тонн', 'тонны'),
    'кВт': ('киловатт', 'киловатта', 'киловатт', 'киловатта'),
    'МВт': ('мегаватт', 'мегаватта', 'мегаватт', 'мегаватта'),
    'ГВт': ('мегаватт', 'мегаватта', 'мегаватт', 'мегаватта'),
    'Вт': ('ватт', 'ватта', 'ватт', 'ватта'),
    '₽': ('рубль', 'рубля', 'рублей', 'рубля'),
    '£': ('фунт стерлингов', 'фунта стерлингов', 'фунтов стерлингов', 'фунта стерлингов'),
    'л\u002Eс\u002E': ('лошадиная сила', 'лошадиные силы', 'лошадиных сил', 'лошадиной силы'),
    'тыс\u002E': ('тысяча', 'тысячи', 'тысяч', 'тысячи'),
    'млн': ('миллион', 'миллиона', 'миллионов', 'миллиона'),
    'млрд': ('миллиард', 'миллиарда', 'миллиардв', 'миллиарда'),
    'трлн': ('триллион', 'триллиона', 'триллионов', 'триллиона')
}
def substant(num, key):
    if len(num) > 1 and num[-2] == '1':
        form = forms[key][2]
    else:
        if num[-1] =='1':
            form = forms[key][0]
        elif 1 < int(num[-1]) < 5:
            form = forms[key][1]
        else:
            form = forms[key][2]
    return form

def feminin(num):
    num = str(int(num))
    if len(num) == 1:
        if num == '1':
            num = 'одна'
        elif num == '2':
            num = 'две'
    else:
        if num[-2] != '1':
            if num[-1] == '1':
                num = num[:-1] + '0 одна'
            elif num[-1] == '2':
                num = num[:-1] + '0 две'
    return num

file = open('/tmp/clip.txt', 'r')
text = file.read()
file.close()

##  ШАБЛОНЫ  ##

text = sub(r'\+ ?', 'плюс ', text)
text = sub(r'(?<!\w)-(?=\d)', 'минус ', text)
text = sub(r'[ \t]{2,}', ' ', text)
text = sub(r' +(\n|\Z)', r'\1', text)
text = sub(r'\n{2,}', r'\n', text)
text = sub(r'[«»"]', '', text)
text = sub(r'[‑–−—]', '-', text)

text = sub('№ ?', 'номер ', text)
text = sub('[Тт]\. ?е\.', 'то есть', text)
text = sub('т\. ?д\.', 'так далее', text)
text = sub('т\. ?п\.', 'тому подобное', text)

text = sub(r'\b([Гг])-(н|на|не|ном|ну)\b', r'\1осподи\2', text)
text = sub(r'\b([Гг])-(жа|же|жи|жой|жу)\b', r'\1оспо\2', text)

# Единицы измерения и денежные единицы

text = sub(r'\bруб\.', '₽', text)
text = sub(r'(\$|€|£|₽)([0-9,]+)', r'\2\1', text)
text = sub(r'(\$|€|£|₽) ?(тыс\.|млн|млрд|трлн|тысяч[аи]?|миллион[аов]{,2}|миллиард[аов]{,2}|триллион[аов]{,2})', r' \2 \1', text)
text = sub(' ?€', ' евро', text)

units = r'(%|°|℃|£|₽|\$|кг|км|мг|мм|м\b|см\b|т\b|кВт|МВт|ГВт|Вт|л\u002Eс\u002E|тыс\u002E|млн|млрд|трлн)'
text = sub(r'(?<=\d) ?' + units,  r'\1', text)

samples = findall(r'(\d+,\d+)' + units, text)
for sample in samples:
    text = text.replace(sample[0] + sample[1], sample[0] + ' ' + forms[sample[1]][3], 1)
samples = findall(r'(\d+)' + units, text)
for sample in samples:
    text = text.replace(sample[0] + sample[1], sample[0] + ' ' + substant(sample[0], sample[1]), 1)
samples = findall(r'(тысяч[аи]?|миллион[аов]{,2}|миллиард[аов]{,2}|триллион[аов]{,2}) ?' + units, text)
for sample in samples:
    text = text.replace(sample[0] + ' ' + sample[1], sample[0] + ' ' + forms[sample[1]][2], 1)

text = sub(r'/(сек|с)\b', r' в секунду', text)
text = sub(r'/(час|ч)\b', r' в час', text)

# Удаление пробелов между разрядами /только целая часть числа/
text = sub(r'(?<=\d) (?=\d{3})', r'', text)

# Десятичные дроби (до тысячных включительно)
samples = findall(r'(\d+,)(\d{1,3})\b', text)
for sample in samples:
    length = len(sample[1])
    full = feminin(sample[0][0:-1])
    if full[-1] == 'а':
        full += ' целая '
    else:
        full += ' целых '
    if length == 1:
        frac = ' десят'
    elif length == 2:
        frac = ' сот'
    else:
        frac = ' тысячн'
    decimal = feminin(sample[1])
    if decimal[-1] == 'а':
        frac += 'ая'
    else:
        frac += 'ых'
    text = text.replace(sample[0] + sample[1],  full + decimal + frac, 1)

# Проверка должна следовать после обработки десятичных дробей
samples = findall(r'(\d+) (минут[аы]?|недел[иья]|секунд[аы]?|тонн[аы]|тысяч[аи]?|лошадин[аеыя]{2} сил[аы]?)\b', text)
for sample in samples:
    text = text.replace(sample[0] + ' ' + sample[1], feminin(sample[0]) + ' ' + sample[1], 1)

# Римские цифры
roman = findall(r'\b[IVXLCDM]+\b', text)
for i in roman:
    text = text.replace(i, roman2arabic(i), 1)

text = sub(r'(\d)( ранга)\b', r'\1-го\2', text)
text = sub(r'(\d+)( Олимпийски)([еимх]{1,2})', r'\1-\3\2\3', text)

# Даты

text = sub(r'(январ[еюьям]{1,2}|феврал[еюьям]{1,2}|март[аеуом]{0,2}|апрел[еюьям]{1,2}|ма[йюяем]{1,2}|июн[еюьям]{1,2}|июл[еюьям]{1,2}|август[аеуом]{0,2}|сентябр[еюьям]{1,2}|октябр[еюьям]{1,2}|ноябр[еюьям]{1,2}|декабр[еюьям]{1,2}|начал[аеому]{1,2}|середин[аеойуы]{1,2}|кон[ецауом]{2,3}|половин[аеуыой]{1,2}|лет[ауом]{1,2}|весн[аеуыой]{1,2}|осен[иью]{1,2})( \d+) (года\b|г\.)', r'\1\2-го года', text)

text = sub(r'([Пп]еред \d+) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)', r'\1-м \2', text)

text = sub(r'\b([Зз]а|[Нн]а|[Пп]о)( \d+) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)', r'\1\2-е \3', text)
text = sub(r'\b([Дд]о|[Пп]осле|[Сс]о?)( \d+) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)', r'\1\2-го \3', text)
text = sub(r'\b([Кк]о?)( \d+) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)', r'\1\2-му \3', text)
text = sub(r'(\d+) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)', r'\1-го \2', text)

text = sub(r'(начал[аеому]{1,2}|середин[аеойуы]{1,2}|кон[ецауом]{2,3}|половин[аеуыой]{1,2})( \d+) гг\.', r'\1\2-х годов', text)

text = sub(r'(ноч[иь] со? \d+)( на \d+)', r'\1-го\2', text)

text = sub(r'(\d+) годов', r'\1-го годов', text)
text = sub(r'\b([Кк] \d+)-(\d+) (годам|гг\.)', r'\1-му \2-му годам', text)
text = sub(r'(\d+-м )(гг\.)', r'\1годам', text)

text = sub(r'\b(\d+) века\b', r'\1-го века', text) # Спорный шаблон
text = sub(r'\b([Вв] \d+) (веке|в\.)', r'\1-м веке', text)
text = sub(r'\b([Кк] \d+)(-му) (веку|в\.)', r'\1-му веку', text)
text = sub(r'\b([Дд]о|[Пп]осле|[Сс])( \d+) (века|в\.)', r'\1\2-го века', text)
text = sub(r'\b([Кк] \d+)-(\d+) векам', r'\1-му \2-му векам', text)

text = sub(r'\b([Вв] \d+) (году|г\.)', r'\1-м году', text)
text = sub(r'\b([Кк] \d+) (году|г\.)', r'\1-му году', text)

text = sub(r'([Пп]о сравнению с|[Пп]еред)( \d+) г\.', r'\1\2-м годом', text)
text = sub(r'(\d+) годом', r'\1-м годом', text)
text = sub(r'\b([Дд]о|[Пп]осле|[Сс])( \d+) (года|г\.)', r'\1\2-го года', text)

text = sub(r'\b([Вв] \d+)-(\d+) (годах|гг\.)', r'\1-м \2-м годах', text)
text = sub(r'(\d+)-(\d+) (годы|гг\.)', r'\1-й \2-й годы', text)

text = sub(r'\b([Вв] \d+) (годах|гг\.)', r'\1-х годах', text)
#text = sub(r'\b([Кк] \d+0) гг\.', r'\1-м годам', text)
text = sub(r'\b([Дд]о|[Пп]осле|[Сс])( \d+) (годов|гг\.)', r'\1\2-х годов', text)
text = sub(r'\b([Сс] \d+) по (\d+) (годы|гг\.)', r'\1-го по \2-й годы', text)

text = sub(r'([Зз]им[аеойуы]{1,2} \d+)-(\d+)', r'\1-го \2-го', text)

text = sub(r'(\d)( квартал)\b', r'\1-й\2', text)
text = sub(r'(\d)( квартала)\b', r'\1-го\2', text)
text = sub(r'(\d)( кварталу)\b', r'\1-му\2', text)
text = sub(r'(\d)( квартал)(е|ом)\b', r'\1-м\2\3', text)

text = sub(r'\b([Дд]о|[Кк]о?||[Пп]осле|[Сс]о?)( \d+)( недел)(е|ей|и)\b', r'\1\2-й\3\4', text)

text = sub(r'(\d+-го )г\.', r'\1года', text)
text = sub(r'([Сс] \d+-м )г\.', r'\1годом', text)
text = sub(r'(\d+-е )гг\.', r'\1годы', text)
text = sub(r'(\d+-ми )гг\.', r'\1годами', text)
text = sub(r'(\d+-х )гг\.', r'\1годов', text)

text = sub(r'\b(\d+)-(\d+)-(е|го|ми|м|х)\b', r'\1-\3 \2-\3', text)

text = sub(r'(1\d|[02-9][05-9]|\b[5-9]) года\b', r'\1-го года', text)
text = sub(r'(1\d|[02-9][02-9]|\b[2-9]) год\b', r'\1-й год', text)
text = sub(r'([Нн]а |[Зз]а )(\d{,2}1\d|\d{,2}[02-9][02-9]|\b[2-9]) г\.', r'\1\2-й год', text)

text = sub(r'(\d+) г\.р\.', r'\1-го года рождения', text)

# Порядковые числительные

samples = findall(r'(\d+-е)( Олимпийские| годы)', text)
for sample in samples:
    text = text.replace(sample[0] + sample[1], ordinal(sample[0][:-2], 0, 3) + sample[1], 1)

samples = findall(r'([Вв] )(\d+-е)\b', text)
for sample in samples:
    text = text.replace(sample[0] + sample[1], sample[0] + ordinal(sample[1][:-2], 0, 3), 1)

samples = findall(r'([Кк] )(\d+-м)\b', text)
for sample in samples:
    text = text.replace(sample[0] + sample[1], sample[0] + ordinal(sample[1][:-2], 2, 3), 1)

samples = findall(r'(\d+-х-)', text)
for sample in samples:
    text = text.replace(sample, ordinal(sample[:-3], 1, 3) + ' ', 1)

samples = findall(r'\d+-я\b', text)
for sample in samples:
    text = text.replace(sample, ordinal(sample[:-2], 0, 2), 1)

samples = findall(r'\b([Вв]о? |[Нн]а )(\d+-ю)\b', text)
for sample in samples:
    text = text.replace(sample[0] + sample[1], sample[0] + ordinal(sample[1][:-2], 1, 2), 1)

samples = findall(r'\d+-ю\b', text)
for sample in samples:
    text = text.replace(sample, ordinal(sample[:-2], 1, 2), 1)

samples = findall(r'\b([Вв] |[Нн]а |[Пп]ри )(\d+-м)\b', text)
for sample in samples:
    text = text.replace(sample[0] + sample[1], sample[0] + ordinal(sample[1][:-2], 5, 0), 1)

samples = findall(r'\b([Кк] )(\d+-м)\b', text)
for sample in samples:
    text = text.replace(sample[0] + sample[1], sample[0] + ordinal(sample[1][:-2], 2, 3), 1)

samples = findall(r'\b([Сс] )(\d+-м)\b', text)
for sample in samples:
    text = text.replace(sample[0] + sample[1], sample[0] + ordinal(sample[1][:-2], 3, 0), 1)

samples = findall(r'\d+-му\b', text)
for sample in samples:
    text = text.replace(sample, ordinal(sample[:-3], 2, 0), 1)

samples = findall(r'\d+-го\b', text)
for sample in samples:
    text = text.replace(sample, ordinal(sample[:-3], 1, 0), 1)

samples = findall(r'\d+-ми\b', text)
for sample in samples:
    text = text.replace(sample, ordinal(sample[:-3], 3, 3), 1)

samples = findall(r'(\d{,}1\d|\d{,}[02-9][015-9]|[015-9])-х\b', text)
for sample in samples:
    text = text.replace(sample + '-х', ordinal(sample, 1, 3), 1)

samples = findall(r'\b([Дд]о|[Пп]осле|[Сс]о?) (\d+-й)\b', text)
for sample in samples:
    text = text.replace(sample[0] + ' ' + sample[1], sample[0] + ' ' + ordinal(sample[1][:-2], 1, 1), 1)

samples = findall(r'\d+-й\b', text)
for sample in samples:
    text = text.replace(sample, ordinal(sample[:-2], 0, 0), 1)

samples = findall(r'(\d+-м)( годах)\b', text)
for sample in samples:
    text = text.replace(sample[0] + sample[1], ordinal(sample[0][:-2], 5, 0) + sample[1], 1)

#samples = findall(r'(\d{2}1\d|\d{3}[05-9])( года)\b', text)
#for sample in samples:
#    text = text.replace(sample[0] + sample[1], ordinal(sample[0], 1, 0) + sample[1], 1)

samples = findall(r'(\d+-м)( [а-яА-Я]+м\b)', text)
for sample in samples:
    text = text.replace(sample[0] + sample[1], ordinal(sample[0][:-2], 3, 0) + sample[1], 1)

samples = findall(r'\d+-е\b', text)
for sample in samples:
    text = text.replace(sample, ordinal(sample[:-2], 0, 1), 1)

# Буквы греческого алфавита
#greekletters = 'ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσΤτΥυΦφΧχΨψΩως'
#letternames = ('альфа', 'бета', 'гамма', 'дельта', 'эпсилон', 'дзета', 'эта', 'тета', 'йота', 'каппа', 'лямбда', 'мю', 'ню', 'кси', 'омикрон', 'пи', 'ро', 'сигма', 'тау', 'ипсилон', 'фи', 'хи', 'пси', 'омега', 'сигма')
#for j in greekletters:
#    text = text.replace(j, letternames[greekletters.index(j)//2])

text = sub(r'(\w)(\n|\Z)', r'\1.\2', text)

file = open('/tmp/clip.txt', 'w')
file.write(text)
file.close()
