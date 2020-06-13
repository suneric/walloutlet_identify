### Electical wall outlet detection with OpenCV CascadeClassifier

# Install OpenCV
  - build from [source](https://docs.opencv.org/master/d7/d9f/tutorial_linux_install.html)
  - make sure the opencv libs are built and installed (usually in '/usr/bin/') and the path is sourced.

# STEP 1: Make the positive and negative images
- Make positive images: `python modify_image [source dir] [positive dir] [width] [height]`
  Put the images of target object in the 'source dir', and the target images with specified shape will be generated in 'positive dir'
- Download background images from image-net: `python download_image.py [start_index] [url]`
  The images will be downloaded in 'neg' folder, an example of 'url': http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n01905661
- Generate negative images: `python make_training_data [negative dir] [type]`
  Type for negative is 'neg', a bg.txt file will be created for background images
# STEP 2: Create training samples
- `opencv_createsamples -img [pos.jpg] -bg bg.txt -info info/info.lst -num [number of postive sampels]`
  The postive sampels created in 'info' folder
- `opencv_createsamples -info info/info.lst -num [number of samples] -w 20 -h 20 -vec positives.vec`
  A vector file will be created
# STEP 3: Training
- `opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20`
  A general rule for ration of pos:neg images is 2:1, amd 10-20 at least stages.
  A cascade file (xml) will be generated which can be used for detection
# STEP 4: Play detection
- `python cascade_classifier.py [test image] [cascade_file]` with providing a test image containing target object


# reference
- [1] [OpenCV Cascade Classifier Training](https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/)
- [2] [Creating your own Haar Cascade OpenCV Python Tutorial](https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/)
