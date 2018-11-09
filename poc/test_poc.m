close all; 
%2�̉摜���C���v�b�g
img   = imread('lena.tif');
imagesc(img)
pause;
%�摜���w�肵���p�x�ɉ�]
IMG=imrotate(img,40,'bilinear','crop');
imagesc(IMG);
pause;
%2�����t�[���G�ϊ����v�Z
img   = fftshift(img(:,:,2));
f     = fft2(img);
pause;
IMG=fftshift(IMG(:,:,2));
F=fft2(IMG);
pause;
%���ꂼ��̉摜�̐U���X�y�N�g���ƈʑ��X�y�N�g�����v�Z
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
%���ꂼ��̉摜�̈ʑ��X�y�N�g��������
IM=imfuse(ang,ANG,'blend','Scaling','joint');
imshow(IM);
pause;
%���������ʑ��X�y�N�g�����t2�����t�[���G�ϊ�
inv=ifft2(IM);
inv=abs(inv).^2;
imresize(inv,[512 512]);
imshow(ans);