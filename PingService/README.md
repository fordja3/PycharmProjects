1. The first of the two services is called PingService and the second PongService. 
The PingService has a HTTP GET endpoint called ping and the PongService a HTTP GET endpoint called pong.
Both ping and pong do not require any input data. When ping receives a request, it, in turn, makes a
GET request to pong, records the time it takes to complete the request (in milliseconds) and returns a
JSON payload with a single value pingpong t. 
The other end point pong either returns some dummy data or no data at all.
2. Both of the services use HTTP Digest Authentication, with a default username/password pair set to
vcu and rams.
3. Both services are deployed to Heroku and available to be contacted from anywhere. You should be
able to create a free Heroku account that would allow you to do this."