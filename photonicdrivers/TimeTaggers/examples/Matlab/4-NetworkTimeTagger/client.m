%% Network Time Tagger - Client example
% Connects to a TimeTaggerNetwork server and performs a measurement.
% See also: server.m
%

disp('*****************************')
disp('*    Time Tagger Network     ')
disp('*      Client example        ')
disp('*****************************')

disp('Search for Time Taggers on the network...');
servers = TimeTagger.scanTimeTaggerServers();
disp([num2str(numel(servers)), ' servers found.'])
disp(servers)

disp('Information about Time Tagger server on localhost:')
try
    server_info = TimeTagger.getTimeTaggerServerInfo('localhost');
    disp(server_info(1:100))
    disp('...');
catch ME
    error('No Time Tagger server available on "localhost" and the default port 41101.')
end

disp('Connecting to the server on localhost.');

ttn=TimeTagger.createTimeTaggerNetwork('localhost');

% With the TimeTaggerNetwork object, we can set up a measurement as usual
crt = TTCountrate(ttn, [1, 2, 3, 4]);

crt.startFor(1e12);
crt.waitUntilFinished();
countrates = crt.getData();

disp('Measured countrates in Hz on channel 1-4:')
disp(countrates)

% Check for overflows
overflows = ttn.getOverflows();
if overflows == 0
    disp('All incoming data has been processed.')
else
    warning('%s\n         ', ...
        sprintf('%d data blocks are lost.', overflows), ...
        'Block loss can happen during the USB transfer ', ...
        'from the Time Tagger to the Time Tagger Server and/or during ', ...
        'the data transfer over the network from the Time Tagger Server ', ...
        'to the client. Overflows are caused by exceeding the processing ', ...
        'power (CPU) on the client and/or the server, the USB bandwidth, ', ...
        'or the network bandwidth.')
end

% Disconnect the client from the server
freeTimeTagger(ttn);
clear ttn
