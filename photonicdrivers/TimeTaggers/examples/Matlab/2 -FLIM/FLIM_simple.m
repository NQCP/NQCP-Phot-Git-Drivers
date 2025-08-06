disp('This is an example not including the binary dump file required for the analysis.')
disp('Please contact the support@swabianinstruments.com for further assistance.')

% The data file is expected to be in the Downloads folder of your Windows User.
% You have to modify this path to the Pollen_Galvo_c.1.ttbin file if you stored it elsewhere.
data_file = [getenv('USERPROFILE'), '/Downloads/Pollen_Galvo_c.1.ttbin'];

% defining the channel numbers and parameters
laser = 1;
click1 = -2;
click2 = -3;
frame = 4;
pixel = 5;
line = 6;
bins = 100;
binwidth = 125;
xDim = 513;
yDim = 513;

laser_frequency = 80e6;
total_frames = 2;

disp('Initiating the TimeTagger Virtual and defining the FLIM objects.')
ttv=TimeTagger.createTimeTaggerVirtual();
ttv.setInputDelay(laser, -1/laser_frequency*1e12)
flim1 = TTFlim(ttv, laser, click1, pixel, xDim*yDim, bins, binwidth, ...
    TimeTagger.CHANNEL_UNUSED, frame, total_frames, 1);
flim2 = TTFlim(ttv, laser, click2, pixel, xDim*yDim, bins, binwidth, ...
    TimeTagger.CHANNEL_UNUSED, frame, total_frames, 1);

disp('Reading the dumped binary file.')
replay = ttv.replay(data_file);
ttv.waitForCompletion();


%convert into 2D images and take out the first pixel row and line
frames1 = [];
for i=0:total_frames-1
    base_frame = flim1.getReadyFrameEx(i);
    sums = base_frame.getIntensities();
    trans = reshape(sums, xDim, yDim);
    frames1 = cat(3, frames1, trans);
end

frames2 = [];
for i=0:total_frames-1
    base_frame = flim2.getReadyFrameEx(i);
    sums = base_frame.getIntensities();
    trans = reshape(sums, xDim, yDim);
    frames2 = cat(3, frames2, trans);
end

disp('Plotting the FLIM images from the different detectors.')
figure(1)
imagesc(frames1(:,:,1))
xlabel('pixel x');
ylabel('pixel y');
cb = colorbar;
ylabel(cb, 'life time (ps)');

figure(2)
imagesc(frames2(:,:,1))
xlabel('pixel x');
ylabel('pixel y');
cb = colorbar;
ylabel(cb, 'life time (ps)');
