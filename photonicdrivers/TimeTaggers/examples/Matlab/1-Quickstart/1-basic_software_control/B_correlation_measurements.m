%Cross correlation between channels 1 and 2
%binwidth=1000 ps, n_bins=3000, thus we sample 3000 ns
%we should see the correlation delta peaks at a bit more than 1000 ns distance

disp('*************************************');
disp('*** Demonstrate cross correlation ***');
disp('*************************************');
disp(' ');
disp('Create a cross correlation on channels 1 and 2 with 1 ns binwidth and 3000 points.');
disp(' ');

% create a TimeTagger instance
tagger=TimeTagger.createTimeTagger();

% apply the built-in test signal to channels 1 and 2
disp('Enabling test signal on channels 1 and 2.'); disp(' ');
tagger.setTestSignal([1,2], true);
pause(.1);

corr = TTCorrelation(tagger, 1, 2, 1000, 3000);
corr.startFor(1e12) % 1s
corr.waitUntilFinished();
figure(2)
plot(double(corr.getIndex())/1e3, corr.getData())
xlabel('Time (ns)')
ylabel('Clicks')
title('Cross correlation between channel 1 and 2')
text(-1050,max(corr.getData())*0.8, { ...
'The built-in test signal',...
'is applied to channel 1', ...
'and channel 2.' ...
'The peak distance',...
'corresponds to the' ...
'test signal period.' });
text(100,max(corr.getData())*0.8, { ...
'The decreasing peak heights', ...
'and broadening of the peaks', ...
'reflect the jitter of the built-in', ...
'test signal, which is much larger', ...
'than the instrument jitter.'});


% cross correlation between channels 1 and 2
% binwidth=10 ps, n_bins=400, thus we sample 4 ns
% The standard deviation of the peak
% is the root mean square sum of the
% input jitters of channels 1 and 2
disp('Create a cross correlation on channels 1 and 2 with 10 ps binwidth and 400 points.'); disp(' ');
corr = TTCorrelation(tagger, 1, 2, 10, 300);
corr.startFor(2e12) %2s
corr.waitUntilFinished();
figure(3)
plot(corr.getIndex(), corr.getData())
title('High res cross correlation showing <60 ps jitter')
xlabel('Time (ps)')
ylabel('Clicks')
text(-1450,max(corr.getData())*0.5, { ...
'The half width of the peak is', ...
'sqrt(2) times the instrument jitter.', ...
'The shift of the peak from zero', ...
'is the propagation delay of the', ...
'built-in test signal.'});

freeTimeTagger(tagger);