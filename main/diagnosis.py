"""Diagnose summary statistics of the cover/uncover eye test"""
import json
import os

def diagnose_to_json(before, after):
    """
    Diagnose the summary statistics before and after cover
    in cover/uncover eye test and save result to json file
    Parameters:
        before: Path to JSON of summary statistics before cover
        after: Path to JSON of summary statistics after cover
    Returns:
        diagnosis: String of diagnosis
    """
    with open(before, "r") as f:
        before = json.load(f)
    with open(after, "r") as f:
        after = json.load(f)
    diagnosis = diagnose(before, after)
    diagnosis_json = json.dumps({"diagnosis": diagnosis})
    if not os.path.exists("./results"):
        os.mkdir("./results")
    with open("./results/diagnosis.json", "w") as f:
        f.write(diagnosis_json)
    pass

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
    N = 180 # number of samples
    T_CRIT = 1.9734 # critical t-value at 95% confidence with DOF=178

    expo_estotropia_test = (before["cornea10Dx"], after["cornea10Dx"], "Expotrophia", "Esotrophia") 
    hyper_hypotropia_test = (before["cornea10Dy"], after["cornea10Dy"], "Hypertropia", "Hypotrophia")
    test1_var =  cauchy_schwartz_variance(expo_estotropia_test[0]["std"], expo_estotropia_test[1]["std"], N)
    test1 = confidence_interval(expo_estotropia_test[0]["mean"], expo_estotropia_test[1]["mean"],test1_var, N, T_CRIT)
    test2_var = cauchy_schwartz_variance(hyper_hypotropia_test[0]["std"], hyper_hypotropia_test[1]["std"], N)
    test2 = confidence_interval(hyper_hypotropia_test[0]["mean"], hyper_hypotropia_test[1]["mean"],test2_var, N, T_CRIT)
    if test1[0] > TOLERANCE:
        return expo_estotropia_test[2]
    if test1[1] < -1 * TOLERANCE:
        return expo_estotropia_test[3]
    if test2[0] > TOLERANCE:
        return hyper_hypotropia_test[2]
    if test2[1] < -1 * TOLERANCE:
        return hyper_hypotropia_test[3]
    else:
        return "Normal"

def cauchy_schwartz_variance(std1, std2, N):
    """Calculate the variance of the difference of two samples
    using the Cauchy Schwartz Variance/Inequality
    Parameters:
        std1: standard deviation of sample 1
        std2: standard deviation of sample 2
        N: number of samples in total
    """
    return (std1 + std2)**2 / N

def confidence_interval(mu1, mu2, var, N, T_CRIT):
    """Calculate 95% confidence interval
    Parameters:
        mu1: mean of sample 1
        mu2: mean of sample 2
        var: variance of the difference of 
            means of sample 1 and 2
        N: number of samples in total
        T_CRIT: critical t-value at 95% confidence with DOF=N-2
    """
    return (mu1 - mu2 + (T_CRIT * var / N), mu1 - mu2 - (T_CRIT * var / N))