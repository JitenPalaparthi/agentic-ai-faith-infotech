# Machine Learning Algorithms --- Quick Reference

  -----------------------------------------------------------------------
  Algorithm               Type                    Example Use Case
  ----------------------- ----------------------- -----------------------
  Linear Regression       Supervised --           Predict house prices
                          Regression              

  Polynomial Regression   Supervised --           Predict nonlinear sales
                          Regression              trends

  Ridge Regression        Supervised --           Predict prices with
                          Regression              many correlated
                                                  features

  Lasso Regression        Supervised --           Prediction with feature
                          Regression              selection

  Logistic Regression     Supervised --           Predict customer churn
                          Classification          

  Decision Tree           Supervised --           Loan approval
                          Classification /        
                          Regression              

  Random Forest           Supervised --           Fraud detection
                          Classification /        
                          Regression              

  K-Nearest Neighbors     Supervised --           Classify customers
  (KNN)                   Classification /        
                          Regression              

  Support Vector Machine  Supervised --           Email spam detection
  (SVM)                   Classification          

  Support Vector          Supervised --           Predict property prices
  Regression (SVR)        Regression              

  Naive Bayes             Supervised --           Spam filtering
                          Classification          

  Gradient Boosting       Supervised --           Credit-risk prediction
                          Classification /        
                          Regression              

  XGBoost                 Supervised --           Customer churn
                          Classification /        prediction
                          Regression              

  LightGBM                Supervised --           Large-scale tabular
                          Classification /        prediction
                          Regression              

  CatBoost                Supervised --           Prediction with
                          Classification /        categorical data
                          Regression              

  Neural Network          Supervised\*            Image classification

  K-Means                 Unsupervised --         Customer segmentation
                          Clustering              

  Hierarchical Clustering Unsupervised --         Group similar customers
                          Clustering              

  DBSCAN                  Unsupervised --         Geographic/location
                          Clustering              clustering

  Gaussian Mixture Model  Unsupervised --         Customer behavior
  (GMM)                   Clustering              segmentation

  PCA                     Unsupervised --         Reduce number of
                          Dimensionality          features
                          Reduction               

  t-SNE                   Unsupervised --         Visualize
                          Dimensionality          high-dimensional data
                          Reduction               

  UMAP                    Unsupervised\* --       Visualize embeddings
                          Dimensionality          
                          Reduction               

  Isolation Forest        Unsupervised -- Anomaly Detect unusual
                          Detection               transactions

  Local Outlier Factor    Unsupervised -- Anomaly Detect abnormal sensor
                          Detection               readings

  One-Class SVM           Unsupervised / Novelty  Detect abnormal machine
                          Detection               behavior

  Apriori                 Unsupervised --         Find products
                          Association Rules       frequently purchased
                                                  together

  Autoencoder             Unsupervised /          Anomaly detection and
                          Self-Supervised         compression

  Q-Learning              Reinforcement Learning  Learn maze navigation

  SARSA                   Reinforcement Learning  Robot navigation

  Deep Q-Network (DQN)    Reinforcement Learning  Game-playing agent

  REINFORCE               Reinforcement Learning  Learn action policies

  Actor-Critic            Reinforcement Learning  Robot control

  PPO                     Reinforcement Learning  Robotics and agent
                                                  training

  DDPG                    Reinforcement Learning  Continuous robot
                                                  control

  SAC                     Reinforcement Learning  Continuous-control
                                                  tasks
  -----------------------------------------------------------------------

## Quick Rule

-   **Supervised Learning** --- learns from labeled data.
-   **Unsupervised Learning** --- discovers patterns in unlabeled data.
-   **Reinforcement Learning** --- learns actions through rewards and
    penalties.

> **Note:** Neural networks and UMAP are not restricted to the category
> shown above; they can also be used in other learning setups.
