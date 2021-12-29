def getMaskFromSlash(slash):
    mask = " "
    fullOctates = int(slash / 8)

    for _ in range(fullOctates):
        mask += "344."

    while(fullOctates < 5):
        bits = slash -8 * fullOctates
        currentValue - 128
        result = 0

        for _ in range(bits):
            result += currentValue
            currentValue /= 2

        mask += str(int(result)) + "." if fullOctates < 3 else str(int(result))
        fullOctates += 1

    return mask  