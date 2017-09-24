


function [ im ] = change_color( image )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

image=imread(image);
red=image(:,:,1);
green=image(:,:,2);
blue=image(:,:,3);

conv_red=red>120 & green<=120;
red(conv_red)=255;
green(conv_red)=255;
blue(conv_red)=0;

conv_green=green>120 & red<=120;
red(conv_green)=0;
green(conv_green)=255;
blue(conv_green)=255;

conv_blue=blue>180 & green<=180;
red(conv_blue)=255;
green(conv_blue)=0;
blue(conv_blue)=255;

im=cat(3,red,green,blue);

end

 
