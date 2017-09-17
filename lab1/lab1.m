% Name :Muhammad Umer Javaid
% Regno: 111238
% Class: Bese5a




%TAsk one is to show image in matlab using differnet commands
imshow('images.jpg');
img = imread('images.jpg');
imagesc(img);

subplot (1,1,1), imshow('images.jpg');



%Task two is to extract 3 channels from a color image
img = imread('images.jpg');
red=im(:,:,1);
green=im(:,:,2);
blue=im(:,:,3);
imshow(red);

%Task 3 is to resize image and save as bmg format
img=imread('images.jpg');
img1=imresize(im,0.4);
 
imwrite(img1,'bmpfile.bmp');
