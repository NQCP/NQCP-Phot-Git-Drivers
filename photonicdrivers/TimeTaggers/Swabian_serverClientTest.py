import TimeTagger

tagger = TimeTagger.createTimeTaggerNetwork('10.109.67.53:41101')
# Connect to the Time Tagger server. 'ip' is the IP address of the server and 'port' is the port defined by the server. The default port is 41101

correlation = TimeTagger.Correlation(tagger=tagger, channel_1=1, channel_2=2, binwidth=1, n_bins=1000)
# tagger can be used to perform measurements as if the client was connected to the TimeTagger via USB. In this case, the client starts a correlation measurement.
# After a measurement is finished, the client can disconnect with TimeTagger.freeTimeTagger(tagger)

TimeTagger.freeTimeTagger(tagger)