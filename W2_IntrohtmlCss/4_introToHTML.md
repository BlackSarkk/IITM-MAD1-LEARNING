
# HTML (HyperText Markup Language)
- HTML first used by Tim-Berners-Lee in orignal Web at CERN (~1989)
- Consider an application of SGML (Standard Generalized Markup Language)
    - Strict definitions on structure, syntax, validity
- HTML meant for browser interpretation
    - Very Forgiving: loose validity checks
    - Best effort to display


# HTML example:
```html
<!DOCTYPE html>
<html>
    <body>
        <h1>My First Heading</h1>
        <p>My First Paragraph</p>
    </body>
</html>
```

# Tags:
- <h1> </h1> - paired tags
- Angle brackets < > 
- Closing tag with /
- Location specific: <!DOCTYPE>: only at head of doc
- Case-insensitive**


# Nesting:
- <em><strong>Hello</em></strong>


# Presentation vs Semantics:
 <strong>
- Semantic tag
- Indicates importance, emphasis, or strong meaning
- Browsers typically render it as bold, but the meaning is more important than the appearance
- Good for titles, warnings, key points, or anything that needs logical emphasis

 <b>
- Presentational tag
- Simply makes text bold with no semantic meaning
- Good when you want visual boldness without implying importance or emphasis
- (e.g., keywords in a UI, product names, or stylistic bold text)


# TimeLines:
- SGML based
    - 1989 - HTML orignal
    - 1995 - HTML 2
    - 1997 - HTML 3, 4
- XML based
    - XHTML - 1997 - mid 2010s
- HTML 5
    - first release 2008
    - W3C recommendation - 2014


# HTML5
- Block elements: <div>
- Inline elements: <span>
- Logical elements: <nav>, <footer>
- Media: <audio>, <video>

Remove "presentation only" tags:
- <center>
- <font>


# DOM
- Tree Structure representating logical layout of document
- Direct Manipulation of Tree possible!
- Application Programming Interface(APIs)
    - Canvas
    - Offline
    - Web Storage
    - Drag and Drop
    - ...
- Javascript primary means of manipulating
- CSS used for styling




