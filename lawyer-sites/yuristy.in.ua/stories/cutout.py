import onnxruntime as ort, numpy as np, cv2
from PIL import Image, ImageFilter
im=Image.open('khmelnytskyi.jpg').convert('RGB')
s=ort.InferenceSession('/tmp/u2net_human_seg.onnx')
x=np.asarray(im.resize((320,320),Image.BILINEAR)).astype('float32')/255
x=(x-[0.485,0.456,0.406])/[0.229,0.224,0.225]; x=x.transpose(2,0,1)[None].astype('float32')
m=s.run(None,{s.get_inputs()[0].name:x})[0][0,0]
m=(m-m.min())/(m.max()-m.min())
M=Image.fromarray((m*255).astype('uint8')).resize(im.size,Image.BICUBIC)
a=np.asarray(M).astype('float32')/255
a=np.clip((a-0.35)/0.4,0,1)                       # різкіший край
b=(a>0.5).astype('uint8')*255
b=cv2.morphologyEx(b,cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(25,25)))
ff=b.copy(); h,w=ff.shape; mask=np.zeros((h+2,w+2),np.uint8); cv2.floodFill(ff,mask,(0,0),255)
holes=cv2.bitwise_not(ff)                      # внутрішні дірки
filled=cv2.bitwise_or(b,holes).astype('float32')/255
a=np.maximum(a,filled*(1.0))
a=cv2.GaussianBlur(a,(0,0),1.2)
W2,H2=im.width*2,im.height*2
big=im.resize((W2,H2),Image.LANCZOS)
A=Image.fromarray((cv2.resize(a,(W2,H2),interpolation=cv2.INTER_CUBIC).clip(0,1)*255).astype('uint8'))
out=big.convert('RGBA'); out.putalpha(A); out.save('portrait-cutout.png')
bg=Image.new('RGBA',out.size,(63,76,138,255)); bg.alpha_composite(out); bg.convert('RGB').resize((640,640)).save('/tmp/cut_check.jpg')
