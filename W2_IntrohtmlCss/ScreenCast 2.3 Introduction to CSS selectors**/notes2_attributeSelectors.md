

# What Are Attribute Selectors in CSS?

- They target HTML elements based on the presence or value of an attribute.

Example:

```css
input[type="text"] {
  background-color: yellow;
}
```

This selects:
<input type="text">


<!--**************************************************  -->


# Types of Attribute Selectors

## [attr] — Attribute Exists
- Selects elements that have the attribute (any value).

```css
input[required] {
  border: 2px solid red;
}
```

Matches:
<input required>
<input required="true">

<!--**************************************************  -->


## [attr="value"] — Exact Match
- Selects elements whose attribute exactly matches the value.

```css
a[target="_blank"] {
    color: green;
}
```

<!--**************************************************  -->


## [attr~="value"] — Contains Word
- Matches when the attribute contains the value as a whole word, separated by spaces.

```css
div[class~="box"] {
  border: 1px solid black;
}
```

Matches:
<div class="big box special"></div>

Does NOT match:
<div class="boxy"></div>


<!--**************************************************  -->


## [attr|="value"] — Starts With Value (Hyphen Allowed)
- Common for languages.

```css
p[lang|="en"] {
  color: blue;
}
```

Matches en, en-US, en-UK


<!--**************************************************  -->


## [attr^="value"] — Starts With
- Target attribute values that start with something.

```css
a[href^="https"] {
  font-weight: bold;
}
```

Matches:
https://google.com

Not matches:
http://example.com


<!--**************************************************  -->


## [attr$="value"] — Ends With

```css
img[src$=".png"] {
  border: 2px solid green;
}
```

<!--**************************************************  -->


## [attr*="value"] — Contains Substring
- Checks ANY substring, not just a word.

```css
a[href*="login"] {
  color: red;
}
```

Matches:

/user/login
/login/settings
/my-login-page