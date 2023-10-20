"# learning"

TO CREATE NEW GIT REPOSITORY
mkdir nameofnewdirectory (this is to create a new directory)
cd nameofnewdirectory (to get into the new directory)
git init (to make the current directory a github repository)

TO SET UP A REMOTE REPOSITORY
go to github and create a new repository
go to your repository directory in the command line the type
git remote add origin pastehereyournewrepositoryurl


GIT COMMANDS
Everytime you start coding do this
git pull origin branchname

When adding/updating code
git add nameoffile.extensionname (to add a single file)
git add . (to add all files or folders in a project)
git status (optional, to check status of file/s to be added)
git commit -m "message" 
git push origin

TO ADD NEW BRANCH
git checkout -b nameofnewbranch

ACCESS A BRANCH
git checkout nameofbranch

PUSHING ANOTHER BRANCH
git checkout nameofbranch
git push origin nameofbranch

TO MERGE files from a branch to another branch
git checkout nameofbranchtoupdate
git merge nameofsourcebranch


TO FIX GIT PUSH CONFLICT
git pull origin branchname

IF AUTOMATIC MERGE FAILED
fix conflicts first in the file then type
git add nameoffile.extensionname
git commit -m "message"
git push

