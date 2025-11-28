


# Discoveries:

We can shove direct logics inside css:

'''html
<style>

tr:nth-child(odd)  { background: #fff; }
tr:nth-child(even) { background: #f2f2f2; }


li:nth-child(3n + 1) { color: red; }          /* → 1st, 4th, 7th, 10th… */
li:nth-last-child(2) { font-weight: bold; }   /* selection from the end */
:nth-of-type()                                /* Based on the tag types */
:nth-last-of-type()                           /* Based on the tag types */


.card:has(img) {                               /* Conditional Logic */
  border: 2px solid blue;
}


input:has(+ label) {                           /* Style an input if it is empty (conditional logic)*/
  margin-bottom: 10px;
}   


a[href^="https://"]  { color: green; }   /* starts with (Attributic logic) */      
a[href$=".pdf"]      { color: red; }     /* ends with   (Attributic logic) */
a[href*="login"]     { color: orange; }  /* contains    (Attributic logic) */


@media (max-width: 600px) {             /* Media Queries */
  body { background: #222; }
}


@container (min-width: 400px) {         /* Like media queries but per component, not per screen. (Container Queries) */
  .card { flex-direction: row; }
}


@supports (backdrop-filter: blur(10px)) {           /* “IF the browser supports X, then apply Y.”  (Feature Queries)*/
  .glass { backdrop-filter: blur(10px); }
}


width: calc(100% - 50px);                           /* Calculations */
font-size: clamp(1rem, 2vw, 2rem);


li.selected:last-child {              /*highlight the last item only if it’s selected*/
  background: yellow;
}


input:invalid ~ .error {            /* Form logic without JS */
  display: block;
}


</style>
'''