# CS_T0828_HW4

## Reference from Github
 EDSR-TensorFlow:https://github.com/Saafke/EDSR_Tensorflow
## Environment & Hardware
 - OS win10
 - Python=3.6.12
 - TensorFlow=1.15
 - CUDA=10.1
 - CuDNN=7.6
 - GCC=9.2
 
 - CPU: AMD Ryzen R5-5600X
 - RAM: 16G*2
 - GPU: NVIDIA GTX1060 6G
 
 ## Files Discription
 - **repository-EDSR_Tensorflow**:This is reference from https://github.com/Saafke/EDSR_Tensorflow. you can download the code from that repository.
 - **repository-bicubic**: There is the result of using bicubic to upscale the image by scale 3.
 - **repository-original result**: There is the result of EDSR using original training dataset.
 - **repository-final result**: There is the result of EDSR using my augmented training dataset.
 - **preprocess.py**: You can run this file to obtain augmented training dataset.
 
 ## Reproducing Submission
    +-EDSR-TensorFlow
    |  +-training_hr_images
    |  |  -training_images
    |  +-testing_lr_images
    |  |  -testing_images
    |  data_utils.py
    |  edsr.py
    |  main.py
    |  preprocess.py
    |  run.py
 
 To reproduce my submission, you can follow following steps:
 #### 1. Download EDSR-Tensorflow
   You can download the source code from above or from [here](https://github.com/Saafke/EDSR_Tensorflow). After download the code, please create folder just like above.
   I have modified some codes so that it can output images normally.
 #### 2. Download dataset
   You can download thte dataset from [here](https://drive.google.com/drive/u/0/folders/1H-sIY7zj42Fex1ZjxxSC3PV1pK4Mij6x).
 #### 3. Run
   Now, you can run EDSR. The running details is in README.md in EDSR-TensorFlow repository. Here I only list instruction I used.
   - Train  ``` python main.py --train --fromscratch --scale 3 --traindir /path/to/train_images --epochs 30```
   - Test   ``` python main.py --upscale --scale 3 --image /path/to/test_images```
   
 ## Brief Introduction
  In this assignment, our major task is to do super-resolution on given shrinked Set14. About the training images, we have only 291 provided images with different size. And we need to train a model then reconstructed the low-resolution images by scale of 3. I choose to train EDSR as my model, and I do some easy trick to augment the training dataset. I will introduce it later. Finally, I got the PSNR=25.637 with my result.
  
 ## Methodology
 ![images](https://github.com/kyliao426/CS_T0828_HW4/blob/main/EDSR_Tensorflow-master/images/EDSR.png) </br>
  The major feature od EDSR is its residual blocks, the author removes the batch normalization layers from residual blocks. The author thinks that Since batch normalization layers normalize the features, they get rid of range flexibility from networks by normalizing the features, it is better to remove them. And because of removal of batch normalization layers, EDSR can save approximately 40% of memory usage during training, compared to SRResNet. Consequently, it can build up a larger model that has better performance than conventional ResNet structure under limited computational resources. In summary, EDSR has 32 residual blocks and 256 filters which is 2 times and 4 times more than SRResNet’s 16 and 64.
  Following are some hyperparameters in my experiment.
  | Hyperparameters | Batch size | Epochs | Learning rate |
  |----|----|----|----|
  | value | 16 | 30 | 0.0001 |
  
 ## Final Result
  <img src="https://github.com/kyliao426/CS_T0828_HW4/blob/main/bicubic/04.png" > 
      bicubic
  <img src="https://github.com/kyliao426/CS_T0828_HW4/blob/main/original%20result/04.png" >
      using original dataset
  <img src="https://github.com/kyliao426/CS_T0828_HW4/blob/main/final%20result/04.png" > 
      using my augmented dataset
   
  <img src="https://github.com/kyliao426/CS_T0828_HW4/blob/main/bicubic/08.png" > 
      bicubic
  <img src="https://github.com/kyliao426/CS_T0828_HW4/blob/main/original%20result/08.png" >
      using original dataset
  <img src="https://github.com/kyliao426/CS_T0828_HW4/blob/main/final%20result/08.png" > 
      using my augmented dataset
   
  <img src="https://github.com/kyliao426/CS_T0828_HW4/blob/main/bicubic/09.png" > 
      bicubic
  <img src="https://github.com/kyliao426/CS_T0828_HW4/blob/main/original%20result/09.png" >
      using original dataset
  <img src="https://github.com/kyliao426/CS_T0828_HW4/blob/main/final%20result/09.png" > 
      using my augmented dataset
    
  <img src="https://github.com/kyliao426/CS_T0828_HW4/blob/main/bicubic/11.png" > <img src="https://github.com/kyliao426/CS_T0828_HW4/blob/main/original%20result/11.png" > <img src="https://github.com/kyliao426/CS_T0828_HW4/blob/main/final%20result/11.png" > </br>
  bicubic/using original dataset/using my augmented dataset </br>
  psnr 24.881/25.532/25.637
 
