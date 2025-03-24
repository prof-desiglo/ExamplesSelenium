import os


def getTestLogPath(value):
    testPath = os.path.join(os.getcwd(), "testLog")
    return os.path.join(testPath, value + ".png")