# YOLOv8 Models

This folder contains models and performances brought by training a YOLOv8 model.

**Model Link:** https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Model/best.pt

## Overview
1. Introduction
<p align="justify"> 
   YOLOv8 is built on cutting-edge advancements in deep learning and computer vision, offering unparalleled performance in terms of speed and accuracy. Its streamlined design makes it suitable for various applications and easily adaptable to different hardware platforms, from edge devices to cloud APIs. Under this model, the dataset was trained under 261 layers of neural networks consisting 11,798,223 parameters.
</p>

2. Metrics Performance
<table>
   <tr>
      <td colspan = 10>
         <img src = https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Model/results.png>
         <p align="center"> Figure 1: YOLOv8 Results </p>
      </td>
   </tr>
   
   <tr><td colspan = 10></td></tr>
   
  <tr>
    <td>
       
| Metric                  | Value    |
|-------------------------|----------|
| `train/box_loss`        | 0.24595  |
| `train/seg_loss`        | 0.44298  |
| `train/cls_loss`        | 0.32934  |
| `train/dfl_loss`        | 0.95113  |
| `metrics/precision(B)`  | 0.81254  |
| `metrics/recall(B)`     | 0.78586  |
| `metrics/mAP50(B)`      | 0.82626  |
| `metrics/mAP50-95(B)`   | 0.75189  |
| `metrics/precision(M)`  | 0.81637  |
| `metrics/recall(M)`     | 0.75146  |
| `metrics/mAP50(M)`      | 0.81135  |
| `metrics/mAP50-95(M)`   | 0.7316   |
| `val/box_loss`          | 0.48191  |
| `val/seg_loss`          | 1.2007   |
| `val/cls_loss`          | 0.84366  |
| `val/dfl_loss`          | 1.132    |
| `lr/pg0`                | 8.95E-06 |
| `lr/pg1`                | 8.95E-06 |
| `lr/pg2`                | 8.95E-06 |
   </td>
   <td>
      <b>Analysis</b>
      <p align = 'justify'>
         The metrics graph for YOLOv8 shows a consistent decrease in both training and validation losses, indicating effective learning. Precision and recall metrics steadily improve, approaching values near 0.8, demonstrating the model's increasing accuracy. The mAP metrics also stabilize at high values, reflecting strong performance in object detection and segmentation tasks which is a reasonable result but not good enough.
      </p>
   </td>
  </tr>
</table>

<br></br>

<table>
   <tr>
      <th colspan = "2">
         Confusion Matrix
      </th>
   </tr>

   <tr>
      <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Model/confusion_matrix.png">
         <p align="center"> Figure 2: YOLOv8 Confusion Matrix </p>
   </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Model/confusion_matrix_normalized.png">
         <p align="center"> Figure 3: YOLOv8 Normalized Confusion Matrix </p>
   </td>
   </tr>
   <tr>
      <td colspan = "2">
         <b>Analysis</b>
         <p align = 'justify'>
            The confusion matrix for YOLOv8 shows varied performance across different categories. Bitter-gourd, Cabbage, Cauliflower, Eggplant, and Sayote achieve perfect classification accuracy. However, some categories like Bottle-Gourd and Carrots have lower accuracies of 70%. Notable misclassifications include Beef being confused with Pork and Milkfish, and Chicken with Cauliflower. Background images also show significant confusion with various categories such as Tomato and Tilapia. 
         </p>
      </td>
   </tr>
</table>

<br></br>

<table>
   <tr>
      <th colspan = "2">
         Precision, Recall, and F1 Scores
      </th>
   </tr>

   <tr>
      <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Model/BoxP_curve.png">
         <p align="center"> Figure 4: Precision Curve </p>
   </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Model/BoxR_curve.png">
         <p align="center"> Figure 5: Recall Curve </p>
   </td>
   </tr>

   <tr>
      <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Model/BoxPR_curve.png">
         <p align="center"> Figure 6: Precision-Recall Curve </p>
   </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Model/BoxF1_curve.png">
         <p align="center"> Figure 7: F1 Curve </p>
   </td>
   </tr>
   
</table>

<br></br>

## References

[^1]:https://docs.ultralytics.com/models/yolov8/

