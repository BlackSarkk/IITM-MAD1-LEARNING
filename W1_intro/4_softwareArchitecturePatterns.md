
# What is a design pattern?

- Its a general reusable solution to a commonly occruing problem within a given context in software design
- Basically experienced devs has some good code designs which they improved over time, newbye can use these design as best practices

- Experienced designers observs 'patterns' in code
- Reusing these patterns can make desgin and development faster
- Guide the design and thought process
- SOME design patterns are: MVC(Model-View-Controller), 
                            MVA(Model-View-Adapter), 
                            MVP(Model-View-Presenter), 
                            HMVC(Hierarchial MVC), 
                            PAC(Presentation-Abstraction-Control), 
                            MVVM, etc


<!--*****************************  -->
<!--*****************************  -->



# Software Architecture Patterns:

## M-V-C Paradigm
- Not the best one in the market
- but good enough to easily learn how things works
- Core concept of MVC is: 
        the user --> uses controller --> To manipulate model --> that updates view --> that user sees
- So this is kind of a closed feedback loop


- Model:
    - Core data to be stored for the application
    - This can be done using dataBase (SQL, MYSQL, etc)
    - Databases, indexing for easy searching, manipulation

- View:
    - User-facing side of application
    - Interfaces for finding information, manipulating.
    - A view need not necessarily be something you see, like audio based interface like alexa comes in the view category

- Controller:
    - "Business logic" - how to manipulate data
    - They tells the system how to actually manipulate the data
    - Like we give a command to delete something, controller gives the logic to system of what needs to be done




<!--*****************************  -->
<!--*****************************  -->

# Focus Of This Course
- Platform : WEB-based
- Architecture: Client-Server
- Software Architecture: MVC

- How to build apps that are web-based with central servers, use hypertext markup to control and manipulate display