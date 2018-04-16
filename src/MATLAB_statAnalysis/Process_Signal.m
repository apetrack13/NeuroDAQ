% Alec Petrack
% NeuroModQC
% Process Signal Data

clear all
warning('off', 'all');
close all
clc

%% Test parameters
     
impedance = 10000;                              % Test Impedance
frequency = input('Frequency in Hz: ');         % Frequency
duration = input('Duration of test: ');         % Duration of Test
maxCurrent = input('Total Current in mA: ');    % Current in mA
minCurrent = maxCurrent * -1;

fileName = input('Enter File Name in Double Quotes: ');
fileNameExt = fileName + ".csv";
data = load(fileNameExt);
numOfRows = size(data, 1);                      % Number of Rows of Data
numOfCols = size(data, 2);                      % Number of Columns of Data

%% Plot of high and low electrode voltages.

sizeData = size(data);
rowsData = sizeData(1);
x1 = linspace(0.5,0.5,rowsData);
x2 = linspace(-0.5,-0.5,rowsData);
x3 = linspace(0,0,rowsData);

channelLabelNum = 0;
i = 0;
for c = 1:2:numOfCols-2
    i = i + 1;
    channelLabelNum = channelLabelNum + 1;
    figure()
    h1 = plot(data(:, numOfCols), data(:, c));
    hold on
    h2 = plot(data(:, numOfCols), data(:, c+1));
    hold off
    nameOfTitle = "Channel " + num2str(channelLabelNum) + " High/Low Electrode Voltages";
    title(nameOfTitle)
    ylabel('Voltage (V)')
    xlabel('Time (s)')
    ylim([-4 4])
    yticks([-4 0 4])
    high_volt(i,:) = data(:, c);
    low_volt(i,:) = data(:, c+1);
    hold on
    h3 = plot(data(:, numOfCols),x3,'k');
    set([h3], 'LineWidth',2)
    legend([h1 h2],{'High Electrode', 'Low Electrode'});
    hold off
end

%% Plot current of channels.

channelLabelNum = 0;
for c = 1:2:numOfCols-2
    channelLabelNum = channelLabelNum + 1;
    figure()
    plot(data(:, numOfCols), ((data(:, c)-data(:, c+1))/impedance)*10^3)
    nameOfTitle = "Channel " + num2str(channelLabelNum) + " High/Low Electrode Current";
    title(nameOfTitle)
    xlabel('Time (s)')
    ylabel('Electrode Current (mA)')
    ylim([-.7 .7])
    yticks([-0.5, 0, 0.5])
    hold on
    plot(data(:, numOfCols),x1,'-.k');
    plot(data(:, numOfCols),x2,'-.k');
    h1 = plot(data(:, numOfCols),x3,'k');
    set([h1], 'LineWidth',2)
    hold off
end

%% Calculate trough/peak electrode current.

numOfMaxMinValues = (frequency * duration) / 2;
i = 0;
for c = 1:2:numOfCols-2
    i = i + 1;
    currentValues = ((data(:, c)-data(:, c+1))/impedance)*10^3;
    sortedCurrent = sort(currentValues);
    sizeOfArray = size(sortedCurrent);
    minCurrent = sortedCurrent(1:numOfMaxMinValues, 1);
    maxCurrent = sortedCurrent(sizeOfArray(1) - numOfMaxMinValues: sizeOfArray(1), 1);
    avgMinCurrent(i) = mean(minCurrent);
    avgMaxCurrent(i) = mean(maxCurrent);
end

%% Standard deviation calculations for channel trough/peak currents.

std_peak_current = std(maxCurrent);
std_trough_current = std(minCurrent);
 % Print std of high and low peak channel currents.
 size_minCurrent = size(minCurrent);
 size_maxCurrent = size(maxCurrent);
 fprintf('\n')
 
 for c = 1: size_maxCurrent(2)
     label = 'The peak current of Channel %i deviates %0.5f mA from the average current %0.3f mA \n';
     fprintf(label, c, std_peak_current(c),avgMaxCurrent(c))
 end
 fprintf('\n')
 for c = 1:size_minCurrent(2)
    label = 'The trough current of Channel %i deviates %0.5f mA from the average current %0.3f mA \n';
    fprintf(label, c, std_trough_current(c), avgMinCurrent(c))
 end

%% Calculate trough voltages of high/low electrodes.

% Sort high voltages and low voltages
sorted_high_volt = sort(transpose(high_volt));
sorted_low_volt = sort(transpose(low_volt));
% Size of voltage matrices.
size_high_volt = size(sorted_high_volt);
size_low_volt = size(sorted_low_volt);
% Get number of cols for high and low electrodes.
num_cols_high_volt = size_high_volt(2);
num_cols_low_volt = size_low_volt(2);
% Get number of rows for high and low electrodes.
num_rows_high_volt = size_high_volt(1);
num_rows_low_volt = size_low_volt(1);
% Grab high and low electrode voltage troughs.
high_volt_troughs = sorted_high_volt([1:numOfMaxMinValues],[1:num_cols_high_volt]);
low_volt_troughs = sorted_low_volt([1:numOfMaxMinValues],[1:num_cols_low_volt]);
% Average high and low electrode troughs.
avg_high_troughs = mean(high_volt_troughs);
avg_low_troughs = mean(low_volt_troughs);

%% Calculate peak voltages of high/low electrodes.

% Sort high and low electrodes voltage in descending order.
sorted_high_volt_desc = sort(transpose(high_volt), 'descend');
sorted_low_volt_desc = sort(transpose(low_volt), 'descend');
% Get high and low electrode voltage peaks.
high_volt_peaks = sorted_high_volt_desc([1:numOfMaxMinValues],[1:num_cols_high_volt]);
low_volt_peaks = sorted_low_volt_desc([1:numOfMaxMinValues],[1:num_cols_low_volt]);
% Average high and low electrode peaks.
avg_high_peaks = mean(high_volt_peaks);
avg_low_peaks = mean(low_volt_peaks);

%% Standard deviation calculations of low/high electrodes of trough/peak voltages.

std_high_volt_troughs = std(high_volt_troughs);
std_low_volt_troughs = std(low_volt_troughs);
std_high_volt_peaks = std(high_volt_peaks);
std_low_volt_peaks = std(low_volt_peaks);

%% Print mean trough voltages of high electrode.
fprintf('\n')
for c = 1:num_cols_high_volt
    label = 'The average trough voltage for the high electrode of Channel %i is: %0.3f V  with a standard deviation of %0.4f V.\n';
    fprintf(label, c, avg_high_troughs(c), std_high_volt_troughs(c))
end

%% Print mean peak voltages of low electrodes.
fprintf('\n')
for c = 1:num_cols_low_volt
    label = 'The average trough voltage for the low electrode of Channel %i is: %0.3f V  with a standard deviation of %0.4f V.\n';
    fprintf(label, c, avg_low_troughs(c), std_low_volt_troughs(c))
end

%% Print mean peak voltages of high electrode.
fprintf('\n')
for c = 1:num_cols_high_volt
    label = 'The average peak voltage for the high electrode of Channel %i is: %0.3f V  with a standard deviation of %0.4f V.\n';
    fprintf(label, c, avg_high_peaks(c), std_high_volt_peaks(c))
end

%% Print mean peak voltages of low electrode.
fprintf('\n')
for c = 1:num_cols_low_volt
    label = 'The average peak voltage for the low electrode of Channel %i is: %0.3f V  with a standard deviation of %0.4f V.\n';
    fprintf(label, c, avg_low_peaks(c), std_low_volt_peaks(c))
end

