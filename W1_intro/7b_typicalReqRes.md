

# Typical request:

```bash
GET / HTTP/1.1              <-- This is the actual request
Host: localhost:1500        <-- These are just headers
User-Agent: curl/7.64.1     <-- These are just headers
Accept: */*                 <-- These are just headers
```

# Viewing response with curl:
- curl, wget etc - Simple command line utilities
- Can perform full HTTP requests
- Verbose output includes all headers
- Very useful for debugging

```bash
curl -v http://localhost:1500
```


# How response looks like:
```bash
*    Trying ::1...      # <-- IP ADDRESS
* TCP_NODELAY set       # some part of TCP settings, that maybe tries to get the maximum data transfer speed
* Connected to localhost (::1) port 1500 (#0)    
GET / HTTP/1.1              # This was sent from curl to the server, this line specifies the type of request: GET / i.e. gimme root info, its also mentioning the protocol using is HTTP1.1
Host: localhost:1500        # This was sent from curl to the server
User-Agent: curl/7.64.1     # This was sent from curl to the server    
Accept: */*                 # This was sent from curl to the server
>                           # This blank line is important, unless you give the blank line, the server doesnot know you're done 
< HTTP/1.1 200 OK           # This is the response, It will alwasys respond with 'HTTP/1.1 200 OK' as we've hard coded it there in the code    
* no chunk, no close, no size. Assume close to signal end   # It just curl saying, i reached the end i dont see anything else
< 
 Thu Nov 27 12:49:46 PM IST 2025  # Response
```




- '*' lines are just debug information, not part of the protocol, not used by computer



