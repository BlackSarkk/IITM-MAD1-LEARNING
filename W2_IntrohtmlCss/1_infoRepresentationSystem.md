
# Markup
- Markup is something that is used in order to change the way something is shown to the user
- And ultimately deals with the asthetics of how something look

# Information representation
- Computers works only with "bits"
    - Binary digits: 0 and 1

- Numbers
    - Place value: binary number: eg. 6 = 0110
    - Two's complement: negative numbers: eg. -6 = 1010 (if it is 4 bit twos complement number) 
                                              10 = 1010 (if it is 4 bit unsigned number)

- Letters? Arbirary Text?
    - Representing Text
        - ASCII
        - Unicode
        - UTF-8

    - Information Interchange
        - Communicate through machines - either between machines or between humans
        - Machines only work with bits
        - Standard "encoding"
            - some sequence of bits intrepreted as a character
        
    - Interpretation
        - What is "0100 0001"?
            - String of bits
            - Number with value 65 decimal
            - Character A
            - All of the above are correct

        - Matter of 'intrepretation' and 'context'
            - If we see it in a random wall, we cant say what it is, just a random string of bits
            - If we see it in something which is discussing binary arithmatics, we'll interpret it as the number 65
            - If we see it which is talking bout character encoding, and letters, we'll take it as character A
        - So the context makes a big difference of how we interpret things
        - And computer donot put these in any random memory location, they surely put it somewhere where it is meant to be in
        - Computer interprets if certain string of bits is char or int by using the context of the program 
        - Which means is, if we go to such memory location, we can interpret if it is a number or character or just random bits
        
    - ASCII(American Standard Code for Information Interchange)
        - It is a standard of code which tells us how certain set of bits should be interpreted
        - Why 7 bits?
            - 7 bits: 128 different entities
                - 'a'...'z'
                - 'A'...'Z'
                - '0'...'9'
                - Special characters: !@#$%^&*(), space, comma, enter, etc 

        - What bout other lang?
            - For a long time ASCII was working preety well
            - but then after other people like eurpeans got fedup, as they have some other special characters in their lang, and various other things, Which meant that there was a need of something like extended ASCII format which was of 8Bits where you can go upto like 256 characters, that is enough for romans, latins chars to fit in
            - But there are various other languages: Hindi, Tamil, Bangla, mandarin, Thai, etc
            - 1000s of characters needed
            - The whole point was to have a standard sytem of communication so everyone in the world can talk to each other in a fixed encoding

        - UNICODE
            - Allow codes for more scripts, characters
            - How many?
                - All living languages? All extinct languages? All future languages?
            - "Universal Character Set" encoding - UCS
                - UCS-2: 2bytes per character - max 65,536 characters
                - UCS-4: 4bytes per character - max 4Billion+ characters
                    - Is it enough? - we never know as of now
                - In present, 1 hundred thousand are defined






