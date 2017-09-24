function [ im ] = conncomp( image )
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here
% reading image 
image=imread(image);
%thresholding image to b&w
W=im2bw(image,graythresh(image)); 
% taking complement so that components in image are white and rest is black
% i.e background
W=imcomplement(W);
%imshow(W);

%using bwlabel to get labels
[labels,n]=bwlabel(W);
n

%Assign random colors ro labels
RGB=label2rgb(labels);
%show labels
imshow(RGB);
im=1


end

