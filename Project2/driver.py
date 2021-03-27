from lib.Manager import Manager
from settings import log, getInput, display
import settings

def main():

    #   Get initialization values from init file
    initValues = getInput(settings.initFilePath)
 
    ST = [int(val) for val in initValues[0].split(" ")]
    PT = [int(val) for val in initValues[1].split(" ")]

    log("INPUT VALUES \n" + str(ST) + "\n" + str(PT))

    manager = Manager(ST,PT) 

    #   Get Virtual addresses from input file
    VA = [int(val) for val in getInput(settings.inputFilePath)[0].split(" ")]

    #   Virtual Addess translation
    log("\n\n VIRTUAL ADDRESS TRANSLATION")
    for i in range(len(VA)):
        PA = manager.virtualAddressTranslation(VA[i])
        display(str(PA))
    
if __name__ == "__main__":
    main()
