import logging

def log_function_call(func):
    def decorator(*args, **kwargs):
        logging.info(f"calling {func.__name__} with args={args} , kwargs={kwargs}")
                     
        result =func(*args , **kwargs) 
        logging.info(f"{func.__name__} returned {result}")

        return result
    return decorator
@log_function_call
def my_function(a, b):
    return a+b