# steganography
 **Technical Specifications:**
 
 - Mode write:
  

```console 
$  python main.py png.png -w -f image.png -t "any text that you want to hide" newImage.png
```

```console
$  python main.py -w image.png -t "any text that you want to hide"                        
``` 
  
    Enter the name of your image :
    >>>test.png

```console
$  python main.py -w image.png -f  newImage.png                     
``` 
  
    Enter the text you want to hide : 
    >>>any text that you want to hide


```console
$  python main.py -w image.png                             
``` 
  
    Enter the name of your image :
    >>>newImamge.png
    Enter your text:
    >>>any text that you want to hide


- Mode read:

```console 
$  python main.py newImage.png
```
    print the text you have hidden on newImage.png
