
def log(filename=None):
    def inner(function):
        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                report = f'{function.__name__} ok, result is: {result}'
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f'{report}\n')
                return report
            except Exception as e:
                report = f'{function.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}'
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f'{report}\n')
                return report
        return wrapper
    return inner
