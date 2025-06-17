import json

import faker

f = faker.Faker()

data = [[f.random_number(digits=12, fix_len=True), f.random_number(digits=6, fix_len=True)] for i in range(10)]

index = 1
result_json = {
    'Entry': {
        'next': 'step1'
    }
}
for a, b in data:
    result_json[f'step{index}'] = {
        'recognition': 'OCR',
        'expected':    '12位',
        'action':      'Click',
        'next':        f'step{index + 1}'
    }
    index += 1
    result_json[f'step{index}'] = {
        'action': 'Key',
        'key':    [30 + int(c) for c in str(a)],
        'next':   f'step{index + 1}'
    }
    index += 1
    result_json[f'step{index}'] = {
        'recognition': 'OCR',
        'expected':    '6位',
        'action':      'Click',
        'next':        f'step{index + 1}'
    }
    index += 1
    result_json[f'step{index}'] = {
        'action': 'Key',
        'key':    [30 + int(c) for c in str(b)],
        'next':   f'step{index + 1}'
    }
    index += 1

result_json[f'step{index}'] = {
    'action': 'DoNothing',
}

with open(r'D:\ProjectsPycharm\maaframeworkpractise\assets\resource\pipeline\pipeline.json', 'w',
          encoding='utf-8') as f:
    json.dump(result_json, f, ensure_ascii=False, indent=4)
