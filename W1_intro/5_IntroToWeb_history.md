
# Why web?
- Platform of choice for this course
- Generic - works across OS, Hardware architecture, basically CROSS PLATFORM OS
- Good Understanding of costs balancing: storage, network, device-sizing, datacenter


<!--********************************  -->
<!--********************************  -->


# Historical Background:

## TELEPHONE NETWORKS ~ 1890+
- TELEPHONE: Circuit Switched Network
- Make sure that both A and B connected through wires, to make them talk
- Send analog sound signal through wires, so only one call at a time
- Also the physical wires tied up for the duration of call means, nobody else can use them in between


## PACKET SWITCHED NETWORK ~ 1960s
- Wires occupied only when data to be sent - more efficient
- Data instead of Voice
- The concept was, you break the voice into small packets of computer data, then those packets are sent to the wires instead of the direct analog signals
- Now a single wire btw two exchages can carry several different convo
- This leads to make them think to send other types of data like image, file over wires just like they did for voice

- NOW this leads to the formation of NETWORK that is neutral to the type of data
- No matter what, the wires are same of every types of data (voice, video, text, img, etc)

## ARPANet ~ 1969
- Node-to-Node network
- Mostly university driven
- Others: IBM SNA, Digital DECNet, Xerox Ethernet
- This leads to the formation of protocol:
    - How to format packets, place them on wire, headers/checksums
    - Each network had its own protocol
- But the problem was each of them had their own algo of packing data and sending over the wires
- This means no two companys could talk to each other as they have complete different network algorithms

## "INTER" network:
- The idea was to put a layer on top of the existing protocol
- Now they can talk to each other as the top layer now take the input and gives a standard output which everyone can read

## IP: Internet Protocol ~ 1 JAN 1983
- Defines headers, packet types, itnerpretation
- Can be carried over different underlying networks: ethernet, DECnet, PPP, SLIP

## TCP: Transmission Control Protocol ~ 1 JAN 1983
- Establish reliable communication - retry, error control
- Automatically scale and adjust to network limits
- means: Try sending data faster and faster until you get failure then backoff a lil bit to send data in fastest possible speed
- Still TCP/IP is kinda backbone of the whole internet

## Domain Names ~ 1985:
- Now people can now talk to one another, but the problem was one still needed to know the IP address of the other machine
- Which was tough to remember
- One more advantage in domain names is one can change the existing device without worrying about their IP address will change

- So they started using Domain Names instead of IP addresses
- Easy to remember - .com revolution still in the future

## HyperText ~ 1989+
- In general "Text" is a set of alphabets, text by itself is just a pile of raw data, it doesn't tells us what to do of the information
- The idea was to embed hints as texts in a text document itself
- Now if you have a program that can read these texts and identify the hints, it will tell us what part needs to be bold, what part need to be on top, what should be the color of the text here, this part leads to a hyperlink, 
- An hyperlink tells pc, the immediately appearing texts after the hyperlink corresponds to an another file, this is a name of the file you need to load
- This Business of linking documents ika "HyperText"
- Which leads to the formation of "THE WORLD WIDE WEB" ~ The WEB
- The WEB means the networks of documents
- The Internet means the network of servers that are connected to each other

- Text documents to be "served"
- Formatting hints inside documents to "link" to other documents - HyperText


<!--********************************  -->
<!--********************************  -->


# BACK THEN:
- ORIGNAL web limits:
    - Static Pages
    - Complicated executable interface
    - Limited Styling
    - Browsers compaitability issues

# WEB 2.0 ~ 2004+
- dynamic pages - generate on the fly
- HTTP as a transport mechanism - binary data, serialized objects
- client side computation and rendering
- Platform agnostic OS
- Servers are no longer just serving the files, they are actully computing and generating relevent information for the client
- Now one can write the code of the web without worrying what kind of machine the client has
