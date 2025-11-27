

# What is web server?
- Any old computer with a network connection can act as a server
- Software
    - Listening for incomming network connections on a specific port
    - Respond in specific ways
    - Opening network connections, ports, etc already known to OS

- Total number of logical ports = 2^16 = 65,536
- Total PHYSICAL PORT => varies per PC

- LOGICAL PORT number = 0 - 65,535 => network communication endpoints
- PHYSICAL PORTS => hardware ports => for hardware connections


# What is a transport protocol?

- Protocol
    - What should client ask server
    - How should server respond to client

- This protocol of how the client communicate to server and server respond to client ika HTTP

# HTTP:
- HyperText:
    - Regular text document
    - Contains "codes" inside that indicate special functions - how to "link" to other documents    

- HyperTextTransferProtocol:
    - Largely text based: client sends requests, server responds with hyperText doc

- So the client sends request to the server
- Server returns an HTML document that can contain text, links, images, styles, and scripts.