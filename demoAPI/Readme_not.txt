Tools/Librarry:
=================
pip install pytest==3.8.1
pip install selenium==3.141.0
pip install requests==2.17.3
pip install jsonpath==0.75
pip install openpyxl==2.6.1
pip install allure-pytest==2.5.2



# Add project in git hub repository:
---------------------------------
>Configure local repository:
===========================
:Configure user_name , user_email and see all configre list
mds-MacBook-Pro:API-pytest-project mdrubel$ git config --global user.name "rubeldm123"
mds-MacBook-Pro:API-pytest-project mdrubel$ git config --global user.email "email@gmail.com"
mds-MacBook-Pro:API-pytest-project mdrubel$ git config --list
credential.helper=osxkeychain
user.name=username
user.email=email@gmail.com
--------------------------------------------------------------------------------------
>Create local Repository:
===========================
:Create a Local repository in different location then project location example:create folder in desktop"
------
mds-MacBook-Pro:~ mdrubel$ cd Desktop
mds-MacBook-Pro:Desktop mdrubel$ mkdir Api_Automation_python_Jan2021
mds-MacBook-Pro:Desktop mdrubel$ cd Api_Automation_python_Jan2021/
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ pwd
/Users/mdrubel/Desktop/Api_Automation_python_Jan2021

::::::::git init:::::: Initiallize Local repositor with .git extention
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git init
Initialized empty Git repository in /Users/mdrubel/Desktop/Api_Automation_python_Jan2021/.git/
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ ls -all
total 0
drwxr-xr-x@  3 mdrubel  staff   96 Jan 23 13:46 .
drwx------@ 24 mdrubel  staff  768 Jan 23 13:46 ..
drwxr-xr-x@  9 mdrubel  staff  288 Jan 23 13:46 .git
:::::::::::::::::::::::::::::::::::::::::::::::::::
>:::::::::git status :::::::Copy project to local reository and navigate to Local repository
NOTE: WHEN we copy project to local repository it will be UNTRACT state
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ pwd
/Users/mdrubel/Desktop/Api_Automation_python_Jan2021
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.DS_Store
	API-pytest-project/

nothing added to commit but untracked files present (use "git add" to track)
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
>:::::::::::::::git add: Move file to the STAGE state
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git add API-pytest-project/
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   API-pytest-project/.idea/.gitignore
	new file:   API-pytest-project/.idea/API-pytest-project.iml
	new file:   API-pytest-project/.idea/inspectionProfiles/profiles_settings.xml
	new file:   API-pytest-project/.idea/misc.xml
	new file:   API-pytest-project/.idea/modules.xml
	new file:   API-pytest-project/Selenium_test/__pycache__/test_TC_001_ValidateRegistration.cpython-39-PYTEST.pyc
	new file:   API-pytest-project/Selenium_test/chromedriver
	new file:   API-pytest-project/Selenium_test/test_TC_001_ValidateRegistration.py
	new file:   API-pytest-project/asasastest_TC_001_ValidateRegistratio

NOTE: If we write " git add." it will add all the file to Untract to Stage state
::::::::::::::::::::::::::::::::::::::::::::;
::::::::::git commit -m "Automation start": move file to TRACT stage:::::::
NOTE: git commit // it will move all the file from STAGE state to TRACK stage
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git commit -m "Automation start"

::Check status:

mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git status
On branch master
nothing to commit, working tree clean



:::::::::::::git log ::::::It will display history of the log:
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git log
commit 925cd9b19219e7fab9aa486004b8f629f7dc3ca3 (HEAD -> master)
Author: rubelfdg3 <rfdgl.com>
Date:   Sat Jan 23 14:25:12 2021 -0600

    Update Readme file

::::::::::::git reset HEAD : it will move file from STAGE state to Untract state:
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git reset HEAD API-pytest-project/readme_note.txt
Unstaged changes after reset:
M	API-pytest-project/readme_note.txt
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   API-pytest-project/readme_note.txt

no changes added to commit (use "git add" and/or "git commit -a")

:::::::::::::: Add above to STAGE stat and then move to Track stage musing commit




mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git add .
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   API-pytest-project/readme_note.txt

mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git commit -m "Update Readme file"
[master 2e47d80] Update Readme file
 1 file changed, 29 insertions(+)
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git status


:::Add remote Repository::::::::::::
:::::::::::git remote -v --> it will show all Remote repository
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git remote -v
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git remote add origin https://github.com/rubeldm123/Pytest_Demo.git
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git remote -v
origin	https://github.com/rubeldm123/API_Automation_Python_Jan2021.git (fetch)
origin	https://github.com/rubeldm123/API_Automation_Python_Jan2021.git (push)
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$


:::::::::::::::::::git push ::::::it will push to Remote repository:
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git push origin master


We will pull it from Git hub Repository, update Readme file then will make commit and pust it agian to git hub
mds-MacBook-Pro:Api_Automation_python_Jan2021 mdrubel$ git pull origin master

This is upto date version

++++++++++++++++++++++++++++++++++++++++++++++++

::::::::::::Jenkins configuration::::::::::
https://www.jenkins.io/doc/pipeline/tour/getting-started/


https://get.jenkins.io/war-stable/2.263.2/

mds-MacBook-Pro:downloads mdrubel$ java -jar jenkins.war --httpPort=8090
*************************************************************
*************************************************************
*************************************************************

Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

92e896fbc148427fb99b597dbba324d8

This may also be found at: /Users/mdrubel/.jenkins/secrets/initialAdminPassword

*************************************************************
*************************************************************
*************************************************************
 http://localhost:8090
userName; rubel
password: password123

------------_Allure Reprt:
^Cmds-MacBook-Pro:demoAPI mdrubel$ python -m pytest --alluredir=target/allure-rertr
^Cmds-MacBook-Pro:demoAPI mdrubel$ allure serve target/allure-report

