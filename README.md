# Weapon Classification

**Target:** To build a model which classifies **12 types** of **weapons**, including `Bow_and_arrow`, `Cannon`, `Dagger`, `Knife`, `Rifle`, `Shotgun`, `Tank`, `Axe`, `Handgun`, `Sword`, `Missile` and `Bomb` using Artificial Neural Networks.


**About the model:** We use a model here known as `resnet34`, trained using about `1.3` million images.

**Dataset:** We use Google's `Open Images Dataset v4` open source as a dataset. The dataset consists of `600` classes which contains `1.7` million pictures.

## Library installation
We need:

`fastai==2.7.12

`torch==2.0.1+cu118

## Dataset

We use `Google`'s [Open Images Dataset v4](https://storage.googleapis.com/openimages/web/index.html) open source as a dataset. The dataset consists of [600](https://storage.googleapis.com/openimages/2018_04/bbox_labels_600_hierarchy_visualizer/circle.html) classes which contains `1.7 million` pictures.

In order to download this, we use `OIDv4_ToolKit`. (https://github.com/EscVM/OIDv4_ToolKit)

![picture](https://raw.githubusercontent.com/EscVM/OIDv4_ToolKit/master/images/classes.png)

## Deployment
**Streamlit:** https://weaponclassification.streamlit.app/

## Further Work:


**Fine-tuning the Model**: To improve the model's performance, consider fine-tuning the pre-trained `resnet34` on a dataset specifically related to weapon classification. Fine-tuning can help the model adapt better to the nuances of weapon images.

**Data Augmentation:** Explore more advanced data augmentation techniques to increase the diversity of your training dataset. This could involve applying transformations like rotation, scaling, and cropping to the images, which may lead to better generalization.

**Hyperparameter Tuning**: Experiment with different learning rates, batch sizes, and optimizers to find the best combination for your specific problem. Hyperparameter tuning can significantly impact model performance.

**Model Ensembling:** Combine predictions from multiple models or checkpoints to improve the overall accuracy. Ensembling techniques, such as bagging or boosting, can be effective in enhancing model robustness.

**Class Imbalance Handling:** Address any class imbalance issues if present in your dataset. Techniques like oversampling, undersampling, or using class weights can help the model perform better on minority classes.

**Explainability:** Implement methods for interpreting model decisions, especially in critical applications like weapon classification. Techniques like Grad-CAM or LIME can provide insights into what features the model uses to make predictions.

**Real-world Deployment:** Consider deploying the model in real-world scenarios, such as security systems or surveillance applications. Ensure that the model's performance remains consistent in different lighting and environmental conditions.

## Conclusion:


In this project, we successfully developed a weapon classification model using the `resnet34` architecture trained on the extensive `Google Open Images Dataset v4`. The model achieved a respectable accuracy of approximately **70%** on the validation set. However, there is room for improvement.

**In conclusion**, this project lays the foundation for further enhancements. Fine-tuning, advanced data augmentation, hyperparameter tuning, and model ensembling are avenues for boosting performance. Additionally, addressing class imbalances and ensuring model explainability are crucial for practical deployment.

The weapon classification model shows promise for various applications, from security systems to law enforcement. With continued work and optimization, it has the potential to contribute significantly to the safety and security of our communities.
