clear all;
%�E���Ɏʐ^���z�u�����(�[�x�摜)
file_name = uigetfile('*');
IMG = imread(file_name);
IMG = imresize(IMG,[256 256]);
IMG(:,:,1) = imadjust(IMG(:,:,1));
IMG(:,:,2) = imadjust(IMG(:,:,1));
IMG(:,:,3) = imadjust(IMG(:,:,1));
IMG = histeq(IMG);
imagesc(IMG); colorbar; axis image;

IMG0 = IMG;
%�����Ɏʐ^���z�u�����(RGB�摜)
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