clear all;
%右側に写真が配置される
file_name = uigetfile('*');
IMG = imread(file_name);
IMG = imresize(IMG,[256 256]);
IMG(:,:,1) = imadjust(IMG(:,:,1));
IMG(:,:,2) = imadjust(IMG(:,:,1));
IMG(:,:,3) = imadjust(IMG(:,:,1));
imagesc(IMG); colorbar; axis image;

IMG0 = IMG;
%左側に写真が配置される
file_name = uigetfile('*');
IMG = imread(file_name);
IMG = imresize(IMG,[256 256]);
IMG(:,:,1) = imadjust(IMG(:,:,1));
IMG(:,:,2) = imadjust(IMG(:,:,1));
IMG(:,:,3) = imadjust(IMG(:,:,1));
imagesc(IMG); colorbar; axis image;


IMG = [IMG IMG0];

imwrite(IMG,'result.png');
imagesc(IMG); colorbar; axis image;