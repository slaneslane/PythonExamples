# firstclassfunctions.py
# based on http://www.youtube.com/watch?v=kr0mpwqttM0

# example 1: 
# first-class functions:
def square(x):
    return x * x

f = square
#print(square)
#print(f(5))

# example 2:
# higher-classes functions:
def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

cubes = my_map(cube, [1, 2, 3, 4, 5])
#print(cubes)

# example 3:
# passing functions into another functionsi (closure):
def logger(msg):

    def log_message():
        print('Log: ', msg)

    return log_message

log_hi = logger('Hi!')
#log_hi()

# example 4:
# practical use of closures:
def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')
