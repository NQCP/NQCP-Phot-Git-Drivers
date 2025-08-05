%% Network Time Tagger - server example
% Connects to a Time Tagger hardware and starts the server.
% See also: client.m
%

disp('*****************************')
disp('*    Time Tagger Network     ')
disp('*      Server example        ')
disp('*****************************')

tagger=TimeTagger.createTimeTagger();
tagger.setTestSignal([1, 2, 3, 4], true)

% Start the server. Now use the client.py script to connect a client
tagger.startServer(TTAccessMode.Control)
disp('Time Tagger server started successfully on localhost (127.0.0.1) and the default port 41101.')

disp('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
disp('+  Now you can run the "client.m" in the same or in a separate Matlab process.  ')
disp('+  Or you can use any other client example from a different language.           ')
disp('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

% Please stop the server and free the TIme Tagger after you have done with
% the client example. Alternatively you can uncomment the following lines.

% input('Press ENTER to stop the server...', 's');
% tagger.stopServer()
% freeTimeTagger(tagger);
% clear tagger