
# Simplest server:
```bash
while true; do
    echo -e "HTTP/1.1 200 OK\n\n $(date)" | nc -lN localhost 1500;
done
```

```bash     **do this in another terminal
curl http://localhost:1500
```

- here first part is kinda server, which is responding with HTTP statusCode: 200 OK, and the response is date
- second part is the client that will take some information from the server 

- nc will ask the OS to open and listen on port 1500 and anytime the request comes from port 1500, that will feed to nc
- now nc will take whatever came from the echo send it out to whoever asks it anything on port 1500
- now whenever a client will hit the port 1500, they will receive current date as response 


- echo -e: just prints it out in the screen but in unix system it prints it out in stdout(standard output)
- PIPE(|): do something in the first part and pipe that info in the second part
           so in this case instead of sending the output of echo on the screen, it goes to the second part
- nc: netCat 
- l: listen
- N: makes nc close the connection


# What the previous code does:
- Listen on a fixed port
- On incomming request, run some code and return a result
    - Standard headers to be sent as part of result
    - Output can be text or other format - MIME (Multipurpose Internet Mail Extension)




