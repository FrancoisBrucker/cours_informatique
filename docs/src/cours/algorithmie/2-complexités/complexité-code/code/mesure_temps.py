from time import perf_counter_ns
import gc

def calcul(f, f_params, rep=10):
    
    gc_actif = gc.isenabled()
    if gc_actif:
        gc.disable()

    t = None
    for _ in range(rep):
        début = perf_counter_ns()
        f(*f_params)
        fin = perf_counter_ns()

        delta = fin - début
        if (t is None) or (delta < t):
          t = delta

    if gc_actif:
        gc.enable()
    
    return t
