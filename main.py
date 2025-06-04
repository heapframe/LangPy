import requests, time, os, datetime, random, sys, json, languagenut
from tqdm import tqdm
from prettytable import PrettyTable

print(r"""                  
   __                  ___      
  / /  ___ ____  ___ _/ _ \__ __
 / /__/ _ `/ _ \/ _ `/ ___/ // /
/____/\_,_/_//_/\_, /_/   \_, / 
               /___/     /___/  
              """)


languagenut = languagenut.LanguageNut()


def Login(AttemptFileLogin):
    if len(sys.argv) == 2:
        print("Subversion, using loginfile provided as argument")
        if os.path.isfile(sys.argv[1]):
            f = open(sys.argv[1], "r")
            usernameIn = f.readline()
            password = f.readline()
        else:
            print("Subversion file doesn't exist.")
            usernameIn = input("Username: ")
            password = input("Password: ")
    elif AttemptFileLogin:
        if os.path.isfile("login"):
            print("Login file detected, skipping login...")
            f = open("login", "r")
            usernameIn = f.readline()
            password = f.readline()
        else:
            usernameIn = input("Username: ")
            password = input("Password: ")
            choice = input("Would you like to save these login details? Y/n: ")
            if choice.lower() != "n":
                filename = input("What name to save it under? (name it login for autologin): ")
                if os.path.isfile(filename):
                    choice = input("File exists, overwrite? Y/n: ")
                    if choice.lower() != "n":
                        with open(filename, "w") as dafile:
                            dafile.write(f"{usernameIn}\n{password}")
                            print("Saved")
                    else:
                        success = False
                        while not success:
                            filename = input("What name to save it under? (name it login for autologin)")
                            if os.path.isfile(filename):
                                print("File already exists")
                            else:
                                with open(filename, "w") as dafile:
                                    dafile.write(f"{usernameIn}\n{password}")
                                    print("Saved")
                else:
                    with open(filename, "w") as dafile:
                        dafile.write(f"{usernameIn}\n{password}")
                        print("Saved")
    else:
        usernameIn = input("Username: ")
        password = input("Password: ")
    
    return languagenut.loginController.attemptlogin(usernameIn, password)


login = Login(True)

if not login.get("isLoggedIn"):
    Success = False
    while not Success:
        print("Failed to login, try again")
        login = Login(False)
        if login.get("isLoggedIn"):
            Success = True

# print(login)

print("Hello", login.get("personName"))
token = login.get("newToken")

HwData = languagenut.assignmentController.getViewableAll(token)

print("This is all your set homework")

HwDataList = {}
idToName = {}

prettyHwTable = PrettyTable(["ID", "Name", "Teacher", "Set Date", "Due Date", "Completed Tasks"])

for hw in HwData.get("homework"):
    HwDataList[hw.get("id")] = hw.get("tasks")
    idToName[hw.get("id")] = hw.get("createdBy")
    data = languagenut.recentActivity.getAllStudentActivity(token, idToName[hw.get("id")])
    names = [activity['name'] for activity in data['activity']]
    # print("(", hw.get("id"), ")", " ", hw.get("name"), "| ", names[0], " | Due: ", hw.get("due"))
    completed = 0
    total = 0
    for task in hw.get("tasks"):
        if task["gameResults"] is not None:
            completed += 1
        total += 1
    prettyHwTable.add_row(
        [hw.get("id"), hw.get("name"), names[0], hw.get("set"), hw.get("due"), f"{completed}/{total}"])

print(prettyHwTable)

hwIdSelected = input("Select by id: ")

if not hwIdSelected in HwDataList:
    Success = False
    while not Success:
        print("Unknown id")
        hwIdSelected = input("Select by id: ")
        if hwIdSelected in HwDataList:
            Success = True


work = 0
taskC = 0

print("Completing homework...")
print("PSA: Grammar bot does not work")
random.random()
awwMan = 0
#f3 = open(str(time.time()) + "_taskdata", "w")
#json.dump(HwDataList[hwIdSelected], f3, indent = 6)
#f3.close()
#input()
for task in tqdm(HwDataList[hwIdSelected], "Botting"):
    translation = task.get("translation")
    moduleUid = task.get("rel_module_uid")
    moduleType = task.get("type")
    gameUid = task.get("game_uid")
    catalogUid = task.get("rel_module_uid")
    featureUid = task.get("feature_uid")
    gameType = task.get("base")[5]
    # vocabNumber = task.get("no_correct")
    homeworkUid = hwIdSelected
    getWrong = random.randrange(0,2)
    done = 0
    translationData = languagenut.vocabTranslationController.getVocabTranslations(token, catalogUid, homeworkUid) #getVocabTranslations(token, catalogUid, homeworkUid)
    #f2 = open(str(time.time()) + "_translation", "w")
    #json.dump(translationData, f2, indent = 6)
    #f2.close()
    correctVocabs = ""
    incorrectVocabs = ""
    correctStudentAns = ""
    incorrectStudentAns = ""
    try:

        for translation in translationData.get("vocabTranslations"):
            correctVocabs = correctVocabs + "%2C" + translation.get("uid")

        for translation in translationData.get("vocabTranslations"):
            correctStudentAns = correctStudentAns + "%2C" + translation.get("originalWord")

        correctVocabs = correctVocabs[3:]
        correctStudentAns = correctStudentAns[3:].replace(" ", "+").replace(",","")

        addScore = languagenut.gameDataController.addGameScore(token, moduleUid, gameType, homeworkUid, gameUid, "true", correctVocabs, incorrectVocabs, "false", # order is meant to be correct, incorrect
                                featureUid, "false", "false", "false", "false", str(random.randrange(180000, 360000)) , "10", correctStudentAns,
                                str(unixMillis()), str(int(unixMillis() - 3000)))
        if addScore.get("SUCCESS"):
            work += 1
        taskC += 1
        #TODO: remove temp code
        #f = open(str(time.time()), "w")
        #json.dump(addScore, f, indent = 6)
        #f.close()
    except TypeError:
        awwMan = awwMan + 1
        continue
    time.sleep(5)
print(f"Completed {work}/{taskC} tasks")
if awwMan != 0:
    print(f"Failed to complete {awwMan} tasks. Unsupported?")
