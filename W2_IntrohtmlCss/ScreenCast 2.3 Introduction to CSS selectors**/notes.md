

# Descendent vs Children

- Children
    - Direct child elements.
    - One level down.
    - Example:

```html
<div>
  <p></p>   <!-- child of div -->
</div>
```
Here, <p> is a child of <div>.



```css
div > p {
  color: red;   /* only p that are DIRECT children of div */
}
```










- Descendants
    - All elements inside, no matter how deep.
    - Children, grandchildren, great-grandchildren… everything.
    - Example:
```html
<div>
  <section>
    <p></p>   <!-- descendant of div (but NOT a child) -->
  </section>
</div>
```

- Here: 
<section> → child of <div>

<p> → descendant of <div> (because it’s inside it),
but not a child, since it’s two levels down.



```css
div p {
  color: blue; /* all p inside div, any depth */
}
```








read bout pseudo element selectors:
::before
::after
::first-letter
::first-line
::selection
::placeholder
::marker

