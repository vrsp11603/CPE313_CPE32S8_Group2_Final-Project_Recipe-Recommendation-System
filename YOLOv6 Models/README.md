# YOLOv6 Models

This folder contains models and performances brought by training a YOLOv6 model.

## Overview
1. Introduction
<p align="justify"> YOLOv6 is an object detection model that offers remarkable balance between speed and accuracy, making it a popular choice for real-time applications. This model introduces several notable enhancements on its architecture and training scheme, including the implementation of a Bi-directional Concatenation (BiC) module, an anchor-aided training (AAT) strategy, and an improved backbone and neck design for state-of-the-art accuracy on the COCO dataset [^1]. It was trained under 142 layers of neural networks consisting 4,235,823 parameters.</p>

2. Metrics Performance
   
![alt text][image]

[image]: https://github.com/vrsp11603/CPE313_CPE32S8_Group2_Final-Project_Recipe-Recommendation-System/blob/main/YOLOv6%20Models/results.png "YOLOv6 Model Results"

<p align="center"> Figure 1: YOLOv6 Results </p>



<table>
   <tr>
      <th colspan = "2">
         **Confusion Matrix**
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


4. Testing Result

## References
{^1]: https://docs.ultralytics.com/models/yolov6/
