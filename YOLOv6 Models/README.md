# YOLOv6 Models

This folder contains models and performances brought by training a YOLOv6 model.

**Model Link:** https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/best.pt

## Overview
1. Introduction
<p align="justify"> YOLOv6 is an object detection model that offers remarkable balance between speed and accuracy, making it a popular choice for real-time applications. This model introduces several notable enhancements on its architecture and training scheme, including the implementation of a Bi-directional Concatenation (BiC) module, an anchor-aided training (AAT) strategy, and an improved backbone and neck design for state-of-the-art accuracy on the COCO dataset. It was trained under 142 layers of neural networks consisting 4,235,823 parameters.</p>

2. Metrics Performance
<table>
   <tr>
      <td colspan = 10>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/results.png">
         <p align="center"> Figure 1: YOLOv6 Results </p>
      </td>
   </tr>
   
   <tr><td colspan = 10></td></tr>
   
  <tr>
    <td>

| Metric                  | Value    |
|-------------------------|----------|
| `train/box_loss`        | 0.36346  |
| `train/cls_loss`        | 0.59692  |
| `train/dfl_loss`        | 1.0571   |
| `metrics/precision(B)`  | 0.823    |
| `metrics/recall(B)`     | 0.76092  |
| `metrics/mAP50(B)`      | 0.81639  |
| `metrics/mAP50-95(B)`   | 0.71952  |
| `val/box_loss`          | 0.54164  |
| `val/cls_loss`          | 0.84549  |
| `val/dfl_loss`          | 1.2003   |
| `lr/pg0`                | 7.96E-06 |
| `lr/pg1`                | 7.96E-06 |
| `lr/pg2`                | 7.96E-06 |

   </td>
   <td>

### Analysis
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
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/confusion_matrix.png">
         <p align="center"> Figure 2: YOLOv6 Confusion Matrix </p>
   </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/confusion_matrix_normalized.png">
         <p align="center"> Figure 3: YOLOv6 Normalized Confusion Matrix </p>
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
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/P_curve.png">
         <p align="center"> Figure 4: Precision Curve </p>
   </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/R_curve.png">
         <p align="center"> Figure 5: Recall Curve </p>
   </td>
   </tr>

   <tr>
      <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/PR_curve.png">
         <p align="center"> Figure 6: Precision-Recall Curve </p>
   </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/F1_curve.png">
         <p align="center"> Figure 7: F1 Curve </p>
   </td>
   </tr>
   
</table>

<br></br>

