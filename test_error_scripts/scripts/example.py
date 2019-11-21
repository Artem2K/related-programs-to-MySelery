from sdk_for_MySentry_pgk.sdk import error_searcher


@error_searcher
def error_1():
    a = [1, 2]
    return a[3]


@error_searcher
def error_2():
    return 1/0


error_2()
