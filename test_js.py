import execjs
with open('src/bookstore/scripts/js/validation.js') as file:
    js_code = file.read()
ctx = execjs.compile(js_code)
result1 = ctx.call('validateEmail', 'example@example.com')
result2 = ctx.call('validateEmail', 'not an email address')
result3 = ctx.call('validateEmail', 'almost_an_email_address@email')
print(f'result 1 is {result1}')
print(f'result 2 is {result2}')
print(f'result 3 is {result3}')