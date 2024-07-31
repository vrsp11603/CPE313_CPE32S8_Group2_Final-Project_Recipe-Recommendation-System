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

