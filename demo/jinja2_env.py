from jinja2 import Environment

def environment(**options):
    env = Environment(**options)
    env.filters['jinjafilter'] = jinjafilter

    return env


def jinjafilter(li):
    if li in [1,2,3]:
        return li*2
