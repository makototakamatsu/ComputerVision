close all; 
%2つの画像をインプット
img   = imread('lena.tif');
imagesc(img)
pause;
%画像を指定した角度に回転
IMG=imrotate(img,40,'bilinear','crop');
imagesc(IMG);
pause;
%2次元フーリエ変換を計算
img   = fftshift(img(:,:,2));
f     = fft2(img);
pause;
IMG=fftshift(IMG(:,:,2));
F=fft2(IMG);
pause;
%それぞれの画像の振幅スペクトルと位相スペクトルを計算
imagesc(100*log(1+abs(fftshift(f)))); colormap(hot); 
title('magnitude spectrum');
pause;
ang=angle(f);
imagesc(ang);  colormap(gray);
title('phase spectrum');
pause;
imagesc(100*log(1+abs(fftshift(F)))); colormap(hot); 
title('magnitude spectrum');
pause;
ANG=angle(F);
imagesc(ANG);  colormap(gray);
title('phase spectrum');
pause;
%それぞれの画像の位相スペクトルを合成
IM=imfuse(ang,ANG,'blend','Scaling','joint');
imshow(IM);
pause;
%合成した位相スペクトルを逆2次元フーリエ変換
inv=ifft2(IM);
inv=abs(inv).^2;
imresize(inv,[512 512]);
imshow(ans);