# decorators_with_args.py
# based on http://www.youtube.com/watch?v=KIBPCzcQNU8

def prefix_decorator(prefix, sufix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print('{} Executed Before {}'.format(prefix, original_function.__name__))
            result = original_function(*args, **kwargs)
            print('{} Execute After {}'.format(sufix, original_function.__name__), '\n')
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator('OPENING:', 'CLOSING:')
def display_info(name, age):
    print('display_info ran with arguments: ({}, {})'.format(name, age))

display_info('Tom', 34)
display_info('Jane', 32)
