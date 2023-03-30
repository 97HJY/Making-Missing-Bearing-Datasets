clc;
clear all;
close all;

drive_100 = load('100.mat');
drive_108 = load('108.mat');
drive_121 = load('121.mat');
drive_133 = load('133.mat');
drive_172 = load('172.mat');
drive_188 = load('188.mat');
drive_200 = load('200.mat');
drive_212 = load('212.mat');
drive_225 = load('225.mat');
drive_237 = load('237.mat');

% de_100 = drive_100.X100_DE_time(1:121048);
de_100 = drive_100.X100_DE_time(1:4:484192);
de_108 = drive_108.X108_DE_time(1:121048);
de_121 = drive_121.X121_DE_time(1:121048);
de_133 = drive_133.X133_DE_time(1:121048);
de_172 = drive_172.X172_DE_time(1:121048);
de_188 = drive_188.X188_DE_time(1:121048);
de_200 = drive_200.X200_DE_time(1:121048);
de_212 = drive_212.X212_DE_time(1:121048);
de_225 = drive_225.X225_DE_time(1:121048);
de_237 = drive_237.X237_DE_time(1:121048);

de_signals = [de_100,de_108,de_121,de_133,de_172,de_188,de_200,de_212,de_225,de_237];
signals = de_signals.';

save('c10signals.mat','signals');
whos('-file','c10signals.mat')