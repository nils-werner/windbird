def wind_bft(val):
    thresholds = (
        0.3, 1.5, 3.4, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6
    )

    for bft, ms in enumerate(thresholds):
        if val < ms:
            return bft

    return len(thresholds)


def wind_kts(val):
    return val * 3.6 / 1.852
