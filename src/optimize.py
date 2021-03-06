def NewtonMethod(f, df, xini=0., toler=0.001, itrLim=50):
    '''
    Solve x where f(x) = 0 with Newton method.
    '''
    itr = 0
    x = xini
    while abs(f(x)) >= toler and itr < itrLim:
        msg = 'itr: {:d}, x: {:8.4f}, f: {:8.4f}, df: {:8.4f}'.format(itr, x, f(x), df(x))
        print(msg)
        x -= (f(x) / df(x))
        itr += 1
    
    msg = 'itr: {:d}, x: {:8.4f}, f: {:8.4f}, df: {:8.4f}'.format(itr, x, f(x), df(x))
    print(msg)
    return x


def GradientDescent(f, df, xini=-1.0, alpha=1, toler=0.001, itrLim=50):
    '''
    Solve x where f(x) = 0 with the gradient descent method.
    '''
    itr = 0
    x = xini
    while abs(df(x)) >= toler and itr < itrLim:
        msg = 'itr: {:d}, x: {:8.4f}, f: {:8.4f}, df: {:8.4f}'.format(itr, x, f(x), df(x))
        print(msg)
        x -= alpha * df(x)
        itr += 1
    
    msg = 'itr: {:d}, x: {:8.4f}, f: {:8.4f}, df: {:8.4f}'.format(itr, x, f(x), df(x))
    print(msg)
    return x