# __Created By__  
 * Krishnanunni  
 * Computer Science  
 * College Of Engineering trivandrum

Using an sqlite for development.  

## Documentation for MCQ

* April 1 2017
* Started the project mcqfoss.
* Created an app "exam"
* Added exam to list of installed apps in Settings.
* Added the models in models.py of exam. They are

## Questions


| question_no     | question_text |   answer   |   options   |
|-----------------|---------------|------------|-------------|
| Integer         | Character     | Character  | Foreign Key |


## Tests


| test_title | teacher   |  date_of_exam   |  start_time  | end_time |     questions      |
-------------|-----------|-----------------|--------------|----------|--------------------|
| Character  | Character |       Date      |  Time        |  Time    | Many to Many Field |


## Department

| dept_code |
|-----------|
| Character |

## Student

|        user       |  department  |
|-------------------|--------------|
| Many to Many Field|  ForeignKey  |

## Testscore

|  student  |   test   | test_score|
|-----------|----------|-----------|
| ForeignKey|ForeignKey| Integer   |


* Migrated the data to database.
* A template folder was added in settings. "template" in root  of the project.
* Added a  controller function in view(tests). It returns list of all elements in Tests model.
* Created a template tests.html renders the view tests.
* Display all the tests in tests.html.
* Created a template question_pages.html.Using URI offsetting to go to a test and particular question.
* question_pages.html display the first question.


* Added April 4th and 5th 2017

* Created an app authentication.
* Authentication defines Student which inherits from user.
* Another model class for defining departments.
* Another model class for storing test scores.
* The newly created model classes have been registered at admin.py.
