
# How fast a site can be
# What are things that limits the performance?

- Latency - How much time does it takes to get a response for a given request
    - Speed of light: 3e8 m/s in vacuum, ~2e8 m/s on cable
        - 5ns/m => ~ 5ms for 1000km
    - Data center 2000km away
        - One way request ~ 10ms
        - Round trip ~ 20ms
    - Max 50 requests /seconds
    - Even if the speed of light is unimaginable, it still a limiting factor here

- Response size 
    - Response = 1KB of text(headers, HTML, CSS, Js)
    - Network connection = 100Mbps ~ 10MBps
    - 10MBps ~ 10,000 requests/seconds  
    - So our entire pipe of 10MBps is not fundamentally capable of handling 10,000 requests / sec
    - Now if everyone connects to the server at the same time during examinations and all
    - Server cant handle the load => **Server crashes


- Google response
    - Header ~ 100B
    - Content ~ 144KB
    - Approx 60,000 requests per second (maybe) ~ 80Gbps bandwidth
    - Surely this kind of speed isnt achievable from single datacenters, they have distributed datacenters for that

- Memory - Youtube
    - One python HTTP server process: ~6MB (measured)
    - Multiple parallel requests: multiple processes
        - eg: YouTube will have long running server processes
    - 2016 Presidential debate in US:
        - ~ 2 Million concurrent viewers
        - 2M x 6MB = 12TB RAM
        - Big servers have like 30-60GB rams
        - So they surely have multiple distributed servers

- Storage - Google
    - Index 100s of billions of web pages 
    - Cross-reference, pageranks
    - Total index size estimate: 100,000,000 GB => 100Petabytes
    - Storage?
    - Retrieval would be challenging
    - So they have multiple distributed servers for this

# Summary:
- The web is a useful device/OS agnostic platform for apps
- Built on HTTP for transport, HTML and related tech for presentation
- Servers trivial at most basic
- Scaling requires careful design

                

