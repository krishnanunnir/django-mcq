# __Created By__  
 * Krishnanunni  
 * Computer Science  
 * College Of Engineering trivandrum

Python 2.7 has been used for the project. A virtualenv with python2.7 installation and the requirements can be instantiated as such  
```
 virtualenv --python=/usr/bin/2.7 <src-to-directory>
 source <src-to-directory>/bin/activate
 pip install -r requirements.txt   
```
Using sqlite database for development.  
Secret Key should be stored and imported from the ```secret.py``` directory defined in root of the directory.  
The database ```db.sqlite3``` is used by default. The database setting can be changed by setting the ```database.py``` file at the root. 

For further documentation refer the documentation.md file.