import numpy as np

def summary_statistics(measurements):
    """Takes a list of measurements and returns measurement summary statistics
    Parameters:
        measurements: list of values
    Returns:
        summary_statistics: dictionary of summary statistics
            - key: statistic name (e.g. "mean")
            - value: statistic value
    """
    try:
        summary_statistics = {
            "mean": np.mean(measurements),
            "std": np.std(measurements),
            "min": np.min(measurements),
            "max": np.max(measurements),
            "median": np.median(measurements),
            "range": np.max(measurements) - np.min(measurements)
        }
        return summary_statistics
    except TypeError:
        return {}
