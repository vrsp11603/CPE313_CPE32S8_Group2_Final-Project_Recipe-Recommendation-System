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
    <td>
      <h3>Metrics</h3>
      <table>
        <tr>
          <th>Metric</th>
          <th>Value</th>
        </tr>
        <tr>
          <td>`train/box_loss`</td>
          <td>0.24595</td>
        </tr>
        <tr>
          <td>`train/seg_loss`</td>
          <td>0.44298</td>
        </tr>
        <tr>
          <td>`train/cls_loss`</td>
          <td>0.32934</td>
        </tr>
        <tr>
          <td>`train/dfl_loss`</td>
          <td>0.95113</td>
        </tr>
        <tr>
          <td>`metrics/precision(B)`</td>
          <td>0.81254</td>
        </tr>
        <tr>
          <td>`metrics/recall(B)`</td>
          <td>0.78586</td>
        </tr>
        <tr>
          <td>`metrics/mAP50(B)`</td>
          <td>0.82626</td>
        </tr>
        <tr>
          <td>`metrics/mAP50-95(B)`</td>
          <td>0.75189</td>
        </tr>
        <tr>
          <td>`metrics/precision(M)`</td>
          <td>0.81637</td>
        </tr>
        <tr>
          <td>`metrics/recall(M)`</td>
          <td>0.75146</td>
        </tr>
        <tr>
          <td>`metrics/mAP50(M)`</td>
          <td>0.81135</td>
        </tr>
        <tr>
          <td>`metrics/mAP50-95(M)`</td>
          <td>0.7316</td>
        </tr>
        <tr>
          <td>`val/box_loss`</td>
          <td>0.48191</td>
        </tr>
        <tr>
          <td>`val/seg_loss`</td>
          <td>1.2007</td>
        </tr>
        <tr>
          <td>`val/cls_loss`</td>
          <td>0.84366</td>
        </tr>
        <tr>
          <td>`val/dfl_loss`</td>
          <td>1.132</td>
        </tr>
        <tr>
          <td>`lr/pg0`</td>
          <td>8.95e-06</td>
        </tr>
        <tr>
          <td>`lr/pg1`</td>
          <td>8.95e-06</td>
        </tr>
        <tr>
          <td>`lr/pg2`</td>
          <td>8.95e-06</td>
        </tr>
      </table>
    </td>
    <td>
      <h3>Analysis</h3>
      <p align="justify">
        The graphs indicate that the object detection model shows significant improvement in performance over time. Both box and classification losses for training and validation steadily decrease, indicating enhanced accuracy in predicting bounding boxes and classifications. The steady decrease in losses reflects improved model training and generalization, leading to better performance metrics across both training and validation datasets.
      </p>
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

