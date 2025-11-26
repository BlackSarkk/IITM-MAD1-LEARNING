

# Architectures
- Client Server architecture
- Distributed or Peer to Peer architecture

<!--*******************************************  -->
<!--*******************************************  -->

# ClientServer:
- Server - Store Data; Provides data on demand; May perform computation
- Client - End user; Requests data; UI, display
- Network - Connect the client to the server; Can be local; Data Pipe - no alteration

        CLIENTs <---> NETWORK <---> SERVER

- Any request or info that a client puts in to the network is supposed to pipe through the server without really gets modified in by the client
- Its the server that decides what to do with that information
- Once the server responds, the responce should reliably come back to the client

- This model has explicit differentiation btw the client and server so we can identify btw client and server

## Local systems:
- Both client and server are on the same machine - local Network / Communication
- Conceptually still a networked system

## Machine client:
- Eg: Software / Anitvirus updaters
- Need not have user interaction

## Variants: 
- Multiple servers, single queue, multiple queues, load balancing frontends

## Examples:
- Email, Database, Whatsapp / messaging, Web browsers


<!--*******************************************  -->
<!--*******************************************  -->

# Distributed or Peer to Peer architecture
- We cant really tell which is client and which is server

- All peers are considered "equivalent", some peers may be more equal than others
- Error Tolarance: Master/introducer, Election/re-selection of master on failure
- Shared Information

Ex: bit Torrent, BlockChain based system, distributed file system
