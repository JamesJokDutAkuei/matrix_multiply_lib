## 📄 README: Queen Loss in Africanized Honeybee Dataset – PCA Project

This project analyzes the **queen loss Africanized honeybee dataset** using **Principal Component Analysis (PCA)** to explore patterns and reduce the dimensionality of the dataset for visualization and interpretation. The work was divided evenly among the four team members.

### 👩🏽‍💻 Mariam Awini Issah

**Tasks: Question 1 & Question 2**

- **Question 1**:
  Mariam handled **loading and exploring the dataset**.

  - Imported required libraries (`pandas`, `numpy`, `matplotlib`, etc.)
  - Loaded the dataset `queen_loss_africanized_honeybee_dataset.csv` using `pandas`.
  - Displayed the structure of the dataset including columns, data types, and summary statistics.
  - Checked for missing values and basic cleaning if needed.

- **Question 2**:
  Mariam worked on **data preprocessing and normalization**.

  - Selected relevant numerical features for PCA.
  - Scaled the features using `StandardScaler` to ensure each feature contributed equally.
  - Verified the transformation by inspecting mean and variance after scaling.

### 👨🏽‍💻 David

**Tasks: Question 3 & Question 4**

- **Question 3**:
  David applied **Principal Component Analysis (PCA)** on the preprocessed data.

  - Imported `PCA` from `sklearn.decomposition`.
  - Fit the PCA model on the normalized dataset.
  - Computed the principal components and explained variance ratio.

- **Question 4**:
  David handled **variance analysis and component selection**.

  - Plotted a **scree plot** to show the explained variance by each principal component.
  - Decided on the number of components to keep (e.g., those explaining 95% of the variance).
  - Interpreted the result and explained the dimensionality reduction decision.

### 👨🏽‍💻 James

**Tasks: Question 5 & Question 6**

- **Question 5**:
  James implemented the **projection of original data onto the principal components**.

  - Generated a reduced dataset using the chosen principal components.
  - Stored the reduced data in a DataFrame for visualization and further analysis.

- **Question 6**:
  James attempted **2D visualizations** of the PCA output.

  - Created scatter plots using `matplotlib` and `seaborn` to visualize distributions.
  - Faced a `KeyError` during plotting, which was debugged and fixed.
  - Ensured clean visual output by hiding spines and adding axis labels.

### 👨🏽‍💻 Innocente

**Tasks: Question 7 & Question 8**

- **Question 7**:
  Innocente analyzed the **PCA component loadings**.

  - Interpreted how each original feature contributes to the principal components.
  - Displayed component weights in a structured format for easy understanding.

- **Question 8**:
  Innocente completed the project by **comparing original vs PCA-reduced data visually**.

  - Plotted both original data (first two features) and PCA-reduced data side-by-side.
  - Helped interpret the transformation and visualize the dimensionality reduction effectively.

### In Summary

In this project, we worked together as a team to understand and apply Principal Component Analysis (PCA) to a real-world biological dataset. Each of us contributed equally to different parts of the process from data cleaning and preprocessing to dimensionality reduction and visualization. Through our collaboration, we were able to reduce the dataset to fewer dimensions while preserving most of the important information, resulting in a clear and meaningful analysis.
