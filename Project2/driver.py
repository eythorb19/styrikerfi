from lib.Manager import Manager
from settings import log, getInput, display
import settings

def main():

    initValues = getInput(settings.initFilePath)
 
    ST = [int(val) for val in initValues[0].split(" ")]
    PT = [int(val) for val in initValues[1].split(" ")]

    log(ST)
    log(PT)

    manager = Manager(ST,PT)
    returnVal = ""

    VA = [int(val) for val in getInput(settings.inputFilePath)[0].split(" ")]

    for i in range(len(VA)):
        PA = manager.virtualAddressTranslation(VA[i])
        display(str(PA))
    
if __name__ == "__main__":
    main()
