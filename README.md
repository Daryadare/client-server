# client-server
  Client-server application realized through sockets in Python. Servers are multithreaded and support several active connections that are handled in the order 
  of the queue. Servers work with system Windows information. Response from server includes current date and time and comes only after client's query. After 
  disconnection from server client can connect to another one or even the same server. Client disconnects completely only by it's own choice. Servers can't close 
  client same as client can't close the server.
    
  Client's part can be launched from Linux system and connect to the active server working in Windows.
