clear all;
%右側に写真が配置される(深度画像)
file_name = uigetfile('*');
IMG = imread(file_name);
%バイラテラルフィルタ
patch = imcrop(IMG,[50, 50, 50 50]);
imshow(patch);
patchVar = std2(patch)^2;
DoS = 2*patchVar;
IMG = imbilatfilt(IMG,DoS);
imshow(IMG);
IMG = imbilatfilt(IMG,DoS,2);
imshow(IMG);
IMG = imresize(IMG,[256 256]);
IMG(:,:,1) = imadjust(IMG(:,:,1));
IMG(:,:,2) = imadjust(IMG(:,:,1));
IMG(:,:,3) = imadjust(IMG(:,:,1));
%ヒストグラム
%IMG = histeq(IMG);
imagesc(IMG); colorbar; axis image;

IMG0 = IMG;
%左側に写真が配置される(RGB画像)
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