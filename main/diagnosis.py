from pstats import Stats
import numpy as np

def diagnose(before, after):
    """
    Diagnose the summary statistics before and after cover
    in cover/uncover eye test
    Parameters:
        before: Dictionary of summary statistics before cover
        after: Dictionary of summary statistics after cover
    Returns:
        diagnosis: String of diagnosis
    """
    TOLERANCE = 4 # mm
    N = 90 # number of samples
    DOF = 178 # degrees of freedom
    expo_estotropia_test = (before["cornea10Dx"], after["cornea10Dx"], "Expotrophia", "Esotrophia") 
    hyper_hypotropia_test = (before["cornea10Dy"], after["cornea10Dy"], "Hypertropia", "Hypotrophia")
    test1 = t_test(expo_estotropia_test[0]["mean"], expo_estotropia_test[1]["mean"], expo_estotropia_test[0]["std"], expo_estotropia_test[1]["std"], N, DOF)
    test2 = t_test(hyper_hypotropia_test[0]["mean"], hyper_hypotropia_test[1]["mean"], hyper_hypotropia_test[0]["std"], hyper_hypotropia_test[1]["std"], N, DOF)
    
def t_test(mu1, mu2, std1, std2, N, DOF):
    t = (mu1 - mu2) / (std1 / np.sqrt(N) + std2 / np.sqrt(N))
    p = 1 - Stats.t.cdf(t, DOF)
    return (t, p)