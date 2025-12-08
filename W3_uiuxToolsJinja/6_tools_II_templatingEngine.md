
# Programmatic HTML generation: pyHTML
- Generating HTML template using python
- Composable functions - each function generates a specific output

- Example:
    - to generate a h1 heading: function should return
        "<h1>Text of heading</h1>"
    - This might look like:

    ```py
        def h1(string):
            return "<h1>" + string + "</h1>"
        h1("Hello")  --> "<h1>Hello</h1>"
    ```




- Example code:

```py
import pyhtml as h

t = h.html(
    h.head(
        h.title('Test page')
    ),
    h.body(
        h.h1('This is a title'),
        h.div('This is some text'),
        h.div(
            h.h2('inside title'),
            h.p('some text in a paragraph.')
        )
    )
)

print(t.render())

```

- That looks nice, but theres still a question whether it is scalable
- It would be difficult update things here, due to clutterings and all




# More complex HTML:
```py
def f_table(ctx):
    return (tr( td(cell) for cell in row ) for row in ctx['table'])
``` 
- It is possible to generate something fancy like this using libery function called pyHTML



# Templates:
- Standard template text
- Placeholders/Variables
- Basic (very limited) programmability
- Examples:
    - Python inbuilt String Templates - good for simple tasks
    - Jinjs2 - Used by Flask
    - Genshi
    - Mako
    - ... - just pick one and go with it


```py
from string import Template

t = Template('$name is the $job of $company')
s = t.substitute(name='Tim Cook', job='CEO', company='Apple Inc.')
print(s)
```


# Jinja:
- Ties in closely with Flask
- Template funtioinality with detailed API
- Remember: Templates can generate any output, not just HTML
- Jinja is a templating engine

```py
from jinja2 import Template
t = Template("Hello {{ something }}!")
print(t.render(something="World"))
'''
Hello World!
'''


t = Template("My favourite numbers: {% for n in range(1, 10) %}{{n}} " "{% endfor %}")
print(t.render())
'''
My favourite numbers: 1 2 3 4 5 6 7 8 9 
'''

```