# YOLOv9 Models

This folder contains models and performances brought by training a YOLOv9 model.

**Model Link:** https://drive.google.com/file/d/1UW--VDQkGRcNoGI5QVwGuhQcMYTPY9IJ/view?usp=sharing

## Overview
1. Introduction
<p align="justify"> 
   YOLOv9 builds on its predecessors by incorporating improved backbone networks, spatial pyramid pooling, and attention mechanisms for better feature extraction and multi-scale object detection. It uses anchor-free detection and sophisticated loss functions like CIoU for improved accuracy and localization. YOLOv9 maintains the YOLO family’s philosophy of high-speed, real-time object detection with enhanced precision and efficiency. Under this model, the dataset was trained under 618 layers of neural networks consisting 25,548,507 parameters.
</p>

2. Metrics Performance
<table>
   <tr>
      <td colspan = 10>
         <img src = https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv9%20Model/results.png>
         <p align="center"> Figure 1: YOLOv9 Results </p>
      </td>
   </tr>
   
   <tr><td colspan = 10></td></tr>
   
  <tr>
    <td>
       
| Metric                  | Value    |
|-------------------------|----------|
| `train/box_loss`        | 0.38486  |
| `train/cls_loss`        | 0.21674  |
| `train/dfl_loss`        | 1.0511   |
| `metrics/precision(B)`  | 0.91963  |
| `metrics/recall(B)`     | 0.91533  |
| `metrics/mAP50(B)`      | 0.95399  |
| `metrics/mAP50-95(B)`   | 0.77917  |
| `val/box_loss`          | 0.73456  |
| `val/cls_loss`          | 0.42685  |
| `val/dfl_loss`          | 1.2933   |
| `lr/pg0`                | 1.48E-05 |
| `lr/pg1`                | 1.48E-05 |
| `lr/pg2`                | 1.48E-05 |
   </td>
   <td>
      
### Analysis
   <p align = 'justify'>
   The YOLOv9 metrics show significant improvements in model performance, with loss values consistently decreasing and stabilizing. Training and validation box losses fall below 0.5, and classification losses settle around 0.5 for training and 0.75 for validation. Precision and recall exceed 0.9, indicating high accuracy. Mean average precision (mAP) metrics stabilize around 0.95 (mAP@50) and 0.78 (mAP@50-95), reflecting robust performance. Overall, YOLOv9 achieves high accuracy and precision in ingredient detection.
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
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv9%20Model/confusion_matrix.png">
         <p align="center"> Figure 2: YOLOv9 Confusion Matrix </p>
   </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv9%20Model/confusion_matrix_normalized.png">
         <p align="center"> Figure 3: YOLOv9 Normalized Confusion Matrix </p>
   </td>
   </tr>
   <tr>
      <td colspan = "2">

### Analysis
   <p align = 'justify'>
   This figure shows the confusion matrix for YOLOv9 shows high accuracy for most categories, with many items having near-perfect precision and recall. Beef, BitterGourd, Pumpkin, and Sayote achieve 100% correct classifications. Other items like Chicken, Broccoli, and Cabbage also exhibit high accuracy, although there are some misclassifications, such as Carrots being confused with Broccoli and Galunggong with Milkfish. Overall, YOLOv9 performs robustly across various categories, maintaining high precision and recall
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
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv9%20Model/P_curve.png">
         <p align="center"> Figure 4: Precision Curve </p>
   </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv9%20Model/R_curve.png">
         <p align="center"> Figure 5: Recall Curve </p>
   </td>
   </tr>

   <tr>
      <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv9%20Model/PR_curve.png">
         <p align="center"> Figure 6: Precision-Recall Curve </p>
   </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv9%20Model/F1_curve.png">
         <p align="center"> Figure 7: F1 Curve </p>
   </td>
   </tr>
   
</table>

<br></br>

## References

[^1]:https://docs.ultralytics.com/models/yolov9/

