# YOLOv6 Models

This folder contains models and performances brought by training a YOLOv6 model.

## Overview
1. Introduction
<p align="justify"> YOLOv6 is an object detection model that offers remarkable balance between speed and accuracy, making it a popular choice for real-time applications. This model introduces several notable enhancements on its architecture and training scheme, including the implementation of a Bi-directional Concatenation (BiC) module, an anchor-aided training (AAT) strategy, and an improved backbone and neck design for state-of-the-art accuracy on the COCO dataset [^1]. It was trained under 142 layers of neural networks consisting 4,235,823 parameters.</p>

2. Metrics Performance
<table>
   <tr>
      <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/results.png">
         <p align="center"> Figure 1: YOLOv6 Results </p>
      </td>
   </tr>
</table>

<div class="row">
  <div class="column">
    <table>
        <thead>
            <tr>
                <th>Train Box Loss</th>
                <th>Train Class Loss</th>
                <th>Train DFL Loss</th>
                <th>Precision (B)</th>
                <th>Recall (B)</th>
                <th>mAP50 (B)</th>
                <th>mAP50-95 (B)</th>
                <th>Validation Box Loss</th>
                <th>Validation Class Loss</th>
                <th>Validation DFL Loss</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>0.36346</td>
                <td>0.59692</td>
                <td>1.0571</td>
                <td>0.823</td>
                <td>0.76092</td>
                <td>0.81639</td>
                <td>0.71952</td>
                <td>0.54164</td>
                <td>0.84549</td>
                <td>1.2003</td>
            </tr>
        </tbody>
    </table>     
  </div>
  <div class="column">
     <p align = 'justify'>
        The graphs indicate that the object detection model shows significant improvement in performance over time. Both box and classification losses for training and validation steadily decrease, indicating enhanced accuracy in predicting bounding boxes and classifying objects. Precision and recall metrics stabilize above 0.8, reflecting high accuracy and the model's capability to identify true objects with low false positive and negative rates. The mean average precision (mAP) metrics, particularly mAP@50 and mAP@50-95, demonstrate strong and robust detection performance. 
     </p>
  </div>
</div>

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
</table>

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


4. Testing Result
<table>
   <tr>
      <th colspan = "2">
         Validation Prediction
      </th>
   </tr>

   <tr>
      <th>
         True Labels
      </th>
      <th>
         Predicted Labels
      </th>
   </tr>

   <tr>
      <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/val_batch0_labels.jpg">
         <p align="center"> Figure 8: Validation Batch 1 True Labels </p>
      </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/val_batch0_pred.jpg">
         <p align="center"> Figure 9: Validation Batch 1 Predicted Labels </p>
      </td>
   </tr>

   <tr>
      <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/val_batch1_labels.jpg">
         <p align="center"> Figure 10: Validation Batch 2 True Labels </p>
      </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/val_batch1_pred.jpg">
         <p align="center"> Figure 11: Validation Batch 2 Predicted Labels </p>
      </td>
   </tr>

   <tr>
      <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/val_batch2_labels.jpg">
         <p align="center"> Figure 12: Validation Batch 3 True Labels </p>
      </td>
      
   <td>
         <img src = "https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/val_batch2_pred.jpg">
         <p align="center"> Figure 13: Validation Batch 3 Predicted Labels </p>
      </td>
   </tr>
   
</table>

## References
[^1]: https://docs.ultralytics.com/models/yolov6/
