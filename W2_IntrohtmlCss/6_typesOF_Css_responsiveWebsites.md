
# Inline CSS:
- Directly add style to the tag
- Example: <h1 style="color:blue; text-align:center">A heading</h1>



# Internal CSS:
- Embed inside <head> tag
- Now all <h1> tags in document will look the same - centrally modified

<style>
body {
    background-color: linen;
}

h1{
    color: maroon;
    margin-left: 40px
}
</style>


# External CSS:
- Extract common content for reuse
- Multiple CSS file can be included
- Latest definition of style takes precedence


# Responsive Design:
- Mobile and Tablets have smaller screens
    - Different form factors
- Adapt to screen - Respond
- CSS control styling 
- HTML controls content!


# Bootstrap:
- Commonly used framework
    - Originated from Twitter
    - Widely used now
- Standard sytles for various componenets
    - Buttons
    - Forms
    - Icons
- Mobile first: Highly responsive layout


# Javascript:
- Interpreted language brought into the browser
- Not really related to JAVA in any way - formally ECMAScript
- Why?
    - HTML is not a programming language
    - CSS is not a programming language, but with modern features it sometimes behaves in ways that resemble programming. Still, its purpose and design remain non-programmatic, it was never meant to be used as a programming language.
- Would still like to have "programmability" inside browser
- Not part of the core presentation requirements
    - Very useful, but will be considered later
