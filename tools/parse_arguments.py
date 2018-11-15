#!/usr/bin/env python3

def camel(s:str)->str:
    result = ''
    flag = False
    for c in s:
        if c in ('_', '-'):
            flag = True
            continue
        if flag:
            result += c.upper()
            flag = False
        else:
            result += c
    return result

def uncamel(s:str, undercore:bool = False)->str:
    result = ''
    for c in s:
        if c.isupper():
            result += ('_' if undercore else '-') + c.lower()
        else:
            result += c
    return result

if __name__ == '__main__':
    import sys, re
    with open(sys.argv[1], 'r+') as fp:
        default_options = {}
        for line in fp.readlines():
            line = re.sub(r'^\s+', '', line[:-1])
            if not line or line.startswith('//'): continue
            name, value = tuple([x.strip() for x in re.split(r'\s*:\s*', line.split(',')[0])])
            data = default_options[uncamel(name, True)] = [name, None]
            assert name == camel(uncamel(name))
            if value in ('true', 'false'):
                argument = 'arguments.add_argument(\'--var-{}\', choices=[\'true\',\'false\'])'.format(uncamel(name))
                data[1] = value
            elif re.match(r'^\d+$', value):
                argument = 'arguments.add_argument(\'--var-{}\', type=int)'.format(uncamel(name))
                data[1] = int(value)
            elif value == 'null':
                argument = 'arguments.add_argument(\'--var-{}\')'.format(uncamel(name))
            else:
                value = re.sub(r'[\'"]', '', value)
                argument = 'arguments.add_argument(\'--var-{}\')'.format(uncamel(name))
                data[1] = value
            print(argument)
        print(default_options)
