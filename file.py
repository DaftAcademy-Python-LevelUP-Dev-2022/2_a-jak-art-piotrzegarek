def greeter(func):
    pass
    def inner(*args):
        input_data = "Aloha " + func(*args).title()
        return input_data
    return inner


def sums_of_str_elements_are_equal(func):
    pass
    def inner(*args):
        input_data = func(*args).split()
        results_list = []
        for string in input_data:
            sum = 0
            if string[0] != "-":
                for value in string:
                    sum += int(value)
            else:
                for value in string[1:]:
                    sum -= int(value)
            results_list.append(sum)

        if results_list[0] == results_list[1]:
            return f"{results_list[0]} == {results_list[1]}"
        else:
            return f"{results_list[0]} != {results_list[1]}"
    return inner


def format_output(*required_keys):
    pass
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            new_result = {}     
            for key in required_keys:
                if '__' in key:
                    splited_keys = key.split('__')
                    for single_key in splited_keys:
                        if single_key not in result:
                            raise ValueError

                    new_result[key] = ""
                    for i in range(len(splited_keys)):
                        new_result[key] = new_result[key] + result[splited_keys[i]] + " "
                    new_result[key] = new_result[key][:-1]

                else:
                    if key in result:
                        if result[key] != "":
                            new_result[key] = result[key]
                        else:
                            new_result[key] = "Empty value"
                    else:
                        raise ValueError

            return new_result
        return wrapper
    return decorator   


def add_method_to_instance(klass):
    pass
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            return func()
        setattr(klass, func.__name__, inner_wrapper)
        return inner_wrapper
    return outer_wrapper
