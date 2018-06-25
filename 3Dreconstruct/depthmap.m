load('webcamsSceneReconstruction.mat');

I1=imread('right.png');
I2=imread('left.png');

[J1,J2]=rectifyStereoImages(I1,I2,stereoParams);

figure
imshow(cat(3,I1(:,:,1),I2(:,:,2:3)),'InitialMagnification',50);

disparityMap = disparity(rgb2gray(I1), rgb2gray(I2));
figure
imshow(disparityMap,[0,300],'InitialMagnification',50);
