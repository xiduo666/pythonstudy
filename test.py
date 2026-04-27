from functools import partial
def log(level, message): print(f"[{level}] {message}")
info_log=partial(log,level='INFO')
error_log=partial(log,'ERROR')
print(error_log('hello'))