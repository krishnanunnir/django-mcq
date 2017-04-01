__#Created By__  
 * Krishnanunni  
 * Computer Science  
 * College Of Engineering trivandrum

Using an sqlite database temporarily.  

##Documentation for MCQ

* Started the project mcqfoss.
* Created an app "exam"
* Added exam to list of installed apps in Settings.
* Added the models in models.py of exam. They are

##Questions

--------------------------------------------------------------
| question_no     | question_text |   answer   |   options   |
|-----------------|---------------|------------|-------------|
| Integer         | Character     | Character  | Foreign Key |
--------------------------------------------------------------

##Tests

-------------------------------------------------------------------------------------------
| test_title | teacher   |  date_of_exam   |  start_time  | end_time |     questions      |
-------------|-----------|-----------------|--------------|----------|--------------------|
| Character  | Character |       Date      |  Time        |  Time    | Many to Many Field |
-------------------------------------------------------------------------------------------

##Options

----------------
| option_value |
--------------
|  Character   |
----------------

* Migrated the data to database.
* A template folder was added in settings. "template" in root  of the project.
* Added a  controller function in view(tests). It returns list of all elements in Tests model.
* Created a template tests.html renders the view tests.
