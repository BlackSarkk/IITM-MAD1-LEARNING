
# M-V-C (Model view controller)
- The core idea of MVC have its origin in late 70-80s 
- There was a language called "Smalltalk-80" that came out of Xerox in PARC (Plao Alto Research Corporation)
- Smalltalk was a very interesting kind of OOP language
- While developing smalltalk, they seperated the abstraction, which allowed this whole OOP nature i.e. we could have some object which could have a window as an object or we could also have an object which represent some kind of data/model which can be manipulated by sending messages from one part to another.
- Roots in Object-Oriented GUI development



# Design Pattern
- Several software designers have found that some design patterns are more efficient over others and are very effictive in getting certain properties implemented. And those learnings over the years are abstracted out into various kinds of design patterns. 

- MVC is not essentially a design pattern, its more like a combination of common software pattern
- Both model and view can be thought of as an object
- `Model`: Application Object -- Whatever it is that you're trying to manipulate
- `View`: Screen representation -- buttons, layout, touch, audio, visuals, etc
- `Controller`: How user interface reacts to user input

- We should keep in mind while building a controller in a webapp.
- There is two parts where the user is interacting with the application.
    - When they are consuming what is shown, they're actually seeing what we put on screen
    - When they are actually giving the inputs, like pressing buttons, clicking on links, entering text into text boxes




# Example: 'Student Gradebook'
- In the student marks example, the model is the underlying gradebook data in spreadsheets, the view is the different ways of displaying that data (like tables or charts), and the controller is the logic that responds to user actions to fetch or modify data for those views.​


- Model (student grade data)
    - The model consists of three logical pieces of data stored in spreadsheets: a list of students with IDs, a list of courses with IDs, and a table linking student IDs, course IDs, and marks.​
    - Design questions like whether IDs are needed, how to ensure uniqueness, and how to prevent duplicate marks entries for the same student–course pair are all part of modeling the data correctly.​

- View (how data is shown)
    - A view is any particular representation of this model, such as a table showing all marks for one student given their ID, including their name, registered courses, and marks in each course.​
    - Other possible views include course-wise summaries (number of registered students, highest/lowest marks, histograms, bell-curve-like distributions, cut-offs) or representations as tables, plots, plain text, or JSON for further processing.​

- Controller (connecting user and data)
    - The controller is the part that reacts to user input (like entering a student ID or course ID, clicking buttons, or submitting forms) and then fetches or manipulates data in the model to update the view.​
    - In this gradebook application, controller functionality would include adding/modifying students and courses, entering marks, and triggering the appropriate views to be generated automatically instead of manually copy–pasting in a spreadsheet.​







