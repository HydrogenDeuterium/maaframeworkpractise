import faker
import maafw

f = faker.Faker()

data = [[f.random_number(digits=12, fix_len=True), f.random_number(digits=6, fix_len=True)] for i in range(10)]

tasker=maafw.Tasker()

last_no= ''
for no, pw in data:
    print(no, pw)

    pipelines = {
        'Entry':        {
            'next': ['focus_noa', 'focus_nob']
        },
        'focus_noa':     {
            'recognition': 'OCR',
            'expected':    '12位',
            'next': 'delete_no'
        },
        'focus_nob': {
            'recognition': 'OCR',
            'expected':    ' ?'.join(last_no),
            'next': 'delete_no'
        },
        'delete_no':    {
            'action': 'Key',
            'action': 'Key',
            'key':    [] * 12,
            'next': 'input_no'
        },
        'input_no':     {
            'action':'Text',
            'text':str(no),
            'next': 'focus_pw'
        },
        'focus_pw':{
            'recognition': 'OCR',
            'expected':    r'6位|\*+',
            'next': 'delete_pw'
        },
        'delete_pw':    {
            'action': 'Key',
            'key':    []*12,
            'next': 'kew_pw1'},
        'kew_pw1':      {
            'action': 'Key',
            'key':    ord(pw[1]) - 41,
            'next':   'kew_pw2'},
        'kew_pw2':      {
            'action': 'Key',
            'key':    ord(pw[2]) - 41,
            'next':   'kew_pw3'},
        'kew_pw3':      {
            'action': 'Key',
            'key':    ord(pw[3]) - 41,
            'next':   'kew_pw4'},
        'kew_pw4':      {
            'action': 'Key',
            'key':    ord(pw[4]) - 41,
            'next':   'kew_pw5'},
        'kew_pw5':      {
            'action': 'Key',
            'key':    ord(pw[5]) - 41,
            'next':   'kew_pw6'},
        'kew_pw6':      {
            'action': 'Key',
            'key':    ord(pw[6]) - 41,
            'next':   'click_search'},
        'click_search': {
            'recognition': 'OCR',
            'expected':    '查询',
            'action':      'Click',
            'next':        'check_result'},
        'check_result': {
            'recognition': 'OCR',
            'expected':    '1000'}

    }

    result=tasker.post_task("Entry", pipelines).wait().get()
    print(result)

