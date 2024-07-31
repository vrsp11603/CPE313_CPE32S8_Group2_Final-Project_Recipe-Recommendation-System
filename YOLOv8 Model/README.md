# YOLOv8 Models

This folder contains models and performances brought by training a YOLOv6 model.

## Overview
1. Introduction
<p align="justify"> YOLOv8 
   Dataset was trained under 261 layers of neural networks consisting 11,798,223 parameters.</p>

2. Metrics Performance
<table>
   <tr>
      <td colspan = 10>
         <img src = https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Model/results.png>
         <p align="center"> Figure 1: YOLOv8 Results </p>
      </td>
   </tr>
   
   <tr><td colspan = 10></td></tr>
   
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
| `lr/pg0`                | 8.95e-06 |
| `lr/pg1`                | 8.95e-06 |
| `lr/pg2`                | 8.95e-06 |
<tr><td colspan = 10></td></tr>
      <tr>
         <td colspan = 10>
              <p align = 'justify'>
        The graphs indicate that the object detection model shows significant improvement in performance over time. Both box and classification losses for training and validation steadily decrease, indicating enhanced accuracy in predicting bounding boxes and classifying objects. Precision and recall metrics stabilize above 0.8, reflecting high accuracy and the model's capability to identify true objects with low false positive and negative rates. The mean average precision (mAP) metrics, particularly mAP@50 and mAP@50-95, demonstrate strong and robust detection performance. 
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
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Models/confusion_matrix.png">
         <p align="center"> Figure 2: YOLOv8 Confusion Matrix </p>
   </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Models/confusion_matrix_normalized.png">
         <p align="center"> Figure 3: YOLOv8 Normalized Confusion Matrix </p>
   </td>
   </tr>
   <tr>
      <td colspan = "2">
         <p align = 'justify'>
   The confusion matrix indicates perfect accuracy in detecting bitter gourd and eggplant, and high accuracy for cabbage and cauliflower. However, there are significant misclassifications for chicken, garlic, and especially ginger. Misclassifications frequently occur between similar-looking ingredients, such as pork with beef and papaya, and ginger with garlic.
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
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Models/BoxP_curve.png">
         <p align="center"> Figure 4: Precision Curve </p>
   </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Models/BoxR_curve.png">
         <p align="center"> Figure 5: Recall Curve </p>
   </td>
   </tr>

   <tr>
      <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Models/BoxPR_curve.png">
         <p align="center"> Figure 6: Precision-Recall Curve </p>
   </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv8%20Models/BoxF1_curve.png">
         <p align="center"> Figure 7: F1 Curve </p>
   </td>
   </tr>
   
</table>

<br></br>

## References

[^1]:https://docs.ultralytics.com/models/yolov8/

