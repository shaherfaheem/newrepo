"# learning"

GIT COMMANDS
Everytime you start coding do this
git pull origin

When adding/updating code
git add nameoffile.extensionname (to add a single file)
git add . (to add all files or folders in a project)
git status (optional, to check status of file/s to be added)
git commit -m "message" 
git push origin

TO ADD NEW BRANCH
git checkout -b nameofnewbranch


…or create a new repository on the command line
echo "# learningprojects" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/shaherfaheem/learningprojects.git
git push -u origin main


…or push an existing repository from the command line
git remote add origin https://github.com/shaherfaheem/learningprojects.git
git branch -M main
git push -u origin main


…or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.

